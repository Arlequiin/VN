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
    try:
      await ctx.respond(file=discord.File(get_front_sprite(pokémon)))
    except:
      await ctx.respond(embed=discord.Embed(title=":x: ERREUR",description="Vous avez :\n- Mal saisi le nom du Pokémon (ex : `Majspic` au lieu de `Majaspic`)\n- Vous avez saisi le nom d'un Pokémon de la 9ème génération (ex : `Poussacha`)\n*Si rien de tout cela n'est vrai, veuillez contacter `Arlequiin#1853`*"))

keep_alive()
bot.run(os.getenv("TOKEN"))