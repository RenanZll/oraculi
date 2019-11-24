#!/bin/bash

if [ "$TRAVIS_BRANCH" = "master" ]; then
  echo "Docker login -->"
  docker login --username $DOCKER_NAME --password $DOCKER_PASS
  echo "Docker build -->"
  docker build -f Dockerfile -t $TRAVIS_REPO_SLUG:lastest .
  echo "Docker tag -->"
  docker tag $TRAVIS_REPO_SLUG $DOCKER_REPO
  echo "Docker push -->"
  docker push $DOCKER_REPO
fi
