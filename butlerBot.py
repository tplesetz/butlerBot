import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!clean'):
        async for msg in message.channel.history(limit=100):
            await msg.delete()

if __name__ == '__main__':
    os.environ['token'] = '<your token here>'
    client.run(os.environ['token'])
