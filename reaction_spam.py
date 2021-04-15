from discord.ext import commands
import os
import getpass
os.system('cls')
bot = commands.Bot(command_prefix='!')
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
TOKEN = getpass.getpass('INPUT YOUR TOKEN : ')
emojis = ['😄','😂','😹','😩','👌','👨‍🦲','🐉','🤩','🥳','😥','😌','🧑‍🚒','🍆','😠','💵','🤱','😡']
channel_to_spam = input('Enter channel id to spam (once this stops working you will be asked to enter again): ')
bot = commands.Bot(command_prefix='-----------------------')
@bot.event
async def on_message(message):
    if str(message.channel.id) == channel_to_spam:
        try:
            for i in emojis:
                
                await message.add_reaction(i)
        except:
            channel_to_spam = input('Enter new channel id, cant add to the previous one : ')

bot.run(TOKEN, bot=False)