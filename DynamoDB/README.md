# DynamoDB Local Setup and Testing

## Description
This setup deploys a local instance of DynamoDB using Docker Compose. It ensures that database-related files are stored persistently and provides instructions to test connectivity using a Python script.

---

## Prerequisites
- Docker and Docker Compose installed on your system.
- Python installed, along with the `boto3` library for AWS SDK.

---

## Setup

### 1. Start DynamoDB Local
Run the following command to start the DynamoDB container in detached mode:
```bash
docker-compose up -d
```
This will:
- Expose DynamoDB on port `8000`.
- Create a `docker` folder to store database-related files for persistence.

### 2. Verify the Container
To check if the DynamoDB container is running:
```bash
docker ps
```
Ensure the `dynamodb` container is listed.

---

## Python Test Script
Use the provided Python script `Test_dynamoDB.py` to verify the connection and functionality. The script:
- Connects to the local DynamoDB instance.
- Creates a sample table.
- Inserts and retrieves data.

### Install Dependencies
Install the required Python package using pip:
```bash
pip install boto3
```

### Run the Test Script
Execute the script to confirm everything is working:
```bash
python Test_dynamoDB.py
```

---

## DynamoDB Local Details
- **Command**: `-sharedDb -dbPath ./data` ensures shared access and persistence.
- **Image**: `amazon/dynamodb-local:latest` is used to fetch the latest DynamoDB local image.
- **Working Directory**: `/home/dynamodblocal` inside the container.
- **Volume**: Maps `./docker/dynamodb` on the host to `/home/dynamodblocal/data` in the container for data persistence.

---

## Troubleshooting
1. **Container Not Running:**
   - Check logs using `docker logs dynamodb`.

2. **Test Script Failing:**
   - Ensure the container is running on port `8000`.
   - Verify that `boto3` is installed.

3. **Database Files Not Persisting:**
   - Confirm the `docker` folder exists and has correct permissions.

---

## Cleanup
To stop and remove the container, run:
```bash
docker-compose down
```

To remove the database files, delete the `docker` folder:
```bash
rm -rf ./docker/dynamodb
```

