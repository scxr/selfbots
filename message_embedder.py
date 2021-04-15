import discord, random
from discord.ext import commands
import os
import getpass
os.system('cls')
print(r'''
 .-._                                                   _,-,
  `._`-._                                           _,-'_,'
     `._ `-._                                   _,-' _,'
        `._  `-._        __.-----.__        _,-'  _,'
           `._   `#==="""           """===#'   _,'
              `._/)  ._               _.  (\_,'
               )*'     **.__     __.**     '*( 
               #  .==..__  ""   ""  __..==,  # 
xo#1010         #   `"._(_).       .(_)_."'   #         EV1L IN5IDE
ogu: nemo                                               discord: xo#1010
ig: w3ax                                                github: scxr''')
TOKEN = getpass.getpass('Enter your token here : ')
prefix = '!'
bot = commands.Bot(command_prefix=prefix, self_bot=True)


@bot.event
async def on_ready():
    print("Bot presence t u r n e d on ( ͡° ͜ʖ ͡°)")


@bot.command()
async def embed(ctx, *, message):
    message_arr = message.split('\n')
    if len(message_arr) < 2:
        print('''[ERROR] Your message format should be the following:\n
                !embed
                title here (required)
                description here (required)
                embed_thumbnail (optional)''')
        return
    title = message_arr[0]
    thumbnail_url = None
    description = message_arr[1]

    if len(message_arr) == 3:
        thumbnail_url = message_arr[2]

    embed = discord.Embed(title=title, description=description, colour=random.randint(0, 0xFFFFFF))
    if thumbnail_url != None:
        embed.set_thumbnail(url=thumbnail_url)
    await ctx.send(embed=embed)
    await ctx.message.delete()



bot.run(TOKEN, bot=False)