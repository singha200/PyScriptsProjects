#Script contains unit test for ec2 insatnce creation script a_ec2.py
# Author: singha200
from unittest import mock
from a_ec2 import Get_Image, Start_Ec2
import boto3

class MockResponse:
  '''
  Class to mock urllib3 response
  '''
  def __init__(self, status_code, body):
    self.status_code = status_code
    self.body = body

  def __iter__(self) -> any:
    '''
    Need to implement iterable in order to be representable
    '''
    for value in [self, self.body]:
      yield value

class TestEc2:
  @mock.patch('botocore.client.BaseClient._make_request')
  def test_get_image(self, mock_api):
    '''
    Test the Get Image function
    '''
    mock_api.return_value = MockResponse(
      200,
      {
    'Images': [
        {
            'Architecture': 'i386',
            'CreationDate': 'string',
            'ImageId': 'string',
            'ImageLocation': 'string',
            'ImageType': 'machine',
            'Public': True,
            'KernelId': 'string',
            'OwnerId': 'string',
            'Platform': 'Windows',
            'PlatformDetails': 'string',
            'UsageOperation': 'string',
            'ProductCodes': [
                {
                    'ProductCodeId': 'string',
                    'ProductCodeType': 'devpay'
                },
            ],
            'RamdiskId': 'string',
            'State': 'available',
            'BlockDeviceMappings': [
                {
                    'DeviceName': 'string',
                    'VirtualName': 'string',
                    'Ebs': {
                        'DeleteOnTermination': True,
                        'Iops': 123,
                        'SnapshotId': 'string',
                        'VolumeSize': 123,
                        'VolumeType': 'standard',
                        'KmsKeyId': 'string',
                        'Encrypted': True
                    },
                    'NoDevice': 'string'
                },
            ],
            'Description': 'string',
            'EnaSupport': True,
            'Hypervisor': 'ovm',
            'ImageOwnerAlias': 'string',
            'Name': 'string',
            'RootDeviceName': 'string',
            'RootDeviceType': 'ebs',
            'SriovNetSupport': 'string',
            'StateReason': {
                'Code': 'string',
                'Message': 'string'
            },
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'VirtualizationType': 'hvm'
        },
    ]
}
    )
    ec2_client = boto3.client('ec2')
    assert Get_Image(ec2_client)