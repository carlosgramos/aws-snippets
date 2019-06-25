#Python3.6
import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info('got event{}'.format(event))
    #TO DO

    try:
        #TO DO 

    except Exception as e:
        #TO DO

    finally:
        return {
            'statusCode': '200',
            'body': json.dumps(message),
            'headers': {
                'Access-Control-Allow-Origin' : '*',
                'Content-Type': 'application/json'
            }
