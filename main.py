from keep_alive import keep_alive
import discord
import os # default module
from dotenv import load_dotenv
bot = discord.Bot()
@bot.command(description="Sends the bot's latency.") 
async def ping(ctx):
    await ctx.respond(f"Hello world")
keep_alive()
bot.run(Token)