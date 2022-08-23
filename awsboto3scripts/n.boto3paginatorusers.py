import sys
import boto3
iam = boto3.client("iam")
marker = None
while True:
    paginator = iam.get_paginator('list_users')
    response_iterator = paginator.paginate( 
        PaginationConfig={
            'PageSize': 10,
            'StartingToken': marker})
    for page in response_iterator:
        print("Next Page : {} ".format(page['IsTruncated']))
        u = page['Users']
        for user in u:
            print(user['UserName'])
    try:
        marker = response_iterator['Marker']
        print(marker)
    except KeyError:
        sys.exit()
