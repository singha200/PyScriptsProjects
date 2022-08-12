import boto3
aws_mag_con=boto3.session.Session(profile_name="root")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")
np_sers_ids=[]
f1={"Name": "tag:Name", "Values":['Non_Prod']}
for each_item in ec2_con_cli.describe_instances(Filters=[f1])['Reservations']:
	for each_in in each_item['Instances']:
		np_sers_ids.append(each_in['InstanceId'])
print(np_sers_ids)

print("Starting intances with ids of : ",np_sers_ids)
ec2_con_cli.start_instances(InstanceIds=np_sers_ids)
waiter=ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=np_sers_ids)
print("Your np instances are up and running....")
