# How would you use Boto3 to retrieve a list of all stopped EC2 instances?

import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances(
    Filters=[  # AWS provides a Filters parameter that allows us to retrieve only instances matching particular conditions.
        {
                'Name': 'instance-state-name',
                'Values': ['stopped']

        }
    ]
)

for reservation in response['Reservations']:
    for instance in reservation['Instances']:   
        print(instance['InstanceId'])

print(response)


# # basic syntax for describe_instanceresponse = ec2.describe_instances(
# response = ec2.describe_instances(
#     InstanceIds=[
#         'instance-id-1',
#         'instance-id-2'
#     ],
#     Filters=[
#         {
#             'Name': 'filter-name',
#             'Values': ['value1', 'value2']
#         }
#     ],
#     MaxResults=1000
# )