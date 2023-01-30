from keep_alive import keep_alive
import os
os.system("pip install py-cord==2.3.2")
import discord
from pokemon import *
from PIL import Image
import os
from code import *

bot = discord.Bot()
@bot.event
async def on_ready():
  game = discord.Game("Pokémon Résurrection")
  await bot.change_presence(status=discord.Status.online, activity=game)
#bot.change_presence(activity=discord.Game(name="Pokémon Résurrection"))
##############################################################################################
badwords=['pute','connasse','connard','connard','nique ta']
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if '793941611418615829' in message.content:
      await message.add_reaction("<:pikapinged:842052761645613056>")

      
    if any(badword in message.content.lower() for badword in badwords):
          await message.channel.send('Gros mot!')
##############################################################################################
@bot.command(description="Envoie la latence du bot") 
async def ping(ctx):
  await ctx.respond(f"Pong! {bot.latency}")
##############################################################################################
@bot.command(description="Envoie le pourcentage du Pokédex que vous pouvez compléter actuellement") 
async def dexstat(ctx):
  stat=capturable_percent()
  await ctx.respond(embed=discord.Embed(title="Pokédex",description=f"**Le Pokédex peut actuellement être complété à {round(stat[0],2)}%**\n__Kanto__ : {stat[1][0]}/151\n__Johto__ : {stat[1][1]}/100\n__Hoenn__ : {stat[1][2]}/135\n __Sinnoh__ : {stat[1][3]}/107\n__Unys__ : {stat[1][4]}/156\n__Kalos__ : {stat[1][5]}/72\n__Alola__ : {stat[1][6]}/88\n__Galar__ : {stat[1][7]}/96",color=0xd0361b))
##############################################################################################
@bot.command(description="Envoie le sprite d'un Pokémon") 
async def sprite(ctx,pokémon):
    try:
      await ctx.respond(file=discord.File(get_front_sprite(pokémon)))
    except:
      await ctx.respond(embed=discord.Embed(title="❌ ERREUR",description="Vous avez :\n- Mal saisi le nom du Pokémon (ex : `Majspic` au lieu de `Majaspic`)\n- Vous avez saisi le nom d'un Pokémon de la 9ème génération (ex : `Poussacha`)\n*Si rien de tout cela n'est vrai, veuillez contacter `Arlequiin#1853`*"))


##############################################################################################
@bot.command(description="Envoie les informations d'un Pokémon") 
async def dex(ctx,pokémon):
    msg=await ctx.respond(embed=discord.Embed(title="Veuillez Patienter :clock:",description="Votre commande est en cours de traitement, cela peut prendre jusqu'à 5 secondes."))
    #msg=msg.id
    #channel = ctx.channel
    #msg = await channel.fetch_message(msg)
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
      dico=get_learnset(pokemon[0])
      embed_content=''
      for i in range(len(dico)):
       embed_content+=list(dico.keys())[i]+' : '+list(dico.values())[i]+'\n'
      sumbs=sum(int(e) for e in [infos['hp'],infos['atk'],infos['def'],infos['sp.atk'],infos['sp.def'],infos['speed']])
      embed = discord.Embed(title=f"{pokemon[1]}",description=f"__N°{list(loca.keys()).index(pokemon[1])+1}__ (Nom 🇬🇧: {pokemon[0]})\n__**Type(s)**__ : {type_}\n__**Talents:**__ {ability}\n __**Stats de base**__ :\nPV : {infos['hp']}\nAtq : {infos['atk']}\nDef : {infos['def']}\nAtq.Spé : {infos['sp.atk']}\nDef.Spé : {infos['sp.def']}\nVit : {infos['speed']}\nBS : {sumbs}\n__**Learnset**__\n{embed_content}\n__**Localisation**__ : {loca[pokemon[1]]}",color=type_to_color[french_types[infos['type1'].replace("TYPE_",'').lower()]])
      print(f'https://raw.githubusercontent.com/Arlequiin/pokeemerald-expansion/master/graphics/pokemon/{pokemon[0].lower()}{pokemon[2]}/front.png')
      file = discord.File(removebg(f'https://raw.githubusercontent.com/Arlequiin/pokeemerald-expansion/master/graphics/pokemon/{pokemon[0].lower()}{pokemon[2]}/front.png'))  
      embed.set_thumbnail(url='attachment://temp.png')
      embed.set_author(name="Pokémon Résurrection")
      await msg.edit_original_response(file=file, embed=embed)
    #-------------------------------------------
    except Exception as e:
      print(e)
      await msg.edit_original_response(embed=discord.Embed(title="❌ ERREUR",description="Vous avez :\n- Mal saisi le nom du Pokémon (ex : `Majspic` au lieu de `Majaspic`)\n - Vous avez saisi le nom d'un Pokémon de la 9ème génération (ex : `Poussacha`)\n*Si rien de tout cela n'est vrai, veuillez contacter `Arlequiin#1853`*"))
##############################################################################################
@bot.command(description="Information sur la rom") 
async def rom(ctx):
  embed=discord.Embed(title="Rom actuelle",description="La rom actuelle est la version **DEMO 1.2**\n - Télécharger la dernière version : https://ko-fi.com/s/73114f6144\n - Toutes les versions : https://arlequiin.github.io/resurrection/downloads.html \n - Jouer en ligne : https://resurrection.arlequiin.repl.co")
  embed.set_author(name="Pokémon Résurrection, 2020-2023")
  await ctx.respond(embed=embed)
##############################################################################################
while __name__ == '__main__':
  try:
    keep_alive()
    bot.run(os.getenv("TOKEN"))
  except:
    print("API DISCORD DE MERDE!!!! RESTART")
    os.system('kill 1')