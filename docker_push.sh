#!/usr/bin/env bash

echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin

docker push benblamey/image_analysis_container2:latest