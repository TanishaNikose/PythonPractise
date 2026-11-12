# import boto3 

# # using client()
# s3 = boto3.client('s3', region_name='us-east-1')   # creates a client that that will connect to AWS resource, but does not sent the API request. and If you omit region_name, Boto3 looks for a region in your configured AWS environment.
# response = s3.list_buckets() # calling the API here using listing buckets.
# print(response)

# # some general client() methods
# Suppose you have 5,000 objects in an S3 bucket.
# But the API returns only a limited number of objects per response.
# How do you retrieve all of them?
# You use a paginator.

# # get_paginator()

# import boto3
# s3 = boto3.client('s3', region_name='us-east-1')
# paginator = s3.get_paginator('list_objects_v2') # list_objects_v2 name of the AWS S3 API operation used to list the files (objects) inside an S3 bucket.

# pages = paginator.paginate(
#     Bucket='bio-rhyme-development'
# )

# for page in pages:
#     print(page.get('Contents', []))



#paginator = s3.get_paginator('list_objects_v2') (Setup): Builds and configures a reusable paginator object in memory that knows how to handle S3's pagination tokens (ContinuationToken). 
# No API call is sent to AWS here.

# pages = paginator.paginate(...) (Execution / Generator): Actually prepares the API requests with your specific parameters (like which bucket to look in) and returns a lazy iterator (PageIterator).
#  As your for loop steps through pages, boto3 automatically fetches one batch (up to 1,000 objects per page) from AWS at a time until every object in the bucket has been retrieved.

# # Does paginate() take the Bucket name as a parameter?
# Yes. paginate() accepts the exact same parameters that s3.list_objects_v2() normally accepts (such as Bucket, Prefix, or MaxKeys), 
# plus an optional PaginationConfig dictionary if you want to cap total items or page sizes.

# # 4. What is page.get('Contents', []) doing?
# Each page returned in the loop is a standard Python dictionary representing one API response from AWS.

# 'Contents': When a bucket has files, AWS puts the list of file dictionaries (containing Key, Size, LastModified, etc.) 
# under the key 'Contents'.

# Why .get('Contents', []) instead of page['Contents']? If the S3 bucket is completely empty,
# AWS omits the 'Contents' key from the response dictionary altogether. Writing page['Contents'] on an empty bucket would crash your script with a KeyError.

# [] (Default Fallback): Passing [] as the second argument tells Python: "Look for the 'Contents' key; if it exists,"
# " return the list of files—if it doesn't exist (because the bucket is empty), safely return an empty list [] instead of crashing."


# # get_waiter()

# Suppose you launch an EC2 instance.
# You want your Python script to wait until that instance is running.

# import boto3
# ec2 = boto3.client('ec2')
# waiter = ec2.get_waiter('instace_running')

# waiter.wait( # wait() pauses your Python script and repeatedly polls AWS in the background until the EC2 instance reaches the running state.
#     InstanceIds=['i-1234567890abcdef0']
# )
# print("Instance is running")


# # syntax for wait()
# waiter.wait(
#     Filters=[
#         {
#             'Name': 'string',
#             'Values': [
#                 'string',
#             ]
#         },
#     ],
#     InstanceIds=[
#         'string',
#     ],
#     DryRun=True | False,
#     MaxResults=123,
#     NextToken='string',
#     WaiterConfig={
#         'Delay': 15,
#         'MaxAttempts': 40
#     }
# )

# # can_paginate() - Before creating a paginator, you can check whether an operation supports pagination.

# import boto3
# s3 = boto3.client('s3')
# result = s3.can_paginate('list_objects_v2') # 'list_objects_v2' is the exact string name of the AWS S3 API operation used to list the files (objects) inside an S3 bucket.
# print(result) # it gives true or false



# # AWS specific methods


# import boto3
# # using resource()
# s3 = boto3.resource('s3') # directly calling AWS API operation - list_buckets()
# print(s3)
# for buckets in s3.buckets.all():
#     print(buckets.name)

# # It retrieves all S3 buckets in your account and returns an iterable collection of bucket resource objects.

# # In simple terms:
# # - s3.buckets → represents the collection of S3 buckets.
# # - .all() → lets you iterate through all the buckets in that collection.
# # - Each item → represents one individual S3 bucket.


# ec2 = boto3.client('ec2')
# iam = boto3.client('iam')


# cloudtrail = boto3.client('cloudtrail')
# response  = cloudtrail.lookup_events() # makes the API request    
# print(response)




# question :
# s3.buckets.all() -- what it is doing ?