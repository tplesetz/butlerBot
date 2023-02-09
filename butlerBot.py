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
    os.environ['token'] = 'MTA3MzAxMDQ2MTAwOTc5MzA3Ng.G7HMmz.rFGULLB6D-zYW_pXQlVt6ZosCaLXwX8pyfGcW8'
    client.run(os.environ['token'])
