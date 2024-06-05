import boto3

''' 1-Get AWS Management Console'''

aws_mag_console = boto3.session.Session(profile_name="iam-dev")

''' 2-Get IAM Console resource object'''
iam_console_re = aws_mag_console.resource('iam')
# print(dir(iam_console_re))

''' 3-get users from resource object'''
for user in iam_console_re.users.all():
    print(user.name)
# print('################################')

''' Or Get IAM Console client object'''
# iam_console_cli = aws_mag_console.client('iam')

''' get users from client object'''
# for user in iam_console_cli.list_users()['Users']:
#     print(user['UserName'])
