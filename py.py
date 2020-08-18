import discord
import os
import datetime


client = discord.Client()


@client.event
async def on_ready():
  print("login")
  print(client.user.name)
  print(client.user.id)
  print("------------------")
  await client.change_presence(game=discord.Game(name='!help', type=1))
  
@client.event
async def on_message(message):



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
