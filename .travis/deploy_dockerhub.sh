#!/bin/bash

if [ "$TRAVIS_BRANCH" = "master" ]; then
  echo "Docker login -->"
  docker login --username $DOCKER_USER --password $DOCKER_PASS
  echo "Docker build -->"
  docker build -f Dockerfile -t oraculi:lastest -t oraculi:v$TRAVIS_COMMIT .
  echo "Docker tag -->"
  docker tag  oraculi $DOCKER_REPO
  echo "Docker push -->"
  docker push $DOCKER_REPO
fi
