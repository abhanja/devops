import json
import boto3

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    
    tableUser = dynamodb.Table('Users_table')
    response = tableUser.scan()
    return {
    'statusCode': 200,
    'body': response['Items']
    }