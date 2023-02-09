import discord
import os

# This is the default intent set, but you can change it to whatever you want.
intents = discord.Intents.default()
intents.message_content = True

# This is the default activity, but you can change it to whatever you want.
client = discord.Client(intents=intents)

# Function to delete a specified number of messages from a channel
async def delete_messages(channel, num_messages):
    messages = []
    async for message in channel.history(limit=num_messages):
        messages.append(message)
    await channel.delete_messages(messages)

# This is the default status, but you can change it to whatever you want.
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Event that triggers when the bot receives a message
@client.event
async def on_message(message):
    # Check if the message starts with the prefix "!delete"
    if message.content.startswith("!delete"):
        # Extract the number of messages to delete
        num_messages = int(message.content.split(" ")[1])
        # Delete the specified number of messages from the channel
        await delete_messages(message.channel, num_messages)

# This is the default token, but you can change it to whatever you want.
if __name__ == '__main__':
    os.environ['token'] = '<your token here>'
    client.run(os.environ['token'])
