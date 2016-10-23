#! /usr/bin/env bash

# Build docker image and run it
docker-compose up --build

# When it has terminated, bring everything down and delete the local image
docker-compose down --rmi local

