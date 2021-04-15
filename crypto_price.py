import requests
from discord.ext import commands

headers = {
    'accept': 'application/json',
}


real_names = {
    'btc':'bitcoin',
    'eth':'ethereum',
    'ltc':'litecoin',
    'uni':'uniswap'
}
def main(coin):
    coin = real_names.get(coin)
    if coin is None:
        return None
    params = (
        ('ids', coin),
        ('vs_currencies', 'usd'),
    )

    response = requests.get('https://api.coingecko.com/api/v3/simple/price', headers=headers, params=params)
    return response.json()

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_message(message):
    if str(message.channel.id) == '762845688634671144' or str(message.channel.id) == '623416794329120790':
        if message.content.startswith('p'):
            curr = message.content.split()[1]
            resp = main(curr)
            
            if resp:
                print(f'{message.author} requested {curr} succesfully')
                currency = real_names.get(curr)
                await message.channel.send(f"{currency} current price is : ${resp[currency]['usd']}\n*made by xo#1010*")
            else:
                print(f'{message.author} requested {curr} unsuccesfully')
                await message.channel.send('I currently only support btc, eth, ltc and uni if you want another support adding dm me what u want')
TOKEN=""
bot.run(TOKEN, bot=False)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=btc&vs_currencies=usd', headers=headers)
