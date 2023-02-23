# butlerBot
You'll need a Discord bot to get started. Here is a reference for how to set one up

https://discord.com/developers/docs/getting-started

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
