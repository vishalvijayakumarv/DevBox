FROM jenkins/jenkins:2.401.1

USER root

# Install Ansible
RUN apt-get update && \
    apt-get install -y ansible

USER jenkins