import boto3

def test_dynamodb():
    try:
        dynamodb = boto3.resource(
            'dynamodb',
            endpoint_url='http://localhost:8000',
            region_name='us-east-1',
            aws_access_key_id='fake',
            aws_secret_access_key='fake'
        )
        table_name = "TestTable"
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {'AttributeName': 'id', 'KeyType': 'HASH'}
            ],
            AttributeDefinitions=[
                {'AttributeName': 'id', 'AttributeType': 'S'}
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )
        table.wait_until_exists()
        print(f"Table {table_name} created successfully!")
        table.put_item(Item={'id': '1', 'data': 'Hello, DynamoDB!'})
        response = table.get_item(Key={'id': '1'})
        print(f"Retrieved item: {response['Item']}")
    except Exception as e:
        print(f"DynamoDB error: {e}")

if __name__ == "__main__":
    test_dynamodb()