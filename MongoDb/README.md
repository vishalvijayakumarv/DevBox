
# MongoDB and Mongo Express Docker Setup

This repository contains a Docker Compose configuration to set up MongoDB and Mongo Express for local development.

## Prerequisites

- Docker installed on your system.
- Docker Compose installed.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Configure Environment Variables**
   - Copy the `.env.sample` file to `.env`:
     ```bash
     cp .env.sample .env
     ```
   - Modify the `.env` file with your desired environment variable values.

3. **Start the Services**
   Run the following command to start the services:
   ```bash
   docker-compose up -d
   ```

4. **Access Mongo Express**
   - Mongo Express is available at [http://127.0.0.1:8081](http://127.0.0.1:8081).
   - **Basic Authentication**: Use the credentials `admin:pass`. If you encounter issues, check the logs to verify the credentials:
     ```bash
     docker logs -f mongo-express
     ```

5. **Database Connection**
   - Other applications can connect to MongoDB at `127.0.0.1:27017`.
   - Use the credentials defined in your `.env` file.

## Data Persistence

A volume folder named `mongo_data` will be created in the project directory to store MongoDB data persistently.

## Environment Variables

Make sure your `.env` file contains the following variables:

```env
# MongoDB credentials
MONGO_INITDB_ROOT_USERNAME=admin
MONGO_INITDB_ROOT_PASSWORD=admin

# Mongo Express credentials
ME_CONFIG_MONGODB_ADMINUSERNAME=admin
ME_CONFIG_MONGODB_ADMINPASSWORD=admin
```

## Stopping the Services

To stop the services, run:
```bash
docker-compose down
```

## Additional Information

- Ensure that the `mongo_data` directory has appropriate permissions if you're facing issues with data persistence.
- For troubleshooting, check the logs:
  ```bash
  docker logs -f mongodb
  docker logs -f mongo-express
  ```

Happy coding!
