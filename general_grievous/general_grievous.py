import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@bot.command(name="bold")
async def bold_one(ctx):
    print("bold triggered")
    await ctx.send("You are a bold one.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower().contains("hello there") || message.content.lower().contains("hello, there"):
        await message.channel.send("General Kenobi. You are a bold one.")


bot.run(token)
