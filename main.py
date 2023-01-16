from keep_alive import keep_alive
import discord
from pokemon import *
from PIL import Image
import os
from code import *

bot = discord.Bot()
#bot.change_presence(activity=discord.Game(name="Pokémon Résurrection"))
#----------------------------------------------------
@bot.command(description="Envoie la latence du bot") 
async def ping(ctx):
  await ctx.respond(f"Pong! {bot.latency}")
  
@bot.command(description="Envoie le sprite d'un Pokémon") 
async def sprite(ctx,pokémon):
    try:
      await ctx.respond(file=discord.File(get_front_sprite(pokémon)))
    except:
      await ctx.respond(embed=discord.Embed(title="❌ ERREUR",description="Vous avez :\n- Mal saisi le nom du Pokémon (ex : `Majspic` au lieu de `Majaspic`)\n- Vous avez saisi le nom d'un Pokémon de la 9ème génération (ex : `Poussacha`)\n*Si rien de tout cela n'est vrai, veuillez contacter `Arlequiin#1853`*"))
@bot.command(description="Envoie les informations d'un Pokémon") 
async def dex(ctx,pokémon):
    try:
      pokemon=get_name(pokémon)
      infos=get_info(pokemon)
      if infos['type1']==infos['type2']:
        type_=type_to_emote[french_types[infos['type1'].replace("TYPE_",'').lower()]]
      else:
        type_=type_to_emote[french_types[infos['type1'].replace("TYPE_",'').lower()]]+' '+type_to_emote[french_types[infos['type2'].replace("TYPE_",'').lower()]]
      print(infos['ability'])
      ability=[get_ability(talent.replace(" ","")) for talent in infos["ability"].replace("{","").replace("}","").split(",")]
      if len(ability)!=3:
        ability.append("-------")
      print(ability)
      ability[2]+=" (Talent Caché)"
      final_ability=[]
      for i in range(len(ability)):
        if '----' in ability[i]:
          pass
        else:
          if ability[i] not in final_ability:
           final_ability.append(ability[i])
      print(final_ability)
      ability=', '.join(final_ability)
      embed = discord.Embed(title=f"{pokemon[1]}",description=f"__N°???__ (Nom 🇬🇧: {pokemon[0]})\n**Type(s)** : {type_}\n**Talents:** {ability}\n **Stats de base** :\nPV : {infos['hp']}\nAtq : {infos['atk']}\nDef : {infos['def']}\nAtq.Spé : {infos['sp.atk']}\nDef.Spé : {infos['sp.def']}\nVit : {infos['speed']}\n__**Localisation**__ : {loca[pokemon[1]]}",color=type_to_color[french_types[infos['type1'].replace("TYPE_",'').lower()]])
      print(f'https://raw.githubusercontent.com/Arlequiin/pokeemerald-expansion/master/graphics/pokemon/{pokemon[0].lower()}{pokemon[2]}/front.png')
      file = discord.File(removebg(f'https://raw.githubusercontent.com/Arlequiin/pokeemerald-expansion/master/graphics/pokemon/{pokemon[0].lower()}{pokemon[2]}/front.png'))  
      embed.set_thumbnail(url='attachment://temp.png')
      embed.set_author(name="Pokémon Résurrection")
      await ctx.respond(file=file, embed=embed)
    except Exception as e:
      print(e)
      await ctx.respond(embed=discord.Embed(title="❌ ERREUR",description="Vous avez :\n- Mal saisi le nom du Pokémon (ex : `Majspic` au lieu de `Majaspic`)\n - Vous avez saisi le nom d'un Pokémon de la 9ème génération (ex : `Poussacha`)\n*Si rien de tout cela n'est vrai, veuillez contacter `Arlequiin#1853`*"))
@bot.command(description="Information sur la rom") 
async def rom(ctx):
  embed=discord.Embed(title="Rom actuelle",description="La rom actuelle est la version **DEMO 1**\n - Télécharger la dernière version : https://ko-fi.com/s/73114f6144\n - Toutes les versions : https://arlequiin.github.io/resurrection/downloads \n - Jouer en ligne : https://resurrection.arlequiin.repl.co")
  embed.set_author(name="Pokémon Résurrection, 2020-2023")
  await ctx.respond(embed=embed)
keep_alive()
bot.run(os.getenv("TOKEN"))