# MySQL and phpMyAdmin Docker Setup

This project provides a quick and easy way to set up a MySQL server with phpMyAdmin for database management using Docker Compose.

## Prerequisites
- Docker installed on your system
- Docker Compose installed

---

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create the `.env` file**:
   - Copy the sample environment file:
     ```bash
     cp env.sample .env
     ```
   - Update the `.env` file with your custom configuration if needed.

3. **Start the containers**:
   ```bash
   docker-compose up -d
   ```

   This will spin up:
   - MySQL container on port **3306** (default).
   - phpMyAdmin container on port **8001** (default).

---

## Configuration Details

### Environment Variables
The `.env` file contains configurable variables:

| Variable         | Default Value        | Description                                              |
|------------------|----------------------|----------------------------------------------------------|
| `MYSQL_PORT`     | `3306`              | Port for MySQL service.                                  |
| `MYSQL_DATABASE` | `sample_database`   | The name of the default database to create.              |
| `MYSQL_USER`     | `mysql_user`        | The default MySQL user.                                  |
| `MYSQL_PASSWORD` | `mysql_user_pass`   | Password for the default MySQL user.                     |
| `MYSQL_ROOT_PASSWORD` | `password123`  | Root password for MySQL.                                 |
| `PHPMYADMIN_PORT`| `8001`              | Port for phpMyAdmin web interface.                       |
| `PMA_HOST`       | `mysql`             | MySQL host (matches the MySQL container service name).    |
| `UPLOAD_LIMIT`   | `50000000`          | File upload limit for phpMyAdmin web interface (in bytes).|

---

## Notes

1. **Data Persistence**:
   - A volume named `mysql_data` is created at the root directory of the `docker-compose.yml` file to store MySQL data persistently.

2. **Customizing File Upload Limit**:
   - Adjust the `UPLOAD_LIMIT` in the `.env` file as per your requirements. This setting is used for uploading SQL files via the phpMyAdmin web interface.

3. **Adding Multiple MySQL Hosts**:
   - To manage multiple MySQL hosts in phpMyAdmin, update the `phpmyadmin_config/config.user.inc.php` file.

---

## Accessing Services

- **phpMyAdmin Web Interface**: [http://localhost:8001](http://localhost:8001)
- **MySQL**: Accessible via localhost on port 3306.

---

## Stopping the Containers
To stop the containers, run:
```bash
docker-compose down
```
This will also remove the containers but preserve the data in the `mysql_data` volume.

---

## Troubleshooting

- Ensure that the `.env` file is correctly set up before starting the containers.
- Check logs for errors:
  ```bash
  docker-compose logs
  ```

