# # How would you write a Boto3 script to check whether a particular EC2 instance is running?
import boto3
ec2  = boto3.client('ec2')

instanceId = 'i-0123456789abcdef0' # example instance

# get instance detail
response = ec2.describe_instances(
    InstanceIds = [instanceId]
)

# check instance state
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        state = instance['State']['Name']

        if state == 'running':
            print(f"Ec2 Instance {instanceId} is running")
        else:
            print(f"Ec2 Instance {instanceId} is not running. Current State: {state} ")




# # response will be look like this, AWS returns instance details in a Python dictionary.
# response = {
#     'Reservations': [
#         {
#             'Instances': [
#                 {
#                     'InstanceId': 'i-0123456789abcdef0',
#                     'State': {
#                         'Name': 'running'
#                     }
#                 }
#             ]
#         }
#     ]
# }

# # things to notice
# Notice:
# - response is a dictionary.
# - Reservations is a list.
# - Each reservation is a dictionary.
# - Instances is another list.
# - Each instance is a dictionary.




