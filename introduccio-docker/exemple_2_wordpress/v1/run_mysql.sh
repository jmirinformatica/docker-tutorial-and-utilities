#!/bin/bash

# creem la xarxa compartida
docker network create mynetwork

docker run \
    --rm \
    --name db \
    --network mynetwork \
    -v mysql:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=root123 \
    -e MYSQL_DATABASE=wordpress \
    -e MYSQL_USER=joe \
    -e MYSQL_PASSWORD=joe123 \
    mysql:5.7
