import discord
from discord.ext import commands
prefix='.'
tokens='OTg1ODQ2MjQ3NDg1MjE0NzMw.G41-sT.D2LUXArPZy4fYxmaAJqMJjAdkC3O-_H2cj0zOQ'

bot = discord.Client()

@bot.event
async def on_ready():
    print("Bot is ready")

bot.run(tokens)