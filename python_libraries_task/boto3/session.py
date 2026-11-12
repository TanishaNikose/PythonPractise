# import boto3
# session = boto3.Session() # boto3.Session() creates a session object.
# print(session)

# How do Session and Client work together?

import boto3
session = boto3.Session( 
    profile_name='default',
    region_name='us-east-1') # creates a session object that holds configuration information (like region, credentials, etc.) for your AWS interactions.

ec2 = session.client('ec2')
response = ec2.describe_instance()
print(response)


# boto3.client() - When you call boto3.client(), Boto3 uses its default session behind the scenes to create the client.