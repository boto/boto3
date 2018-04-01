import boto3
import json
import uuid
import unittest
from botocore.exceptions import ClientError
from botocore.stub import Stubber
import datetime

def mock_endpoints(region='us-east-1', endpoint_services=['s3', 's3', 's3', 'dynamodb', 'elb']):
    endpoints = []
    for service in endpoint_services:
        endpoints.append({
            'VpcEndpointId': 'vpce-{}'.format(str(uuid.uuid4())[0:8]),
            'VpcEndpointType': 'Gateway',  # Interface
            'VpcId': 'vpc-{}'.format(str(uuid.uuid4())[0:8]),
            'ServiceName': 'com.amazonaws.{}.{}'.format(region, service),
            'State': 'Available',
            'PolicyDocument': json.dumps({
                'Version': '2008-10-17',
                'Statement': [
                    {
                        'Effect': 'Allow',
                        'Principal': '*',
                        'Action': '*',
                        'Resource': '*'
                    }
                ]}),
            'RouteTableIds': [
                'rtb-{}'.format(str(uuid.uuid4())[0:8])
            ],
            'SubnetIds': [],
            'Groups': [
                {
                    'GroupId': 'string',
                    'GroupName': 'string'
                }
            ],
            'PrivateDnsEnabled': False,
            'DnsEntries': [
                {
                    'DnsName': 'string',
                    'HostedZoneId': 'string'
                },
            ],
            'NetworkInterfaceIds': ['string'],
            'CreationTimestamp': '1952-03-11T12:29:42Z'
        })

    return {"VpcEndpoints": endpoints}


def mock_create_vpc_endpoint():
        return {
            'VpcEndpoint': {
                'VpcId': 'vpc-2cafad42',
                'PolicyDocument': '{\"Version\":\"2008-10-17\",\"Statement\":[{\"Effect\":\"Allow\",'
                                  '\"Principal\":\"*\",\"Action\":\"*\",\"Resource\":\"*\"}]}',
                'NetworkInterfaceIds': [],
                'SubnetIds': [],
                'PrivateDnsEnabled': False,
                'State': 'available',
                'ServiceName': 'com.amazonaws.us-east-1.s3',
                'RouteTableIds': [],
                'Groups': [],
                'VpcEndpointId': 'vpce-14998642',
                'VpcEndpointType': 'Gateway',
                'CreationTimestamp': '14-03-2018T02:42:42Z',
                'DnsEntries': []
            }
        }

def mock_delete_vpc_endpoint(vpc_endpoint_id, failed=False):
    if not failed:
        return {'Unsuccessful': []}
    else:
        return {'Unsuccessful': [
            {
                'Error': {
                    'Code': 'InvalidVpcEndpoint.NotFound',
                    'Message': ''  # Message doesnt show up in REAL vpce.delete() API Call, but required by stubber!
                },
                'ResourceId': vpc_endpoint_id
            }
        ]}

class TestVPCEndpoints(unittest.TestCase):

    def setUp(self):
        self.session = boto3.session.Session(region_name='us-east-1')
        self.service_resource = self.session.resource('ec2')

    def test_get_endpoint(self):
        expected_endpoints = mock_endpoints(endpoint_services=['s3'])
        endpoint_id = expected_endpoints['VpcEndpoints'][0]['VpcEndpointId']
        with Stubber(self.service_resource.meta.client) as stubber:
            stubber.add_response('describe_vpc_endpoints', expected_endpoints)
            response = self.service_resource.VpcEndpoint(endpoint_id)
            self.assertEqual(response.vpc_id, expected_endpoints['VpcEndpoints'][0]['VpcId'])
            self.assertEqual(response.service_name, expected_endpoints['VpcEndpoints'][0]['ServiceName'])
            self.assertEqual(response.vpc_endpoint_id, expected_endpoints['VpcEndpoints'][0]['VpcEndpointId'])
            stubber.assert_no_pending_responses()

    def test_get_endpoint_not_found(self):
        with Stubber(self.service_resource.meta.client) as stubber:
            stubber.add_client_error('describe_vpc_endpoints',
                                     service_error_code='InvalidVpcEndpointId.NotFound',
                                     service_message="The Vpc Endpoint Id 'vpce-babababa' does not exist",
                                     http_status_code=400)

            with self.assertRaises(ClientError) as ex:
                response = self.service_resource.VpcEndpoint('vpce-babababa')
                vpc_endpoint_service_name = response.service_name
                stubber.assert_no_pending_responses()
            self.assertEqual(
                    str(ex.exception),
                    "An error occurred (InvalidVpcEndpointId.NotFound) when calling the DescribeVpcEndpoints "
                    "operation: The Vpc Endpoint Id 'vpce-babababa' does not exist"
                )
            self.assertEqual(ex.exception.response['ResponseMetadata']['HTTPStatusCode'], 400)

    def test_describe_endpoints(self):
        expected_endpoints = mock_endpoints()
        with Stubber(self.service_resource.meta.client) as stubber:
            stubber.add_response('describe_vpc_endpoints', expected_endpoints)
            response = list(self.service_resource.vpc_endpoints.all())
            stubber.assert_no_pending_responses()

        self.assertEqual(len(response), len(expected_endpoints['VpcEndpoints']))
        self.assertEqual(sorted([x.vpc_endpoint_id for x in response]),
                         sorted([x['VpcEndpointId'] for x in expected_endpoints['VpcEndpoints']]))

    def test_describe_endpoints_filter(self):
        # Filter doesnt really do anything here in unittests as botocore is doing actual work not boto3
        expected_endpoints = mock_endpoints(endpoint_services=['dynamodb'])
        with Stubber(self.service_resource.meta.client) as stubber:
            stubber.add_response('describe_vpc_endpoints', expected_endpoints)
            response = list(self.service_resource.vpc_endpoints.filter(
                Filters=[{'Name': 'service-name', 'Values': ['com.amazonaws.us-east-1.dynamodb']}]
            ))
            stubber.assert_no_pending_responses()

        self.assertEqual(response[0].id, expected_endpoints['VpcEndpoints'][0]['VpcEndpointId'])
        self.assertEqual(response[0].vpc_id, expected_endpoints['VpcEndpoints'][0]['VpcId'])
        self.assertEqual(response[0].service_name, expected_endpoints['VpcEndpoints'][0]['ServiceName'])

    def test_describe_endpoints_none(self):
        with Stubber(self.service_resource.meta.client) as stubber:
            stubber.add_response('describe_vpc_endpoints', {'VpcEndpoints': []})
            response = list(self.service_resource.vpc_endpoints.filter(
                Filters=[{'Name': 'service-name', 'Values': ['com.amazonaws.us-east-1.dynamodb']}]
            ))
            stubber.assert_no_pending_responses()

        self.assertEqual(response, [])

    def test_create_endpoint(self):
        expected_response = mock_create_vpc_endpoint()
        with Stubber(self.service_resource.meta.client) as stubber:
            stubber.add_response('create_vpc_endpoint', expected_response)
            response = self.service_resource.create_vpc_endpoint(VpcId='vpc-2fefad42',
                                                                 ServiceName='com.amazonaws.us-east-1.s3')
            stubber.assert_no_pending_responses()

        self.assertEqual(response.vpc_endpoint_id, expected_response['VpcEndpoint']['VpcEndpointId'])
        self.assertEqual(response.vpc_id, expected_response['VpcEndpoint']['VpcId'])
        self.assertEqual(response.service_name, expected_response['VpcEndpoint']['ServiceName'])

    def test_delete_endpoint(self):
        expected_response1 = mock_endpoints(endpoint_services=['s3'])
        expected_response2 = mock_delete_vpc_endpoint(expected_response1['VpcEndpoints'][0]['VpcEndpointId'])
        with Stubber(self.service_resource.meta.client) as stubber:
            stubber.add_response('describe_vpc_endpoints', expected_response1)
            stubber.add_response('delete_vpc_endpoints', expected_response2)
            endpoint = self.service_resource.VpcEndpoint(expected_response1['VpcEndpoints'][0]['VpcEndpointId'])
            service_name = endpoint.service_name  # dequeue stubber - list would do this for iterators.
            self.assertEqual(service_name, expected_response1['VpcEndpoints'][0]['ServiceName'])
            response = endpoint.delete(VpcEndpointIds=[endpoint.vpc_endpoint_id])
            stubber.assert_no_pending_responses()

        self.assertEqual(response['Unsuccessful'], [])

    def test_delete_endpoint_not_found_error(self):
        expected_response1 = mock_endpoints(endpoint_services=['s3'])
        expected_response2 = mock_delete_vpc_endpoint('vpce-babababa', True)
        with Stubber(self.service_resource.meta.client) as stubber:
            stubber.add_response('describe_vpc_endpoints', expected_response1)
            endpoint = self.service_resource.VpcEndpoint(expected_response1['VpcEndpoints'][0]['VpcEndpointId'])
            service_name = endpoint.service_name  # need this to dequeue stubber
            stubber.add_response('delete_vpc_endpoints', expected_response2)
            response = endpoint.delete(VpcEndpointIds=['vpce-babababa'])
            stubber.assert_no_pending_responses()

        self.assertEqual(response, mock_delete_vpc_endpoint('vpce-babababa', True))
