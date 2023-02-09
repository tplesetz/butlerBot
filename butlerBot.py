import discord
import os

# This is the default intent set, but you can change it to whatever you want.
intents = discord.Intents.default()
intents.message_content = True

# This is the default activity, but you can change it to whatever you want.
client = discord.Client(intents=intents)

# This is the default status, but you can change it to whatever you want.
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# This is the default command, but you can change it to whatever you want.
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!clean'):
        async for msg in message.channel.history(limit=100):
            await msg.delete()

# This is the default token, but you can change it to whatever you want.
if __name__ == '__main__':
    os.environ['token'] = '<your token here>'
    client.run(os.environ['token'])
