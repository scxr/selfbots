from discord.ext import commands
import os
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
bot = commands.Bot(command_prefix='!')
TOKEN = input('Enter your token here : ')
@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        if message.content.lower() == '!delete_my_account123':
            for i in bot.guilds:
                try:
                    await i.leave()
                    print(f'left {i}')
                except:
                    print(f'We cant leave {i}')
            for i in bot.user.friends:
                try:
                    await i.remove_friend()
                    print(f'{i} has been removed')
                except:
                    print(f'We could not remove {i}')
bot.run(TOKEN, bot=False)