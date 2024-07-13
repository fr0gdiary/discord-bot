import discord 
from discord.ext import commands
from bot_logic import ran_pass 

intents = discord.Intents.default()
intents.members = True
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def spam(ctx, spam_count=10):
    for i in range(spam_count):
        await ctx.send(f"Hahahaha {i+1}")

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)
    
bot.run('')