#Script contains three functions CreateBucket, DeleteBucket, EnforceS3Encryption on S3 bucket using boto3
# Author: singha200
import boto3
def CreateBucket(name):
  s3_client = boto3.client('s3')
  try:
    print(s3_client.create_bucket(Bucket=name))
    return True
  except s3_client.exceptions.BucketAlreadyExists:
    print(f"The bucket {name} already exists, choose another unique name")
    return False

def DeleteBucket(name):
  s3_client = boto3.client('s3')
  s3_client.delete_bucket(Bucket=name)
  return True

def EnforceS3Encryption(bucketName):
  s3 = boto3.resource('s3')
  s3_client = boto3.client('s3')
  bucket = s3.Bucket(bucketName)
  try: 
    s3_client.get_bucket_encryption(Bucket=bucket.name)
    print("Encryption already set")
  except s3_client.exceptions.ClientError as error:
    if 'ServerSideEncryptionConfigurationNotFoundError' in str(error):
      response = s3_client.put_bucket_encryption(
        Bucket=bucket.name, 
        ServerSideEncryptionConfiguration = {
          'Rules' : [
            {
              'ApplyServerSideEncryptionByDefault': {
                'SSEAlgorithm': 'AES256'
              }
            }
          ]
        }
      )
      print(response)
    else:
     raise error
  

  # try: 
  #   response = s3_client.get_bucket_encryption(Bucket=bucketName)
  #   print(response)

  # except s3_client.exceptions.ClientError as error:
  #   if 'ServerSideEncryptionConfigurationNotFoundError' in error:
      
  #   else:
  #    raise error

if __name__ == "__main__":
  Name = 'testbucketwithaes256'
  if CreateBucket(Name):
     EnforceS3Encryption(Name)
  else:
     pass
    #DeleteBucket(Name) # uncomment this line to delete the bucket