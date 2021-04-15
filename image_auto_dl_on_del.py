from discord.ext import commands
import os, requests, random, getpass
os.system('cls')
bot = commands.Bot(command_prefix='=======  ')
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

TOKEN = getpass.getpass('ENTER YOUR TOKEN HERE (NO OUTPUT SHOWN) : ')

print('[+] LOGGED IN [+]')
print('ok')
@bot.event
async def on_message_delete(message):
   print(message.attachments)
   if message.attachments:
      url = message.attachments[0].url
      file_type = url.split('.')[-1]
      name = url.split('/')[-1].split('.')[0]
      fp = f'dc_deletes/{name}_{random.randint(1111,9999)}.{file_type}'
      print('###################################################')
      print(f'#Downloaded a file with extension {file_type}\n#Sent in : {message.guild}\n#Originally sent by {message.author}\nSaved to : dc_deletes/{name}_{random.randint(1111,9999)}.{file_type}')
      print('###################################################')

      resp = requests.get(url)
      file = open(fp,'wb+')
      file.write(resp.content)
      file.close()

bot.run(TOKEN, bot=False)