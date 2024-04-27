import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    tableUsers = dynamodb.Table('Users_table')
    id = event['User_Id']
    print('id')
    city = event['City']
    print('City')
    email = event['Email']
    print('email')
    mobile = event['Mobile']
    print('mobile')
    
    try:
        tableUsers.put_item(
            Item={
                "User_Id": id,
                "City": city,
                "Email": email,
                "Mobile":mobile
            }
        )
        return {
        'statusCode': 200,
        'body': json.dumps('Inserted')
        }
    except:
        print("Closing lambda function")
        return{
        'statusCode': 400,
        'body': json.dumps('Error')
        }
        
        
        
    
