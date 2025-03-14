import pytest
import json
from unittest.mock import patch
from ..lambda_function.app import lambda_handler  # Relative import: .. goes up one directory

def test_lambda_handler():
    with patch('boto3.resource') as mock_dynamodb:
        mock_table = mock_dynamodb.return_value.Table
        mock_table.return_value.get_item.return_value = {'Item': {'id': 'resume', 'count': 0}}
        mock_table.return_value.update_item.return_value = {'Attributes': {'count': 1}}

        event = {}
        context = {}
        response = lambda_handler(event, context)
        assert response['statusCode'] == 200
        assert json.loads(response['body'])['count'] == 1
