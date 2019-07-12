"""
1 - Get the role attached to the function
2 - This will get you the PolicyArn
3 - Which will give you the Policy Versions
4 - Which will give you the Policy Document 
"""

import boto3
import pprint
import sys
import json
import yaml

lambda_client = boto3.client('lambda')
iam_client = boto3.client('iam')

#Get the role attached to the function
function_name = sys.argv[1]

lambda_function = lambda_client.get_function(
    FunctionName=function_name
)

role_name = lambda_function['Configuration']['Role'].split('/')[2]

#Get the policy arn
attached_role_policies = iam_client.list_attached_role_policies(
    RoleName=role_name
)

policy_arn = attached_role_policies['AttachedPolicies'][0]['PolicyArn']

#Get the policy's version - capture only the latest once
policy_versions = iam_client.list_policy_versions(
    PolicyArn=policy_arn
)

version_id = policy_versions['Versions'][0]['VersionId']

#Get the policy document
policy_version = iam_client.get_policy_version(
    PolicyArn=policy_arn,
    VersionId=version_id
)

policies = policy_version['PolicyVersion']['Document']['Statement']


entire_policy = ''
for policy in policies:
    entire_policy += json.dumps(policy)
    
print(json.loads(entire_policy))
