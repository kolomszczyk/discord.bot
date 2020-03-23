TOCKEN = 'NjkxNjM1MzA4ODYwNjY5OTgz.Xni2aA.xTx75j8Ar2SwuBUgYrQ8S0LOGK4'
import discord
from discord.ext import commands

client = discord.Client(command_prefix = '!~')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    client.say('elo wszystkim ')

@client.event
async def on_message(message):
    print('Message from {0.author}: {0.content}'.format(message))
    if message == '.exit':
        exit()


    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.command()
async def exit():
	client.say("Opuszaczam discorda")




client.run(TOCKEN)