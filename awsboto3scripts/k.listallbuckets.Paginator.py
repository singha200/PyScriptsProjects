import boto3
s3_cli=session.client(service_name="s3", region_name="us-east-1")
paginator = s3_cli.get_paginator('list_object')
print(paginator.paginate(Bucket=bucket_name)) #Print the object 
for each_page in paginator.paginate(Bucket=bucket_name): #loop through each page 
  for each_object in each_page: #loop through each object 
    print(cnt, each_object['key'])
    cnt=cnt+1
