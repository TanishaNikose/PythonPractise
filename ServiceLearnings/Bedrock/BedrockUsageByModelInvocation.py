# """Report Bedrock model invocations from CloudWatch Logs Insights.

# Prerequisites: model invocation logging enabled in the target region,
# logs delivered to the configured log group, and AWS credentials with
# logs:StartQuery and logs:GetQueryResults permissions.
# """

# # It is filtering data for one user i.e. Tanisha

# import os
# import sys
# import time
# from datetime import datetime, timedelta, timezone

# import boto3
# from botocore.exceptions import BotoCoreError, ClientError, ProfileNotFound 

# REGION = os.getenv('AWS_REGION', 'us-east-1')
# PROFILE = os.getenv('AWS_PROFILE')
# LOG_GROUP = os.getenv('BEDROCK_LOG_GROUP', '/aws/bedrock/model-invocations-poc')
# IAM_ARN = os.getenv('BEDROCK_IAM_ARN', 'arn:aws:iam::817977002522:user/Tanisha')
# HOURS = int(os.getenv('BEDROCK_REPORT_HOURS', '24'))

# # IAM identity is supplied by AWS in invocation logging. Metadata is optional.
# QUERY = """
# fields identity.arn as iamUser,
#        modelId,
#        input.inputTokenCount as inputTokenValue,
#        output.outputTokenCount as outputTokenValue
# | filter identity.arn = "__IAM_ARN__"
# | stats count(*) as requests,
#         sum(inputTokenValue) as inputTokens,
#         sum(outputTokenValue) as outputTokens
#   by iamUser, modelId
# | sort requests desc
# """

# # Converting the data into python dictionary from cloudwatch
# def rows_to_dicts(rows):   
#     return [{cell['field']: cell.get('value', '') for cell in row} for row in rows]


# # To connect with AWS → run the query for CloudWatch Logs Insights  → wait till query complete → fetch the result
# def main():
#     if HOURS < 1:
#         raise ValueError('BEDROCK_REPORT_HOURS must be >= 1')
#     session = boto3.Session(region_name=REGION) # Connecting sessions with AWS
#     sts_identity = session.client('sts').get_caller_identity()
#     if sts_identity['Account'] != '817977002522':
#         raise RuntimeError('Wrong AWS account! Refusing to query logs.')
#     logs = session.client('logs') # storing tthe cloudwatch logs client in the logs variable
#     end = datetime.now(timezone.utc)
#     start = end - timedelta(hours=HOURS)
#     query = QUERY.replace("__IAM_ARN__", IAM_ARN)
#     response = logs.start_query( # CloudWatch Logs Insights API call
#         logGroupName=LOG_GROUP,
#         startTime=int(start.timestamp()),
#         endTime=int(end.timestamp()),
#         queryString=query,
#         limit=10000,
#     )
#     query_id = response['queryId']
#     for _ in range(60):
#         result = logs.get_query_results(queryId=query_id)
#         status = result['status']
#         if status == 'Complete':
#             break
#         if status in ('Failed', 'Cancelled', 'Timeout', 'Unknown'):
#             raise RuntimeError(f'Logs Insights query ended: {status}')
#         time.sleep(2)
#     else:
#         raise TimeoutError('Logs Insights query did not finish in 120 seconds')

#     rows = rows_to_dicts(result.get('results', []))
#     print('\n========== BEDROCK USER CONSUMPTION =========')
#     print(f'IAM User       : {IAM_ARN}')
#     print(f'Region         : {REGION}')
#     print(f'Time Range     : Last {HOURS} hours')
#     print(f'Log Group      : {LOG_GROUP}')
#     print('---------------------------------------------')
#     if not rows:
#         print('No matching invocation logs found.')
#         print('Check logging, region, IAM ARN and time range.')
#     total_requests = total_input = total_output = 0
#     for row in rows:
#         requests = int(float(row.get('requests') or 0))
#         input_tokens = int(float(row.get('inputTokens') or 0))
#         output_tokens = int(float(row.get('outputTokens') or 0))
#         total_requests += requests
#         total_input += input_tokens
#         total_output += output_tokens
#         print(f"Model ID       : {row.get('modelId', 'Unknown')}")
#         print(f'Requests       : {requests:,}')
#         print(f'Input Tokens   : {input_tokens:,}')
#         print(f'Output Tokens  : {output_tokens:,}')
#         print('---------------------------------------------')
#     print(f'Total Requests : {total_requests:,}')
#     print(f'Input Tokens   : {total_input:,}')
#     print(f'Output Tokens  : {total_output:,}')
#     print(f'Total Tokens   : {total_input + total_output:,}')
#     print('=============================================')
#     if len(rows) >= 10000:
#         print('WARNING: Query result limit reached; totals may be incomplete.')
#     print('Note: Counts represent matching logged invocations, not necessarily all attempts.')


# if __name__ == '__main__':
#     try:
#         main()
#     except (BotoCoreError, ClientError, ProfileNotFound, ValueError, RuntimeError, TimeoutError) as exc:
#         print(f'ERROR: {exc}', file=sys.stderr)
#         sys.exit(1)




import os
import sys
import time
import re
from datetime import datetime, timedelta, timezone

import boto3
from botocore.exceptions import BotoCoreError, ClientError, ProfileNotFound

REGION = os.getenv("AWS_REGION", "us-east-1")
LOG_GROUP = os.getenv(
    "BEDROCK_LOG_GROUP",
    "/aws/bedrock/model-invocations-poc"
)

ACCOUNT_ID = "817977002522"
HOURS = 24

QUERY = """
fields identity.arn as iamUser,
       modelId,
       input.inputTokenCount as inputTokenValue,
       output.outputTokenCount as outputTokenValue
| filter identity.arn = "__IAM_ARN__"
| stats count(*) as requests,
        sum(inputTokenValue) as inputTokens,
        sum(outputTokenValue) as outputTokens
  by iamUser, modelId
| sort requests desc
"""


def rows_to_dicts(rows):
    return [
        {
            cell["field"]: cell.get("value", "")
            for cell in row
        }
        for row in rows
    ]


# Reusable function: pass an IAM username or full IAM ARN
def get_user_consumption(user_id, hours=HOURS):

    if not 1 <= hours <= 2160:
        raise ValueError("Hours must be between 1 and 2160")

    # Convert username to IAM ARN
    if user_id.startswith("arn:aws:iam::"):
        iam_arn = user_id
    else:
        if not re.fullmatch(r"[A-Za-z0-9_+=,.@-]+", user_id):
            raise ValueError("Invalid IAM username")
        iam_arn = f"arn:aws:iam::{ACCOUNT_ID}:user/{user_id}"

    # Validate ARN and account
    expected_prefix = f"arn:aws:iam::{ACCOUNT_ID}:user/"
    if not iam_arn.startswith(expected_prefix):
        raise ValueError("IAM ARN must belong to the expected account")

    session = boto3.Session(region_name=REGION)

    sts_identity = session.client("sts").get_caller_identity()

    if sts_identity["Account"] != ACCOUNT_ID:
        raise RuntimeError("Wrong AWS account!")

    logs = session.client("logs")

    end = datetime.now(timezone.utc)
    start = end - timedelta(hours=hours)

    query = QUERY.replace("__IAM_ARN__", iam_arn)

    # Start CloudWatch Logs Insights query
    response = logs.start_query(
        logGroupName=LOG_GROUP,
        startTime=int(start.timestamp()),
        endTime=int(end.timestamp()),
        queryString=query,
        limit=10000
    )

    query_id = response["queryId"]

    # Wait for query completion
    for _ in range(60):

        result = logs.get_query_results(queryId=query_id)

        status = result["status"]

        if status == "Complete":
            break

        if status in ("Failed", "Cancelled", "Timeout", "Unknown"):
            raise RuntimeError(f"Query failed: {status}")

        time.sleep(2)

    else:
        raise TimeoutError("Query did not finish within 120 seconds")

    rows = rows_to_dicts(result.get("results", []))

    total_requests = 0
    total_input = 0
    total_output = 0
    models = []

    print("\n========== BEDROCK USER CONSUMPTION =========")
    print(f"IAM User       : {iam_arn}")
    print(f"Region         : {REGION}")
    print(f"Time Range     : Last {hours} hours")
    print("---------------------------------------------")

    if not rows:
        print("No matching invocation logs found.")

    for row in rows:

        model_id = row.get("modelId", "Unknown")

        requests = int(float(row.get("requests") or 0))
        input_tokens = int(float(row.get("inputTokens") or 0))
        output_tokens = int(float(row.get("outputTokens") or 0))

        total_requests += requests
        total_input += input_tokens
        total_output += output_tokens

        models.append({
            "model_id": model_id,
            "requests": requests,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens
        })

        print(f"Model ID       : {model_id}")
        print(f"Requests       : {requests:,}")
        print(f"Input Tokens   : {input_tokens:,}")
        print(f"Output Tokens  : {output_tokens:,}")
        print("---------------------------------------------")

    print(f"Total Requests : {total_requests:,}")
    print(f"Input Tokens   : {total_input:,}")
    print(f"Output Tokens  : {total_output:,}")
    print(f"Total Tokens   : {total_input + total_output:,}")
    print("=============================================")

    if len(rows) >= 10000:
        print("WARNING: Query result limit reached.")

    # Return results for further processing
    return {
        "iam_user": iam_arn,
        "models": models,
        "total_requests": total_requests,
        "total_input_tokens": total_input,
        "total_output_tokens": total_output,
        "total_tokens": total_input + total_output
    }


if __name__ == "__main__":
    try:
        # Change the username here
        report = get_user_consumption("Tanisha")

    except (
        BotoCoreError,
        ClientError,
        ProfileNotFound,
        ValueError,
        RuntimeError,
        TimeoutError
    ) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
