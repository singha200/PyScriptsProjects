"""Script to get all the IAM users in an AWS accouy="""
import boto3
aws_mag_con = boto3.session.Session(profile_name="cloud_user")
iam_con = aws_mag_con.resource('iam')
for each_user in iam_con.users.all():
    print(each_user.name)

iam_con_cli = aws_mag_con.client(service_name="iam", region_name="us-east-1")
response = iam_con_cli.list_users()
for each_item in response['Users']:
    print(each_item['UserName'])

