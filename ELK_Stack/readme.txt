es may fail due to permision issue , using current path folder instead of docker volume so

mkdir ./elasticsearch-data
chmod -R 777 ./elasticsearch-data
chown -R 1000:1000 ./elasticsearch-data



for auto-generate the password
docker exec -it elasticsearch bin/elasticsearch-setup-passwords auto
replace the password with kibana & docker-compose up -d --build --force-recreate --no-deps kibana 

use kibana_system password at docker-compose file 
use elastic password for login kibana & logstash.conf


for specific user password reset 

Create password for users : elastic & kibana_system
docker exec -it elasticsearch /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic
docker exec -it elasticsearch /usr/share/elasticsearch/bin/elasticsearch-reset-password -u kibana_system