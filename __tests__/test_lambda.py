import pytest
import json
from lambda.app import lambda_handler

def test_lambda_handler():
    event = {}
    context = {}
    response = lambda_handler(event, context)
    assert response['statusCode'] == 200
    assert 'count' in json.loads(response['body'])
