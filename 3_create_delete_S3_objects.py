import boto3

aws_session = boto3.session.Session(profile_name="s3-dev")

'''using client object'''
s3_cli = aws_session.client(service_name='s3', region_name='us-east-2')
bucket_name = 'dolfinedbucket12345'

'''First create the bucket or use existing Bucket'''
# s3_cli.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})

''' Second upload an object without encryption'''
# s3_new_obj=s3_cli.put_object(Body='nice_image.jpeg',Bucket=bucket_name,Key='nice_image')
# print("Successfully uploaded the object image")
# print(s3_new_obj)

'''delete the object from existing BucketName'''
obj_del = s3_cli.delete_object(Bucket=bucket_name, Key='nice_image')
print("Successfully deleted the object image")
print(obj_del)
