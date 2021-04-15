from discord.ext import commands
import os, requests, random, getpass
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
xo#1111         #   `"._(_).       .(_)_."'   #         EV1L IN5IDE
ogu: nemo                                               discord: xo#1111
ig: w3ax                                                github: scxr''')

TOKEN = getpass.getpass('ENTER YOUR TOKEN (there is no output for this, your token is hidden) : ')
bot = commands.Bot(command_prefix='==')
print('[+] LOGGED IN :)')
guilds_ignore = input(
    'Please enter any guilds you would like to ignore : ').split()
@bot.event
async def on_message_edit(before, after):
    if str(before.guild.id) in guilds_ignore:
        print(f'Message ignored in {before.guild.id}')
        return
    else:
        if before.content == '' and after.content == '':
            return

        print('###############################')
        print(f'''\
            Message sent by : {after.author}
            Server sent in : {after.guild}
            Message content before edit : {before.content}
            Message after edit : {after.content}''')
        print('###############################')

bot.run(TOKEN, bot=False)