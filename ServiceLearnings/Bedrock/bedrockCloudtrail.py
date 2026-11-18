# filtering data for all the users in the account

import boto3
import json
from collections import defaultdict
from datetime import datetime, timedelta, timezone

REGION = "us-east-1"
HOURS = 24

API_NAMES = [
    "Converse",
    "ConverseStream",
    "InvokeModel",
    "InvokeModelWithResponseStream"
]

session = boto3.Session(region_name=REGION) 
cloudtrail = session.client("cloudtrail")

end_time = datetime.now(timezone.utc)
start_time = end_time - timedelta(hours=HOURS)

# Store requests by IAM identity and model
user_model_requests = defaultdict(int)

for api_name in API_NAMES:

    paginator = cloudtrail.get_paginator("lookup_events")

    pages = paginator.paginate(
        LookupAttributes=[
            {
                "AttributeKey": "EventName",
                "AttributeValue": api_name
            }
        ],
        StartTime=start_time,
        EndTime=end_time
    )

    for page in pages:
        for event in page.get("Events", []):

            record = json.loads(event["CloudTrailEvent"])

            # Only API call events
            if record.get("eventType") != "AwsApiCall":
                continue

            # Only Bedrock events
            if record.get("eventSource") not in (
                "bedrock.amazonaws.com",
                "bedrock-runtime.amazonaws.com"
            ):
                continue

            # Identify the AWS user or role
            user_arn = (
                record.get("userIdentity") or {}
            ).get("arn") or "Unknown"

            # Identify the Bedrock model
            model_id = (
                record.get("requestParameters") or {}
            ).get("modelId") or "Unknown"

            # Count requests user-wise and model-wise
            user_model_requests[(user_arn, model_id)] += 1


print("\n========== BEDROCK CLOUDTRAIL REPORT =========")
print(f"Region     : {REGION}")
print(f"Time Range : Last {HOURS} hours")
print("----------------------------------------------")

total_requests = 0

if not user_model_requests:
    print("No matching Bedrock API events found.")

for (user_arn, model_id), requests in sorted(
    user_model_requests.items()
):
    print(f"IAM Identity : {user_arn}")
    print(f"Model ID     : {model_id}")
    print(f"API Requests : {requests}")
    print("----------------------------------------------")

    total_requests += requests

print(f"Total Requests : {total_requests}")
print("==============================================")