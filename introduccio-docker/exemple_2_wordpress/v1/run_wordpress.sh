#!/bin/bash
docker run \
    --rm \
    --network mynetwork \
    -p 80:80 \
    -v wordpress:/var/www/html \
    -e WORDPRESS_DB_HOST=db \
    -e WORDPRESS_DB_USER=joe \
    -e WORDPRESS_DB_PASSWORD=joe123 \
    -e WORDPRESS_DB_NAME=wordpress \
    wordpress:5
