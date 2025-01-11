# Jenkins Docker Compose Setup
#### Ref https://www.jenkins.io/doc/book/installing/docker/
This project sets up Jenkins using Docker Compose, with persistent configuration stored in the `jenkins_home` folder.

## Setup

1. **Clone this repository** (if needed).

2. **Ensure Docker and Docker Compose are installed** on your machine.

3. **Folder Structure**:
   - The `jenkins_home` folder holds all Jenkins configurations and is mounted as a volume inside the Jenkins Docker container.
   - A `.env` file is required for configuring the Jenkins agent.

## Running Jenkins

To start Jenkins:

```bash
docker-compose up -d
```

After the container is up, Jenkins will be accessible via the following URL:
- **Jenkins URL**: [http://localhost:8080](http://localhost:8080)

## Getting the Jenkins Admin Token

To retrieve the Jenkins admin token (for first-time login), run the following command:

```bash
docker logs -f jenkins-master
```

You will see the admin token displayed in the logs. Copy the token for login.

## Customizing the Jenkins Master Docker Container

If you need to install additional tools inside the Jenkins master container (e.g., Ansible), you can do so by editing the `master/Dockerfile`.

Once you've updated the Dockerfile, rebuild the container:

```bash
docker-compose up -d --build
```

## Accessing Jenkins Dashboard

Once Jenkins is running, open your browser and visit:

- **Dashboard URL**: [http://127.0.0.1:8080](http://127.0.0.1:8080)

## Stopping Jenkins

To stop Jenkins, run:

```bash
docker-compose down
```

This will stop the containers and remove them.

## Volumes and Data Persistence

- The `jenkins_home` folder persists Jenkins data across container restarts.
- You can back up and restore Jenkins data by managing the contents of this folder.

## Troubleshooting

- If Jenkins is not starting or facing issues, check the logs:

```bash
docker logs jenkins-master
```

## Configuring the Jenkins Build Agent
#### ref https://github.com/jenkinsci/docker-inbound-agent
1. **Add a New Node**:
   - In the Jenkins UI:
     - Navigate to **Manage Jenkins > Nodes > New Node**.
     - Provide a name for the node (e.g., `Builder-01`) and configure it as a **Permanent Agent**.
   - Save the node configuration.
   - Go to the node's status page to retrieve the **secret key** & **node name** and use it in the `.env` file.

2. **Prepare the `.env` File**:
   - Create a `.env` file in the root directory with the following values:
     ```plaintext
     JENKINS_AGENT_NAME=<node_name>
     JENKINS_SECRET=<agent_secret>
     ```
   - Replace `<node_name>` with the name of the agent node you create.
   - Replace `<agent_secret>` with the secret retrieved from the Jenkins UI.

3. **Rebuild and Start the Agent**:
   - After updating the `.env` file, restart the services:
     ```bash
     docker-compose up -d --build
     ```

4. **Verify Connection**:
   - Check the **Manage Nodes and Clouds** section in Jenkins to see if the agent is connected.

## Troubleshooting

- If the agent is not connecting, ensure the `.env` file is correctly configured and matches the node name and secret from Jenkins.
- Check the logs for errors:

```bash
docker logs -f jenkins-master
docker logs -f jenkins-agent
```