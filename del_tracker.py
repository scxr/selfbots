from discord.ext import commands
import os
os.system('cls')
bot = commands.Bot(command_prefix='!!lkjfdasdklj')
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
TOKEN = input('Enter your token here : ')
guilds_ignore = input(
    'Please enter any guilds you would like to ignore : ').split()


@bot.event
async def on_message_delete(message):

    if str(message.guild.id) in guilds_ignore:
        return
    else:
        print('------------------------------------------------------------------------------------------------------')
        print(
            f'Message deleted in : {message.guild}\nGuild id : {message.guild.id}\nMessage author {message.author}\nMessage author id: {message.author.id}\nMessage content : {message.content}')
        print('------------------------------------------------------------------------------------------------------')
bot.run(TOKEN, bot=False)
