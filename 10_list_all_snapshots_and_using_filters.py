import boto3

aws_session = boto3.session.Session(profile_name='ec2-dev')
ec2_con_re = aws_session.resource(service_name='ec2', region_name='us-east-2')

'''printing all Publicly shared snapshots in that Region'''
# for snapshot in ec2_con_re.snapshots.all():
#     print(snapshot)

'''printing only my Snapshots using Filters
first we will get my own account ID using the below script '''
sts_con_cli = aws_session.client(service_name="sts", region_name="us-east-2")
response = sts_con_cli.get_caller_identity()
# print(response)
my_acount_id = response['Account']

'''
List snapshots without my own ID filter will list all available snapshots in that selected
region either owned by me or others
'''
for snapshot in ec2_con_re.snapshots.filter(OwnerIds=[my_acount_id]):
    print(snapshot.id)
print('#' * 50)

'''adding more filter based on Size as an example'''
# size_filter = {"Name": "volume-size", "Values": ["8"]}
# for snapshot in ec2_con_re.snapshots.filter(OwnerIds=[my_own_id], Filters=[size_filter]):
#     print(snapshot.id)

'''list all snapshots based on creating or starting time'''
for snapshot in ec2_con_re.snapshots.filter(OwnerIds=[my_acount_id]):
    print(snapshot.id, snapshot.start_time.strftime("%Y:%M:%D %H:%M:%S"))
