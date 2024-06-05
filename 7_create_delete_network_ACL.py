import boto3
from pprint import pprint

'''Creating a security Network ACL using Client Object for a specified VPC'''
session = boto3.session.Session(profile_name="ec2-dev")
ec2_cli = session.client(service_name="ec2", region_name="us-east-2")
# existing_vpc='vpc-0cdcd3ba5b2f888c9'
# new_network_ACL=ec2_cli.create_network_acl(VpcId=existing_vpc)
# print("the New Network ACL has been created successfully")
# pprint(new_network_ACL)


'''list the existing security Network ACLs'''
existing_network_ACLs = ec2_cli.describe_network_acls()['NetworkAcls']
# pprint(existing_network_ACLs)
# for NACL in existing_network_ACLs:
#     pprint(NACL)

# print(NACL['NetworkAclId'], NACL['VpcId'], NACL['OwnerId'])
# print("#" * 50)
# for value in NACL['Associations']:
#     print(value['NetworkAclAssociationId'], value['SubnetId'], value['NetworkAclId'])
#     print("#" * 50)

'''delete an existing Network ACL'''
NACL_to_delete = 'acl-036f12f5d5364733f'
deleted_NACL = ec2_cli.delete_network_acl(NetworkAclId=NACL_to_delete)
print(f"Network ACL :{NACL_to_delete} has been deleted successfully")
print(deleted_NACL)
