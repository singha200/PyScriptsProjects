import json
import boto3
import sys
def lambda_handler(event, context):
    master_id="XXXXXXXXXXXXXXXXXXX"
    slave_id="YYYYYYYYYYYYYYYYYYY"
    ec2_re=boto3.resource("ec2","us-east-1")
    primary_instance=ec2_re.Instance(master_id)
    if primary_instance.state['Name'] == "running":
        print("Master is running. so no modifications")
    else:
        secondary_instance=ec2_re.Instance(slave_id)
        pnetwork_interface_Info=primary_instance.network_interfaces_attribute[0]
        snetwork_interface_Info=secondary_instance.network_interfaces_attribute[0]
        pnw_interface_id=pnetwork_interface_Info['NetworkInterfaceId']
        snw_interface_id=snetwork_interface_Info['NetworkInterfaceId']
        secondary_ip="xxx.xx.xx.xxx"
        ec2_cli=boto3.client("ec2","us-east-1") 
    
        ec2_cli.unassign_private_ip_addresses(
                NetworkInterfaceId=pnw_interface_id,
                PrivateIpAddresses=[secondary_ip]
                )
    
        ec2_cli.assign_private_ip_addresses(
            AllowReassignment=True,
            NetworkInterfaceId=snw_interface_id,
            PrivateIpAddresses=[secondary_ip]
            )
    return None
