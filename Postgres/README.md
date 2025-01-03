# PostgreSQL Docker Setup & Testing

## Description
This setup deploys a PostgreSQL server using Docker Compose and provides a Python script to test connectivity and basic SQL operations.

## Setup
1. Start PostgreSQL server:
   
   `docker-compose up -d`

2. Run the test script:

   `python postgres_test.py`


## Features
- PostgreSQL server running on port `5432`.
- Default database: `testdb`.
- Default credentials: `admin/password`.
- Python script creates a table, inserts, and retrieves data.

