import discord
import asyncio
import json
import time
from discord.ext import commands
bot = commands.Bot(command_prefix='$')
token = input('token : ')
delp = 'sendall'

@bot.command()
async def lol(message):
	#print(message)
	if message.author.id == bot.user.id:
		if message.content == delp:
			members = message.guild.members
			for member in members:
				try:
					chan = await member.create_dm()
					await chan.send('test')
				except Exception as e:
					print(e)
				await asyncio.sleep(1)
bot.run(token, bot=False, command_prefix='!')