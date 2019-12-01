if [ "$TRAVIS_BRANCH" = "master" ]; then
  echo "Install Heroku client -->"
  wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
  heroku plugins:install @heroku-cli/plugin-container-registry

  echo "Heroku registry login -->"
  docker login --username _ --password=$HEROKU_API_KEY registry.heroku.com

  echo "Push image to Heroku -->"
  heroku container:push web --app $HEROKU_APP_NAME
  
  echo "Release to pushed image -->"
  heroku container:release web --app $HEROKU_APP_NAME
fi
