import boto3
from pprint import pprint

'''Creating a security group using Client Object for a specified VPC'''
session = boto3.session.Session(profile_name="ec2-dev")
ec2_cli = session.client(service_name="ec2", region_name="us-east-2")
# existing_vpc = 'vpc-0cdcd3ba5b2f888c9'
# new_SG = ec2_cli.create_security_group(
#     Description='My security group',
#     GroupName='my-security-group',
#     VpcId=existing_vpc,
# )
# print("the new security group has been created successfully")
# pprint(new_SG)

'''list the existing security groups'''
existing_SGs = ec2_cli.describe_security_groups()['SecurityGroups']
# # pprint(existing_SGs)
# for SG in existing_SGs:
#     print(SG['GroupId'], SG['GroupName'], SG['VpcId'])
#     print("#"*50)

'''delete an existing security group'''
SG_to_delete = 'sg-05654789c188c1dbe'
deleted_SG = ec2_cli.delete_security_group(GroupId=SG_to_delete)
print(f"Security Group :{SG_to_delete} has been deleted successfully")
print("#"*50)
print(deleted_SG)
