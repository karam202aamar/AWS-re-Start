import boto3
from pprint import pprint
aws_session = boto3.session.Session(profile_name="iam-dev")
iam_con_re = aws_session.resource(service_name='iam')
''' listing all IAM groups in my account using resource object'''
# for group in iam_con_re.groups.all():
#     print(group.name)

''' listing all IAM groups in my account using client object'''
iam_con_cli = aws_session.client(service_name='iam', region_name='us-east-2')
response = iam_con_cli.list_groups()
pprint(response)
