import boto3
from pprint import pprint
''' using the Client Object'''
# c2_console = boto3.session.Session(profile_name="ec2-dev", region_name='us-east-2')
# ec2_client = c2_console.client(service_name='ec2', region_name='us-east-2')
# response = ec2_client.describe_instances()
# pprint(response)
# pprint(response['Reservations'])

# for result in response['Reservations']:
#     # pprint(result)
#     for result2 in result['Instances']:
#         # pprint(result2)
#         # break
#         print(f"the instance ID is {result2['InstanceId']} and the Subnet ID is {result2['SubnetId']}")
#         print("#"*50)

#####################################################################################
import boto3
''' using the resource object'''
session = boto3.session.Session(profile_name="ec2-dev")
ec2_res = session.resource(service_name='ec2', region_name='us-east-2')
instances = ec2_res.instances.all()
for instance in instances:
    print(dir(instance))
    # print(instance.private_ip_address)
