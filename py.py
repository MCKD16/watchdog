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
  if message.content == "!report":
    if message.content[8:16] == "Cheating":
      if message.content[17:]:
        await client.send_message(message.channel, "Reported by: `" + message.author + "`\nA reported person: `" + message.content[18:] + "`\nReason: `Cheating`")
    else if message.content[8:16] == "Boosting":
      if message.content[17:]:
        await client.send_message(message.channel, "Reported by: `" + message.author + "`\nA reported person: `" + message.content[18:] + "`\nReason: `Boosting`")
    else if message.content[8:16] == "Teammate":
      if message.content[17:]:
        await client.send_message(message.channel, "Reported by: `" + message.author + "`\nA reported person: `" + message.content[18:] + "`\nReason: `Teammate`")
  if message.content == "!reasons":
    await client.send_message(message.channel, "`Reason Types:`\n`Cheating`\n`Boosting`\n`Teammate`")
  if message.content == "!help":
    await client.send_message(message.channel, "`Commands:`\n`!report (reason) (username)` - report the player.\n`!reasons` - Report types.")


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
