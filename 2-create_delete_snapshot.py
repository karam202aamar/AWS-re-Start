import boto3
from pprint import pprint

'''create a snapshot to an existing volume ID'''
session = boto3.session.Session(profile_name="ec2-dev")
ec2_cli = session.client(service_name="ec2", region_name="us-east-2")
ec2_volumeID = 'vol-0c474fbea4fde0913'
new_snapshot = ec2_cli.create_snapshot(
    Description='This is a snapshot to my Main EC2 instance',
    VolumeId=ec2_volumeID)
pprint(new_snapshot)

'''delete an existing Snapshot'''
# delete_snapshot = ec2_cli.delete_snapshot(SnapshotId='snap-0f4c8384156d3accc')
# print(delete_snapshot)
