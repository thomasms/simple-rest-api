#!/bin/bash

if [ -z "$1" ]; then
    echo 'You must specify a Docker Hub username!'
    exit 1
else
    username=$1
fi
if [ -z "$2" ]; then
    echo 'Missing tag name, setting to "prototype"'
    tag_name=prototype
else
    tag_name=$2
fi
if [ -z "$3" ]; then
    echo 'Missing tag number, setting to "latest"'
    tag_number=latest
else
    tag_number=$3
fi

docker run -p 8080:8080 -u 143 ${username}/${tag_name}:${tag_number}
