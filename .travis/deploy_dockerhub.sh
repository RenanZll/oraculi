#!/bin/bash

if [ "$TRAVIS_BRANCH" = "master" ]; then
  echo "\nDocker login -->"
  docker login --username $DOCKER_USER --password $DOCKER_PASS &&

  echo "\nDelete __pycache__ files created by Docker -->"
  find . -name "__pycache__" | sudo xargs rm -rf && \
    echo "Files deleted!"

  echo "\nDocker build and tag -->"
  docker build -f Dockerfile -t oraculi:latest -t oraculi:v$TRAVIS_COMMIT . && \
    docker tag  oraculi $DOCKER_REPO

  echo "\nDocker push -->"
  docker push $DOCKER_REPO && echo "\nImage deployed in Docker Hub! :)"
fi
