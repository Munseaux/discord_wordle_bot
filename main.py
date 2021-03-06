import discord 
import os
import config

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    wordle_channel = config.CHANNEL_ID  
    if str(message.channel.id) == str(wordle_channel):
        words = message.content.split()
        score = words[2]

        if int(score[0]) < 5:
            await message.pin()


client.run(config.TOKEN)




