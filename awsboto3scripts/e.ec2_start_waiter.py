"""Boto script to start and confirm ec2 status using waiter"""
import boto3 
import time
aws_con=boto3.session.Session(profile_name="ec2_developer")
ec2_con_re=aws_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_con.client(service_name="ec2",region_name="us-east-1")
my_inst_ob=ec2_con_re.Instance("i-002d4110f1199166f")
print("Starting given instance....")
my_inst_ob.start()
waiter=ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=['i-002d4110f1199166f'])
print("Now your ec2 instace is up and running")
