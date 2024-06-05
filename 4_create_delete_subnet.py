import boto3
from pprint import pprint
import sys

'''Creating a subnet using Client Object inside an existing VPC'''
session = boto3.session.Session(profile_name="ec2-dev")
ec2_cli = session.client(service_name="ec2", region_name="us-east-2")
# existing_vpc = 'vpc-0cdcd3ba5b2f888c9'
# new_subnet = ec2_cli.create_subnet(CidrBlock='10.2.0.0/24', VpcId=existing_vpc)
# print("the new subnet has been created successfully")
# pprint(new_subnet)

'''list the existing subnet details'''
# existing_subnets = ec2_cli.describe_subnets()['Subnets']
# # pprint(existing_subnets)
# for subnet in existing_subnets:
#     print(subnet['AvailabilityZone'], subnet['CidrBlock'], subnet['SubnetId'], subnet['VpcId'])
#     print("#"* 50)

'''delete an existing subnet'''
subnet_to_delete = 'subnet-021a1d9906755d758'
deleted_subnet = ec2_cli.delete_subnet(SubnetId=subnet_to_delete)
print(f"Subnet:{subnet_to_delete} has been deleted successfully")
print(deleted_subnet)
