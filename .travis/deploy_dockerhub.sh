#!/bin/bash

if [ "$TRAVIS_BRANCH" = "master" ]; then
  docker login --username $DOCKER_NAME --password $DOCKER_PASS
  docker build -f Dockerfile -t $TRAVIS_REPO_SLUG:lastest .
  docker tag $TRAVIS_REPO_SLUG $DOCKER_REPO
  docker push $DOCKER_REPO
fi
