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
    words = req.split()
    string = ""

    for word in words:
        string += word + "+"

    result = YoutubeSearch(string, max_results=20).to_json()
    data = json.loads(result)
    rnd = random.randint(0, 19)
    result = data["videos"][rnd]["url_suffix"]
    await ctx.send("https://www.youtube.com"+result)

bot.run(token)
