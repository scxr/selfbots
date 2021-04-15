  
import discord, asyncio
from discord.ext import commands
import os
import getpass
import random
os.system('cls')
bot = commands.Bot(command_prefix='48327489237489324789234789234732984732984723987')

print(r'''
 .-._                                                   _,-,
  `._`-._                                           _,-'_,'
     `._ `-._                                   _,-' _,'
        `._  `-._        __.-----.__        _,-'  _,'
           `._   `#==="""           """===#'   _,'
              `._/)  ._               _.  (\_,'
               )*'     **.__     __.**     '*( 
               #  .==..__  ""   ""  __..==,  # 
xo#1111         #   `"._(_).       .(_)_."'   #         EV1L IN5IDE
ogu: nemo                                               discord: xo#1111
ig: w3ax                                                github: scxr''')

TOKEN = getpass.getpass('Enter your password here (no output will be shown) : ')
print('logged in')
@bot.event
async def on_message(message):
    if str(message.content) == '!dbump':#
        embed = discord.Embed(title='Starting bumping in this channel', description='Bumping in 2 hours !!!', colour=random.randint(0,0xFFFFFF))
        await message.channel.send(embed=embed)
        while 1:
            await asyncio.sleep(7200)
            try:
                await message.channel.send('!d bump')
                print('Waiting 2 hours')
            except Exception as e:
                print(e)

            
@bot.command(pass_context=True)
async def dbump(ctx):
    print('ok')
    try:
        await ctx.message.channel.send('!d bump')
        print('bumping')
    except Exception as e:
        print(e)
    await asyncio.sleep(7200)

bot.run(TOKEN, bot=False)