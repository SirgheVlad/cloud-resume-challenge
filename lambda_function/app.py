import json
import boto3
import os
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)

def lambda_handler(event, context):
    try:
        # Initialize DynamoDB table dynamically
        table_name = os.getenv('TABLE_NAME', 'VisitorCountNew')  # Default to 'VisitorCountNew' if not set
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(table_name)

        # Get current item
        response = table.get_item(Key={'id': 'resume'})
        item = response.get('Item', {'id': 'resume', 'count': 0})
        current_count = item.get('count', 0)
        new_count = current_count + 1

        # Update the item
        table.update_item(
            Key={'id': 'resume'},
            UpdateExpression='SET #c = :val',
            ExpressionAttributeNames={'#c': 'count'},
            ExpressionAttributeValues={':val': new_count},
            ReturnValues='UPDATED_NEW'
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'count': new_count}, cls=DecimalEncoder),
            'headers': {
                'Access-Control-Allow-Origin': 'https://sirghevladaws.com',
                'Content-Type': 'application/json'
            }
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}, cls=DecimalEncoder),
            'headers': {
                'Access-Control-Allow-Origin': 'https://sirghevladaws.com',
                'Content-Type': 'application/json'
            }
        }
