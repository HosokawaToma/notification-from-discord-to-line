import discord
import config as config

intents = discord.Intents.none()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

client.run(config.DISCORD_TOKEN())
