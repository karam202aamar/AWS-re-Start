import boto3


''' A- first create the AWS Session'''
aws_session = boto3.session.Session(profile_name="iam-dev", region_name='us-east-2')
iam_con_cli = aws_session.client(service_name='iam', region_name='us-east-2')

''' B- create the user IAM -create user'''
username = 'dolfined1234'
iam_con_cli.create_user(UserName=username)

usr_access_key = iam_con_cli.create_access_key(UserName=username)
''' C- Create user policy or for simplicity attach existing policy'''
iam_con_cli.attach_user_policy(UserName=username,PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess')
Programmatic_Access_key = usr_access_key['AccessKey']['AccessKeyId']
Secret_key = usr_access_key['AccessKey']['SecretAccessKey']
print(f"successfully created username :{username}"
      f" with Access-key_ID:{Programmatic_Access_key} "
      f"with Secret_Key: {Secret_key}")
