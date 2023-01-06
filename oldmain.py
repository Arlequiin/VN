#encoding : utf-8
from PIL import Image, ImageDraw, ImageFont
import discord
from discord.ext import commands
import random
from discord.ext.commands import has_permissions, MissingPermissions
from discord import Permissions
from keep_alive import keep_alive
import pypokedex
from discord import utils
from discord import Webhook, RequestsWebhookAdapter, File
import requests
import re
from bs4 import BeautifulSoup
#-------------------------------------------------------------------------------
client = discord.Client()
bot = commands.Bot(command_prefix='-')



#-------------------------------------------------------------------------------
@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))
  

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  if any(word in msg for word in banwords):
    await msg.delete()
    await msg.channel.send('{} Votre message a été supprimé car il contient un mot banni.'.format(msg.author.mention))

  if any(word in msg for word in pub):
    await msg.delete()
    await msg.channel.send('{} Votre message a été supprimé car il contient une publicité.'.format(message.author.mention))



@bot.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

@bot.command()
async def pick(ctx, args):
  args = str(args)
  args = args.replace(" ","")
  numbers = args.split(',')
  final_number = random.choice(numbers)
  await ctx.send(f"{final_number} !")


@bot.command()
async def deco(ctx):
 await ctx.send("Bonne nuit.")
 await bot.change_presence(status=discord.Status.idle)

@bot.command(pass_context=True)
async def giverole(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    embed=discord.Embed(description=f"{user} a obtenu le rôle {role}")
    await ctx.send(embed=embed)
#-------------------------------------------------------------------------------
#Show Ranked



ctf = {'normal': 0xa5a5a7, 'feu': 0xd0361b, 'eau': 0x1b69d0, 'plante': 0x0a8017, 'électrik': 0xf0f401, 'fée': 0xdf89e1, 'roche': 0x744b25, 'sol': 0xab5707, 'dragon': 0x26077e, 'acier': 0x545454, 'combat': 0xd65d00, 'psy': 0xa238b7, 'glace': 0x84eef0, 'vol': 0xb8e0e0, 'poison': 0x5e0080, 'insecte': 0x6bb300, 'ténèbres': 0x333333, 'spectre': 0x3c0f61}
emotip = {'normal': '<:normal:893024570624339968>', 'feu': '<:feu:893024353757851671>', 'eau': '<:eau:893024109867454544>', 'plante': '<:plante:893024662651564032>', 'électrik': '<:electrik:893024179996217405>', 'fée': '<:fee:893024289014562827>', 'roche': '<:roche:893024894701424660>', 'sol': '<:sol:893024958261891112>', 'dragon': '<:dragon:893024038417481808>', 'acier': '<:acier:893023718786334740>', 'combat': '<:combat:893023954330071080>', 'psy': '<:psy:893024827160543232>', 'glace': '<:glace:893024431809638410>', 'vol': '<:vol:893025189183492106>', 'poison': '<:poison:893024728065925130>', 'insecte': '<:insecte:893024500302618645>', 'ténèbres': '<:tenebres:893025091804332043>', 'spectre': '<:spectr:893025024049577994>'}
@bot.command()
async def info(ctx,*,atk):
  
    from PIL import Image, ImageDraw, ImageFont
    import discord
    from discord.ext import commands
    import random
    from discord.ext.commands import has_permissions, MissingPermissions
    from discord import Permissions
    from keep_alive import keep_alive
    import pypokedex
    from discord import utils
    from discord import Webhook, RequestsWebhookAdapter, File
    import requests
    URL = f"https://www.pokepedia.fr/index.php?title={atk}&action=edit"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    a = str(soup.text)
    a = a.replace("| nom-en=","engname=").replace("| catégorie=","categorie=")
    result = re.search('engname=(.*)', a)
    print(result.group(1))
    engname = str(result.group(1))
    result = re.search('type=(.*)', a)
    print(result.group(1))
    atktype = str(result.group(1))
    result = re.search('categorie=(.*)', a)
    print(result.group(1))
    split = str(result.group(1)).replace("Spécial","<:special:910877171550158869>").replace("Physique","<:physique:910877545593995334>")
    result = re.search('précision=(.*)', a)
    print(result.group(1))
    prec = str(result.group(1))
    result = re.search('puissance=(.*)', a)
    print(result.group(1))
    puissance = str(result.group(1))
    result = re.search('pp=(.*)', a)
    print(result.group(1))
    pp = str(result.group(1))
    result = re.search('{{Générations|1|Effet}}\n(.*).', a)
    print(result.group(1))
    descri = str(result.group(1))
    atk=atk.replace("_","-")
    dicon = f"https://www.pokebip.com/pages/icones/objets/ct-{(atktype.lower())}.png".replace("é","e").replace("è","e")
    print(dicon)
    emotype = emotip[atktype.lower()]
    embed=discord.Embed(title=f":flag_fr: {atk.capitalize()} / :flag_gb:  {engname}",description=f"**Type :** {emotype}\n **Puiss :** {puissance}\n**Préci. :** {prec}\n**PP :** {pp}\n**Catégorie :** {split}\n{descri}",color=ctf[atktype.lower()])
    embed.set_thumbnail(url=dicon)
    await ctx.send(embed=embed)
    
    
  
    await ctx.send(embed=discord.Embed(title=":x: ERREUR",description="Vous avez :\n- Mal saisi le nom de l'attaque (ex : `Surfe` au lieu de `Surf`)\n- Saisi le nom en anglais ? (ex : `Tackle` au lieu de `Charge`)\n*Si rien de tout cela n'est vrai, veuillez contacter `Arlequiin#1853`"))



typesfr = {'normal': '<:normal:893024570624339968>', 'fire': '<:feu:893024353757851671>', 'water': '<:eau:893024109867454544>', 'grass': '<:plante:893024662651564032>', 'electric': '<:electrik:893024179996217405>', 'fairy': '<:fee:893024289014562827>', 'rock': '<:roche:893024894701424660>', 'ground': '<:sol:893024958261891112>', 'dragon': '<:dragon:893024038417481808>', 'steel': '<:acier:893023718786334740>', 'fighting': '<:combat:893023954330071080>', 'psychic': '<:psy:893024827160543232>', 'ice': '<:glace:893024431809638410>', 'flying': '<:vol:893025189183492106>', 'poison': '<:poison:893024728065925130>', 'bug': '<:insecte:893024500302618645>', 'dark': '<:tenebres:893025091804332043>', 'ghost': '<:spectr:893025024049577994>'}



@bot.command()
async def dex(ctx,nbr):
  modlist = ['Rattatac']
  import re
  import requests
  from bs4 import BeautifulSoup
  nbr = nbr.replace("'","%27")
  #Formes spécifiques
  URL = f"https://www.pokepedia.fr/{nbr}"
  gtr = {"démétéros":"landorus","boréas":"tornadus","fulguris":"thundurus","zacian":"zacian-hero","zacian-épée-suprême":"zacian-crowned","zamazenta":"zamazenta-hero","zamazenta-bouclier-suprême":"zamazenta-crowned"}

  
  if nbr.lower().replace("-totémique","").replace("-suprême","").replace("-bouclier","").replace("-épée","") in gtr.keys():
    if nbr.lower().endswith("-totémique") == True:
      bform = nbr.lower()[:-10]
      angname=gtr[bform]+"-therian"
      print(angname)
      p = pypokedex.get(name=gtr[bform]+"-incarnate")
      numerodex = p.dex
      p = pypokedex.get(name=angname)
    elif nbr.lower().startswith("zacian") == True or nbr.lower().startswith("zamazenta") == True:
      bform = nbr.lower().replace("-suprême","").replace("-épée","").replace("-bouclier","")
      print(bform)
      p = pypokedex.get(name=bform+"-hero")
      numerodex = p.dex
      if nbr.lower().endswith("-suprême"):
        angname = bform+"-crowned"
        print(angname)
        p = pypokedex.get(name=angname)
      else:
        angname = bform+"-hero"
        print(angname)
        p = pypokedex.get(name=angname)
      

    else:
      angname = gtr[nbr.lower()]+"-incarnate"
      print(angname)
      p = pypokedex.get(name=angname)
      numerodex = p.dex
  
  #Formes normales
  else:

    
  
    
      page = requests.get(URL)
      soup = BeautifulSoup(page.content, "html.parser")
      a = str(soup.text)

      result = re.search('Nom anglais(.*)Numéros', a)
      try:
        print(result.group(1))
      except:
        await ctx.send(embed=discord.Embed(title="ERREUR",description=":x: Votre commande ne peut pas être satisfaite.\nAvez vous :\n- Mal écrit le nom d'un Pokémon (ex: Pkiachu) ?\n- Ecrit le nom tout en minuscule/majuscule (ex: PIKACHU/pikachu au lieu de Pikachu) ?\n\nSi rien de tout cela est vrai, veuillez contacter `Arlequiin#1853`.",color=0xd0361b))
        return
      angname = result.group(1).replace(" ","-")
      if angname[0:7].lower() == "alolan-":
        angname = angname[7:]+"-alola"
      if angname[0:9].lower() == "galarian-":
        angname = angname[9:]+"-galar"
      
      print(angname)
      #Mega évolutions
      if angname[0:5].lower() == "mega-":
        print(angname[-1])
        if angname[-1] == "Y" or angname[-1]=="X":
          xystock = "-"+angname[-1]
        else:
          xystock = ""
        angnamefornum = angname[5:].replace("_","").replace("X","").replace("Y","").replace(" ","").replace("-","")
        print("FINAL: "+angnamefornum)
        p = pypokedex.get(name=angnamefornum)
        numerodex = p.dex
        angname = angname[5:].replace("_","").replace("X","").replace("Y","")
        angname = angnamefornum+"-Mega"+xystock
        angname = angname.replace("_","").replace(" ","")
        print(angname)
        p = pypokedex.get(name=angname)
      else:
        p = pypokedex.get(name=angname)
        numerodex = p.dex
      

    
    
      

  
  #Types / Couleurs
  type1 = p.types[0]
  print(p.types[0],"\t",type(p.types[0]))
  rg = nbr
  pt = p.types
  ct = {'normal': 0xa5a5a7, 'fire': 0xd0361b, 'water': 0x1b69d0, 'grass': 0x0a8017, 'electric': 0xf0f401, 'fairy': 0xdf89e1, 'rock': 0x744b25, 'ground': 0xab5707, 'dragon': 0x26077e, 'steel': 0x545454, 'fighting': 0xd65d00, 'psychic': 0xa238b7, 'ice': 0x84eef0, 'flying': 0xb8e0e0, 'poison': 0x5e0080, 'bug': 0x6bb300, 'dark': 0x333333, 'ghost': 0x3c0f61}
  ptfr = []
  #tradtypes
  while True:
    pt[0] = typesfr[pt[0]].capitalize()
    ptfr.append(pt[0])
    del(pt[0])
    if len(pt) == 0:
      break
  #Talents
  talent = str(p.abilities).replace("[","").replace("]","").replace("Ability","").replace("name=","").replace("'","").replace('is_hidden=False',"").replace("(","").replace("),","/").replace(")","").replace(",","").replace(" ","").replace("is_hidden=True"," (Talent caché)")

  talent = talent.split("/")
  print(talent)
  talentfr = []
  while True:
    if talent[0].endswith(" (Talent caché)")==True:
      datc = " (Talent caché)"
      talent[0] = talent[0].replace(" (Talent caché)","")
    else:
      datc = ""
    print(talent)
    URL = f"https://pokemondb.net/ability/{talent[0]}"
    del(talent[0])
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    
    a = str(soup.text)
    result = re.search("<th>French</th>\n<td>(.*)</td>", str(soup))
    fortc = str(result.group(1))+datc
    talentfr.append(fortc)
    if len(talent) == 0:
      break
  print(talentfr)
  talentfr = str(talentfr).replace("[","").replace("]","").replace("'"," ").replace(",","/")

  poketype = str(ptfr).replace("]","").replace("[","").replace(",","").replace("'","")
  (hp,attack,defense,sp_atk,sp_def,speed) = p.base_stats
  diff = 3-len(str(numerodex))
  dex000=diff*"0"+str(numerodex)
  if numerodex < 807:
    ig = f"https://www.serebii.net/pokedex-sm/icon/{dex000}.png"
  else:
    ig = f"https://www.serebii.net/pokedex-swsh/icon/{dex000}.png"


  #try
  
  #L'embed dex
  try:
    embed = discord.Embed(title=rg.replace("%27","'").replace("_"," "),description=f"__N°{numerodex}__ (Nom anglais: {p.name.capitalize()})\n**Type(s)** : {poketype}\n**Talents:** {talentfr}\n **Stats de base** :\nPV : {hp}\nAtq : {attack}\nDef : {defense}\nAtq.Spé : {sp_atk}\nDef.Spé : {sp_def}\nVit : {speed}",url=f"https://www.pokepedia.fr/{nbr}",color=ct[type1])
    embed.set_author(name=nbr.replace("%27","'").replace("_"," "),icon_url=ig)
    gens = f'https://play.pokemonshowdown.com/sprites/xyani/{p.name}.gif'
    

    embed.set_thumbnail(url=gens)
    await ctx.send(embed=embed)
  except:
    await ctx.send(embed=discord.Embed(title="ERREUR",description=":x: Le programme a rencontré une exception non gérée, veuillez contacter  `Arlequiin#1853`.",color=0xd0361b))





@bot.command()
async def natures(ctx):
  await ctx.send("https://media.discordapp.net/attachments/887779591513595926/890185594494406686/unknown.png")
@bot.command()
async def engnatures(ctx):
  await ctx.send("https://qph.fs.quoracdn.net/main-qimg-544b2344f3092b3ba0d8beaeab970a7a")


#-------------------------------------------------------------------------------
#setup

@bot.command()
async def sprite(ctx,poke,gen,pos):
  d = {"5":"black-white","1":"red-blue","2":"silver","HGSS":"heartgold-soulsilver","EM":"emerald","FRLG":"firered-leafgreen","Yellow":"yellow","3":"ruby-sapphire","Platine":"platinum","4":"diamond-pearl"}
  posi = {"front":"normal","back":"back-normal","front-shiny":"shiny","back-shiny":"back-shiny","front-colorisé":"normal","back-colorisé":"back-normal"}
  if d[gen] == "black-white":
    anim = "/anim"
    ext = "gif"
  if posi[pos] == "front-colorisé" or posi[pos] == "back-colorisé":
    color = "-color"
  else:
    anim = ""
    ext = "png"
    color = ""
  await ctx.send(f"https://img.pokemondb.net/sprites/{d[gen]}{anim}/{posi[pos]}/{poke}{color}.{ext}")


@bot.command()
async def wiki(ctx,poke):
 import wikipedia
 wiki = wikipedia.page('{}'.format(poke))
 text = str(wiki.content).replace("é","\e")

 first_chars = text[0:4000]

 embed=discord.Embed(title=f"{len(first_chars)} caractères",description=first_chars)
 await ctx.send(embed=embed)

@bot.command()
async def webscrap(ctx,poke):
  import requests
  from bs4 import BeautifulSoup
  URL = f"{poke}"
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  a = str(soup.text)[0:4000]
  print(a)
  embed=discord.Embed(title=f"{len(a)} caractères",description=f"{a}")
  await ctx.send(embed=embed)
  print(a)

@bot.command()
async def desc(ctx,poke):
  import re
  import requests
  from bs4 import BeautifulSoup
  pokemon = poke
  URL = f"https://pokemondb.net/pokedex/{pokemon}"
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  a = str(soup)
  result = re.search('<th>French</th>\n<td>(.*)</td>', a)
  pokefr = str(result.group(1))
  await ctx.send("Nom français : "+result.group(1))

  URL = f"https://www.pokebip.com/pokedex/pokemon/{pokefr}"
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  a = str(soup)


  result = re.search('</div>\n<div class="panel panel-info">\n<div class="panel-heading">X</div>\n<div class="panel-body">(.*)</div>', a)
  description = str(result.group(1))
  print(result.group(1))
  print("-"*10)

  #ajout des \n

  pick = "    "+'''"'''+description[0:40]+'''/n"'''
  pick2 = "\n    "+'''"'''+description[40:80]+'''/n"'''
  pick3 = "\n    "+'''"'''+description[80:120]+'''");'''


  if pick[-4] != " ":
    if pick2[6] != " ":
     pick = pick[:-3]+'''-/n"'''
  if pick2[:-4] != " ":
    if pick3[6] != " ":
     pick2 = pick2[:-3]+'''-/n"'''


  forcode = f"const u8 g{pokemon.capitalize()}PokedexText[] = _(\n{pick}{pick2}{pick3}"
  await ctx.send("```c\n"+forcode+"```")


keep_alive()
#bot.run("")