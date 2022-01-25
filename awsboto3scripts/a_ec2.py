#Script contains two functions: Get_Image and Start_Ec2 to create an ec2 instance using boto3
# Author: singha200
import boto3

#To create the instance set DRY_RUN to False
DRYRUN = False
 #Use aws ec2 to create a new instance
import boto3

DRYRUN = False

def Get_Image(ec2_client):
  images = ec2_client.describe_images(
    Filters=[
      {
        'Name': 'name',
        'Values': [
          'amzn2-ami-hvm*',
        ]
      },
      {
        'Name': 'owner-alias',
        'Values': [
          'amazon',
        ]
      },
    ],
  )
  ec2_image = boto3.resource('ec2')
  AMI = ec2_image.Image(images['Images'][0]['ImageId'])
  return AMI

def Start_Ec2(AMI, ec2_client):
  if AMI.state == 'available':
    print(AMI.image_id)
    instance = ec2_client.run_instances(
      ImageId=AMI.image_id,
      InstanceType='t2.micro',
      MaxCount=1,
      MinCount=1,
      DryRun=DRYRUN
    )
    ec2_instance = boto3.resource('ec2')
    ec2 = ec2_instance.Instance(instance['Instances'][0]['InstanceId'])
    return ec2
  else:
    print("The AMI was not available")
    return None

if __name__ == '__main__':
  ec2_client = boto3.client('ec2')
  AMI = Get_Image(ec2_client)
  ec2 = Start_Ec2(AMI=AMI, ec2_client=ec2_client)
  print(ec2.instance_id)
  ec2.wait_until_running()
  print(f"Instance is {ec2.state['Name']}")
  ec2.terminate()
  ec2.wait_until_terminated()
  print(f"Instance is {ec2.state['Name']}")