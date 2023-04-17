#!/bin/bash

mysql_service_host=$MYSQL_SERVICE_HOST
mysql_service_port=$MYSQL_SERVICE_PORT

while ! nc -z $mysql_service_host $mysql_service_port; do
    sleep 1
done
echo "Database started!"
alembic stamp head
alembic upgrade head
python /app/main.py
