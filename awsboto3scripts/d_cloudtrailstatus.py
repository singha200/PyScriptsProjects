#script to enforce cloudTrail(boto3)
'''
Use case when people hack aws account then the first thing they do is to stop cloudtrail
We can use this to check if cloudtrail is enabled or not
'''
#Author: singha200
import boto3

def Stop_Logging(name):
  cloudtrail_client = boto3.client('cloudtrail')
  response = cloudtrail_client.stop_logging(
      Name=name
  )
  print(response)
  return True

def Start_Logging(name):
  cloudtrail_client = boto3.client('cloudtrail')
  response = cloudtrail_client.start_logging(
      Name=name
  )
  print(response)
  return True

def Get_Cloudtrail_Status(name):
  cloudtrail_client = boto3.client('cloudtrail')
  try:
    response = cloudtrail_client.get_trail_status(
      Name=name
    )
  except cloudtrail_client.exceptions.TrailNotFoundException:
    raise NameError("That cloudtrail was not found")

  return response.get('IsLogging')

if __name__ == "__main__":
  Name = 'cloudtrail'
  # Stop_Logging(Name)
  if not Get_Cloudtrail_Status(Name):
    Start_Logging(Name)
  else:
    print("Logging already enabled")