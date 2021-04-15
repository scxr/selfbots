from discord.ext import commands
import requests
bot = commands.Bot(command_prefix="adkjaskldjsakldjaskldjaslkdjaslkdjl")
webhook=""
TOKEN = ""
def dm_recieved(author, message, channel_id):
    poglul = {
        "avatar_url":"https://pbs.twimg.com/profile_images/930577665643438080/VVjqz6XO.jpg",
        "name":"~~~~~",
        "embeds": [
            {
                "title": f"Message from {author}",
                "description": f"Message content: {message}",
                "color": 15146294,
                "footer":{
                    "text":f"made by xo#0316\nid:{channel_id}"
                    },

            }
        ]
    }
    req = requests.post(webhook, json=poglul)
    
@bot.event
async def on_message(message):
    msg_guild = message.guild
    if not msg_guild:
        dm_recieved(message.author, message.content, message.channel.id)
    if message.content.startswith("!~~!reply!"):
        splitmsg = message.content.split()
        channel_id = splitmsg[1]
        chan = bot.get_channel(int(channel_id))
        await chan.send(" ".join(splitmsg[2::]))
        await message.channel.send('Reply sent')


bot.run(TOKEN, bot=False)