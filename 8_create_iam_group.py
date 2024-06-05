""" this Script is to Create  a new IAM Group , Attach policy to it and add existing IAM user to an IAM group"""
import boto3
from pprint import pprint

aws_session = boto3.session.Session(profile_name="iam-dev")

''' creating IAM group using client object'''
group_name = 'testgroup'
iam_con_cli = aws_session.client(service_name='iam')
new_group = iam_con_cli.create_group(GroupName=group_name)
pprint(new_group)

''' attach policy to the group'''
policy_attach = iam_con_cli.attach_group_policy(GroupName=group_name,
                                                PolicyArn='arn:aws:iam::aws:policy/ReadOnlyAccess')

''' add user to the new group'''
existing_usr = 's3-dev'
user_to_group = iam_con_cli.add_user_to_group(GroupName=group_name, UserName=existing_usr)
