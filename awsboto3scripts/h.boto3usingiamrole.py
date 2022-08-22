import boto3
ec2_con=boto3.resource(service_name="ec2",region_name="us-east-1")
for each_instance in ec2_con.instances.all():
  print(each_instance.id, each_instance.state)
