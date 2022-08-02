"""Script to demo meta object in boto to enter into client object from resource object
This script will list the available resion for EC2 Service"""
import boto3
aws_mag_con=boto3.session.Session(profile_name="root")
ec2_con_re=aws_mag_con.resource(service_name="ec2")

for each_item in ec2_con_re.meta.client.describe_regions()['Regions']:
	print(each_item['RegionName'])
