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
print('###################################################')

@bot.event
async def on_message(message):
    if message.attachments:
        url = message.attachments[0].url
        file_type = url.split('.')[-1]
        name = url  .split('/')[-1].split('.')[0]
        fp = f'from_dc/{name}_{random.randint(1111,9999)}.{file_type}'
        print(f'#Downloaded a file with extension {file_type}\n#Sent in : {message.guild}\n#Originally sent by {message.author}\nSaved to : from_dc/{name}_{random.randint(1111,9999)}.{file_type}')
        print('###################################################')

        resp = requests.get(url)
        file = open(fp,'wb+')
        file.write(resp.content)
        file.close()
bot.run(TOKEN, bot=False)