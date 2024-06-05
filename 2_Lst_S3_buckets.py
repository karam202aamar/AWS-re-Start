import boto3

''' first we will create a number of new S3 Buckets'''
session = boto3.session.Session(profile_name='s3-dev')
S3_cli = session.client(service_name='s3', region_name='us-east-2')
bucket_list=['dolfined1265434','dolfined4576678','dolfined78954']
bucket_locations=[]
for bucket in bucket_list:
    result=S3_cli.create_bucket(ACL='public-read',
        Bucket=bucket,
        CreateBucketConfiguration={
            'LocationConstraint': 'us-east-2'})
    bucket_locations.append(result['Location'])
# print(bucket_locations)

'''second list the buckets using the resource Object'''
s3_re = session.resource(service_name='s3', region_name='us-east-2')
for bucket in s3_re.buckets.all():
    print(bucket.name)


'''we can list buckets also using client object'''
print("#########################################")
for bucket in S3_cli.list_buckets()['Buckets']:
    print(bucket.get('Name'))
