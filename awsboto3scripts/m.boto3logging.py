import boto3
import json 
import os
import logging

s3 = boto3.client('s3')
sns_client = boto3.client('sns')
logger = logging.getLogger('patientcheckout')
logger.setLevel(logging.INFO)
def lambda_handler(event, context):
    topic = os.environ.get('Patient_checkout_topic')
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    logger.info(f'Reading {file_key} from {bucket_name}')
    obj = s3.get.object(Bucket=bucket_name, key=file_key)
    file_content = obj['Body'].read().decode('utf-8')
    checkout_events = json.loads(file_content)
    for each_event in checkout_events:
        logger.info('Message being published')
        logger.info(each_event)
        sns_client.publish(
            TopicArn=topic,
            Message=json.dumps({'default':json.dumps(each_event)}),
            MessageStructure='json'
        )
