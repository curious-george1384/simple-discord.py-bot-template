import discord
from discord.ext import commands

prefix = '!'
token = 'YOUR_TOKEN_HERE' 

bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user})

@bot.command()
async def hello(ctx):
    await ctx.send("Hey!")

@bot.command()
async def square(ctx, num: int):
    sum = num * num
    await ctx.send(f"The square of {num} is {sum}.")
    
bot.run(token)