import boto3
from pprint import pprint

'''Creating a route table  using Client Object inside an existing VPC'''
session = boto3.session.Session(profile_name="ec2-dev")
ec2_cli = session.client(service_name="ec2", region_name="us-east-2")
# existing_vpc = 'vpc-0cdcd3ba5b2f888c9'
# New_RT = ec2_cli.create_route_table(VpcId=existing_vpc)
# print("the new route table has been created successfully")
# pprint(New_RT)

'''list the existing route tables details'''
# existing_RTs = ec2_cli.describe_route_tables()['RouteTables']
# # pprint(existing_RTs)
# for route_table in existing_RTs:
#     print(route_table['RouteTableId'], route_table['VpcId'])

'''delete an existing route table'''
RT_to_delete = 'rtb-01ec172cb255ef7b7'
deleted_RT = ec2_cli.delete_route_table(RouteTableId=RT_to_delete)
print(f"Route Table :{RT_to_delete} has been deleted successfully")
print(deleted_RT)
