import discord
import os
from discord import app_commands

# This is the default intent set, but you can change it to whatever you want.
class aclient(discord.Client):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        self.activity = discord.Activity(type=discord.ActivityType.watching, name="/clean")

# Function to delete a specified number of messages from a channel
async def delete_messages(channel, num_messages):
    messages = []
    async for message in channel.history(limit=num_messages):
        messages.append(message)
    await channel.delete_messages(messages)


client = aclient()

@client.event
async def on_ready():
    await client.tree.sync()

@client.tree.command(name="clean", description="Sweep up the mess in this channel.")

async def clean(interaction: discord.Interaction, *, amount: int):
    await interaction.response.send_message("Cleaning up your filth...", ephemeral=True, delete_after=3)
    await delete_messages(interaction.channel, amount)
    await interaction.channel.send("Done cleaning up!", delete_after=3)

# This is the default token, but you can change it to whatever you want.
if __name__ == '__main__':
    os.environ['token'] = 'MTA3MzAxMDQ2MTAwOTc5MzA3Ng.GIBkGr.buyoAENAVQv7B2GWuGi3JETYPXz5eIwPvWKNlA'
    client.run(os.environ['token'])
