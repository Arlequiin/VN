from keep_alive import keep_alive
import discord
import os # default module
from dotenv import load_dotenv
bot = discord.Bot()
@bot.command(description="Envoie la latence du bot") 
async def ping(ctx):
    await ctx.respond(f"Pong! {bot.latency}")
@bot.command(description="Envoie le sprite d'un Pokémon") 
async def sprite(ctx,pokemon):
    await ctx.respond(f"https://raw.githubusercontent.com/Arlequiin/pokeemerald-expansion/master/graphics/pokemon/{pokemon}/front.png")
keep_alive()
bot.run(os.getenv("TOKEN"))