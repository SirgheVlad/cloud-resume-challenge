import json
import boto3
import os
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.getenv('TABLE_NAME'))

# Test CI/CD pipeline

# Custom JSON encoder to handle Decimal
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)

def lambda_handler(event, context):
    try:
        # Try to get the current item (if it exists)
        response = table.get_item(Key={'id': 'resume'})
        item = response.get('Item', {'id': 'resume', 'count': 0})  # Default to 0 if item doesn't exist
        
        # Update the count
        current_count = item.get('count', 0)  # Default to 0 if count doesn't exist
        new_count = current_count + 1

        # Update the item in DynamoDB
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
            'headers': {'Access-Control-Allow-Origin': '*'}
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}, cls=DecimalEncoder),
            'headers': {'Access-Control-Allow-Origin': '*'}
        }
