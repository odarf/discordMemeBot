import json
import random
from youtube_search import YoutubeSearch
from discord.ext import commands

token = 'your_token'
bot = commands.Bot(command_prefix='!')


@bot.command(pass_context=True)
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@bot.command(pass_context=True)
async def leave(ctx):
    await ctx.voice_client.disconnect()


@bot.command(pass_context=True)
async def yt(ctx, req):
    input_words = req.split()
    yt_req = ""

    for word in input_words:
        yt_req += word + "+"

    data = json.loads(YoutubeSearch(yt_req, max_results=20).to_json())
    result_suffix = data["videos"][random.randint(0, 19)]["url_suffix"]
    await ctx.send("https://www.youtube.com" + result_suffix)


def main():
    bot.run(token)
    
    
if __name__ == "__main__":
    main()    
