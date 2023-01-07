from keep_alive import keep_alive
import discord
from pokemon import *
from PIL import Image
import os
from code import *

bot = discord.Bot()
bot.change_presence(activity=discord.Game(name="Pokémon Résurrection"))
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
@bot.command(description="Envoie les informations d'un Pokémon") 
async def dex(ctx,pokémon):
    #try:
      pokemon=get_name(pokémon)
      infos=get_info(pokemon[0])
      if infos['type1']==infos['type2']:
        type_=type_to_emote[french_types[infos['type1'].replace("TYPE_",'').lower()]]
      else:
        type_=type_to_emote[french_types[infos['type1'].replace("TYPE_",'').lower()]]+' '+type_to_emote[french_types[infos['type2'].replace("TYPE_",'').lower()]]
      embed = discord.Embed(title=f"{pokemon[1]}",description=f"__N°???__ (Nom :flag_gb:: {pokemon[0]})\n**Type(s)** : {type_}\n**Talents:** {infos['ability']}\n **Stats de base** :\nPV : {infos['hp']}\nAtq : {infos['atk']}\nDef : {infos['def']}\nAtq.Spé : {infos['sp.atk']}\nDef.Spé : {infos['sp.def']}\nVit : {infos['speed']}",color=type_to_color[french_types[infos['type1'].replace("TYPE_",'').lower()]])
      embed.set_thumbnail(url=f'https://raw.githubusercontent.com/Arlequiin/pokeemerald-expansion/master/graphics/pokemon/{pokemon[0]}/front.png')
      await ctx.respond(embed=embed)
    #except:
    #  await ctx.respond(embed=discord.Embed(title=":x: ERREUR",description="Vous avez :\n- Mal saisi le nom du Pokémon (ex : `Majspic` au lieu de `Majaspic`)\n- Vous avez saisi le nom d'un Pokémon de la 9ème génération (ex : `Poussacha`)\n*Si rien de tout cela n'est vrai, veuillez contacter `Arlequiin#1853`*"))
keep_alive()
bot.run(os.getenv("TOKEN"))