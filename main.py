from keep_alive import keep_alive
import discord
from pokemon import *
from PIL import Image
import os
from code import *

bot = discord.Bot()
#----------------------------------------------------
@bot.command(description="Envoie la latence du bot") 
async def ping(ctx):
  await ctx.respond(f"Pong! {bot.latency}")
  
@bot.command(description="Envoie le sprite d'un Pokémon") 
async def sprite(ctx,pokémon):
    await ctx.send(file=discord.File(get_front_sprite(pokémon)))
keep_alive()
bot.run(os.getenv("TOKEN"))