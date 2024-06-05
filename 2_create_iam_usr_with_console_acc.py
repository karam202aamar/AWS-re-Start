import boto3
from random import choice

''' A- first create the AWS Session'''
aws_session = boto3.session.Session(profile_name="iam-dev", region_name='us-east-2')
iam_con_cli = aws_session.client(service_name='iam', region_name='us-east-2')
username = 'test123'
''' B- create the user IAM -create user'''
iam_con_cli.create_user(UserName=username)

''' C- create login profile'''
random_chars = "asdfghjklmnbvcxzqwertyuioASDFGHJKLMNBVCXZQWERTYUIO1234567890-=][\\';.?/"
random_pass = []
len_of_pass = 8
for char in range(len_of_pass):
    random_pass.append(choice(random_chars))
password = "".join(random_pass)
# password = "".join(choice(random_chars) for char in range(len_of_pass)) # shortest way
iam_con_cli.create_login_profile(
    UserName=username,
    Password=password,
    PasswordResetRequired=False)
''' D- Create user policy or for simplicity attach existing policy'''
iam_con_cli.attach_user_policy(
    UserName=username,
    PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess')
print(f"successfully creating new user with username: {username} and password :{password}")
