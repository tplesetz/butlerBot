# butlerBot
Head over to dockerhub for installation
https://hub.docker.com/r/tylerplesetz/butlerbot

## pull
```docker
# pull image from dockerhub
docker pull tylerplesetz/butlerbot:latest
```

## build
```docker
# build image
sudo docker build -t butlerbot .
```


## run
```docker
# create container and run
sudo docker run -d --name butlerbot --env DISCORD_BOT_TOKEN="token" tylerplesetz/butlerbot:latest
