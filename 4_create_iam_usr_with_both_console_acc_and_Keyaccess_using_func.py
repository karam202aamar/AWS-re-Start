import boto3
from random import choice
import sys


def get_usr():
    aws_session = boto3.session.Session(profile_name="iam-dev")
    iam_con_cli = aws_session.client('iam')
    return iam_con_cli


def random_pass():
    random_chars = "asdfghjklmnbvcxzqwertyuioASDFGHJKLMNBVCXZQWERTYUIO1234567890-=][\\';.?/"
    len_of_pass = 8
    return "".join(choice(random_chars) for char in range(len_of_pass))


def main():
    usr_client = get_usr()
    username = "s3-dev"
    password = random_pass()
    try:
        usr_client.create_user(UserName=username)
        usr_client.create_login_profile(
            UserName=username,
            Password=password,
            PasswordResetRequired=False)
        usr_access_key = usr_client.create_access_key(UserName=username)
        usr_client.attach_user_policy(
            UserName=username,
            PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess')
        print(f"successfully created username :{username} with Password:{password}")
        print(
            f"successfully created username :{username} with Access-key_ID:{usr_access_key['AccessKey']['AccessKeyId']} with Secret_Key: {usr_access_key['AccessKey']['SecretAccessKey']}")
    except Exception as e:
        print(e.response)
        # if e.response["Error"]['Code'] == 'EntityAlreadyExists':
        #     print(f"the same username {username} is already created, please try another username")
        #     sys.exit(1)
        # else:
        #     print("please try to fix that error and re-run the script again")
        #     print(e)
        #     sys.exit(1)


if __name__ == '__main__':
    main()
