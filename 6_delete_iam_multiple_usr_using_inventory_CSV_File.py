import boto3
from random import choice
import sys
import csv


def get_usr():
    aws_session = boto3.session.Session(profile_name="iam-dev")
    iam_con_cli = aws_session.client(service_name='iam')
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
            usr_client.detach_user_policy(UserName=username, PolicyArn=PolicyArn)
            usr_client.delete_user(UserName=username)

        except Exception as e:
            print(e)

    print('all users are deleted successfully')


if __name__ == '__main__':
    main()
