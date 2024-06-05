import boto3
from random import choice
import sys
import csv

'''
in this example , we will get users attribute details from CSV file and then create those users using  details
extracted from the CSV file.
'''


def get_usr():
    aws_session = boto3.session.Session(profile_name="iam-dev", region_name='us-east-2')
    iam_con_cli = aws_session.client(service_name='iam', region_name='us-east-2')
    return iam_con_cli


def reading_inv(txt):
    with open(txt, "r") as f:
        file = csv.DictReader(f)
        users_details = list(file)
        return users_details


def main():
    usr_client = get_usr()
    usr_details = reading_inv("IAM_168_users_inventory.csv")
    for usr in usr_details:
        username = usr['IAM_User_Name']
        PolicyArn = usr['PolicyARN']

        try:
            usr_client.create_user(UserName=username)
            usr_client.attach_user_policy(
                UserName=username,
                PolicyArn=PolicyArn)

        except Exception as e:
            if e.response["Error"]['Code'] == 'EntityAlreadyExists':
                print(f"the same username {username} is already created, please try another username")
                sys.exit(1)
            else:
                print("please try to fix that error and re-run the script again")
                print(e)
                sys.exit(1)

    print('all users are created successfully')


if __name__ == '__main__':
    main()
