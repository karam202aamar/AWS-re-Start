import boto3
import time

aws_session = boto3.session.Session(profile_name="ec2-dev")
ec2_service_re = aws_session.resource(service_name='ec2', region_name='us-east-2')
ec2_service_cli = aws_session.client(service_name='ec2', region_name='us-east-2')
'''collecting all available instances using service resource object'''
all_instances = []
for instance in ec2_service_re.instances.all():
    all_instances.append(instance.id)
# print(all_instances)
'''stopping all instances in my AWS account'''
# waiter = ec2_service_cli.get_waiter('instance_stopped')
# print("Stopping all instances ......")
# ec2_service_re.instances.stop()
# waiter.wait(InstanceIds=all_instances)
# print("All Instances are stopped now")

'''do some time delay to check the status of instances'''
# time.sleep(20)

'''collecting only selected instances'''
DB_instances = []
f1 = {'Name': 'tag:Name', 'Values': ['DB-Server']}
for instance in ec2_service_re.instances.filter(Filters=[f1]):
    DB_instances.append(instance.id)

'''starting /Terminating , stopping selected tag attribute instances'''
'''starting the selected instances'''
waiter = ec2_service_cli.get_waiter('instance_running')
print("Starting the Selected instance(s) ......")
ec2_service_cli.start_instances(InstanceIds=DB_instances)
waiter.wait(InstanceIds=DB_instances)
print("your selected Instance(s) are up and running")
