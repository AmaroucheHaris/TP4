from Bot.MyBot import MyBot
from Log.Logger import Logger
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="./config")
token = os.getenv("TOKEN")


bot = MyBot(token=token)

#---------------------------------------------------------------------------------------------#

"""
bot = commands.Bot(command_prefix="!haris")
bot.run(token)

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord")

@bot.command(name="del")
async def delete(ctx, number: int):
    messages = await ctx.channel.history(limit=number + 1).flatten()
    
    for each_message in messages:
        await each_message.delete()
"""