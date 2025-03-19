"""Discord Bot の起動とイベントハンドリングを管理するモジュール。"""

import discord
import events
import config

intents = discord.Intents.none()

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    """Botが起動した際に実行される処理。"""
    events.on_ready()
    print(f'We have logged in as {client.user}')

client.run(config.DISCORD_TOKEN())
