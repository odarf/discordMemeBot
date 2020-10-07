import json
import random
import praw
import applemusicpy
from youtube_search import YoutubeSearch
from discord.ext import commands

token = 'NzYxMjA0Nzk2MTQ0MzUzMjgw.X3XNNQ.Iq77g9EcEHrOf7w6v-HgEv8UWA0'
bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

reddit = praw.Reddit(client_id="zAmSKq4rw44kdA",
                     client_secret="JYNBubsgry0rnrWJYBvev7m7zv8",
                     user_agent="discordMemeBot",
                     redirect_uri="http://127.0.0.1:65010/authorize_callback")


@bot.command(pass_context=True)
async def play(ctx, url):
    author = ctx.message.author
    channel = ctx.author.voice.channel
    vc = await bot.connect()
    player = await vc.create_ytdl_player(url)
    player.start()


@bot.command(pass_context=True)
async def meme(ctx):
    for submission in reddit.subreddit("dankmemes").hot(limit=1):
        if not submission.stickied:
            await ctx.send(submission.url)


@bot.command(pass_context=True)
async def help(ctx):
    await ctx.send("```!yt + запрос - скидывает видео с YouTube™ в чат \n!meme - скидывает случайны мем с Reddit™"
                   "\n!music + запрос - скидывает плейлист Spotify™ по запросу```")


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
