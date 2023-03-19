from PIL import Image
from pokemon import *
import urllib.request
import re
import requests
#pip install git+https://github.com/Pycord-Development/pycord
def get_name(pokemon):
  pokemon=pokemon.lower()
  region=''
  if "de galar" in pokemon.lower():
    pokemon=pokemon.lower().replace(" de galar","")
    region="/galarian/"
  if "d'alola" in pokemon.lower():
    pokemon=pokemon.lower().replace(" d'alola","")
    region="/alolan/"
  if "de hisui" in pokemon.lower():
    pokemon=pokemon.lower().replace(" de hisui","")
    region="/hisuian/"
  if "mega-" in pokemon.lower().replace(" ","-").replace("é","e") and "charizard" not in pokemon.lower() and "mewtwo" not in pokemon.lower() and "dracaufeu" not in pokemon.lower():
    pokemon=pokemon.lower().replace("mega-","").replace("méga-","").replace("mega ",'').replace("méga ",'')
    region="/mega/"
  if pokemon.lower()=="sachanobi" or pokemon.lower()=="ash-greninja":
    pokemon="Amphinobi"
    region="/ash/"
  elif "mewtwo" in pokemon.lower() or "charizard" in pokemon.lower() or "dracaufeu" in pokemon.lower() and "mega" in pokemon.lower().replace("é","e"):
    if "y" in pokemon.lower():
      region="/mega_y/"
    elif "x" in pokemon.lower():
      region="/mega_x/"
    if "mewtwo" in pokemon.lower():
      pokemon="Mewtwo"
    else:
      pokemon="Dracaufeu"
  if pokemon.lower().capitalize() in data_en.keys():
   pokemon_fr=data_en[pokemon.lower().capitalize()]
   pokemon=pokemon.lower().capitalize()
  else:
   pokemon_fr=pokemon.lower().capitalize()
   pokemon=data_fr[pokemon.capitalize()]
  return [pokemon,pokemon_fr,region]
def get_image_from_link(url):
      with urllib.request.urlopen(url) as url:
          image_data = url.read()
      with open('data/temp.png', 'wb') as f:
          f.write(image_data)
      return "data/temp.png"

def get_data(pokemon):
    with open("data/temp_stats.h",'w') as f:
        f.write((requests.get('https://raw.githubusercontent.com/Arlequiin/resurrection/master/src/data/pokemon/species_info.h')).text)
    with open("data/temp_stats.h",'r') as f:
        content=f.readlines()
        pokemon_data=[]
        in_pokemon_scope=False
        for row in content:
            if in_pokemon_scope:
                if row in pokemon_data:
                  break
                else:
                 pokemon_data.append(row)
            if 'SPECIES_'+pokemon[0].upper()+']' in row:
              if pokemon[2]=='' and 'alola' not in row.lower() and 'galar' not in row.lower() and 'hisui' not in row.lower() and '_mega' not in row.lower() and '_ash' not in row.lower():
                in_pokemon_scope=True
              else:
                if pokemon[2].upper().replace("/","") in row:
                  in_pokemon_scope=True
            if in_pokemon_scope and 'noFlip' in row:
                in_pokemon_scope=False
    return pokemon_data
def get_info(pokemon):
    print(pokemon)
    rows=get_data(pokemon)
    stats={}
    for row in rows:
        if ".baseHP" in row:
            stats['hp']=re.search("= (.*),",row).group(1)
        if ".baseAttack" in row:
            stats['atk']=re.search("= (.*),",row).group(1)
        if ".baseDefense" in row:
            stats['def']=re.search("= (.*),",row).group(1)
        if ".baseSpAttack" in row:
            stats['sp.atk']=re.search("= (.*),",row).group(1)
        if ".baseSpDefense" in row:
            stats['sp.def']=re.search("= (.*),",row).group(1)
        if ".baseSpeed" in row:
            stats['speed']=re.search("= (.*),",row).group(1)
        if ".types" in row:
            row=row.replace("{ ","<").replace(" }",">").replace("}",">")
            row=re.search("<(.*)>",row).group(1)
            row=row.split(", ")
            stats['type1']=row[0]
            stats['type2']=row[1]
        if ".catchRate" in row:
            stats['catch']=re.search("= (.*),",row).group(1)
        if ".abilities" in row:
            print("CHECK "*8)
            stats['ability']=re.search("= (.*),",row).group(1)
    print(stats)
    return stats
def get_ability(ability):
    ability=ability.upper()
    with open("data/abilities.h",'w') as f:
        f.write((requests.get('https://raw.githubusercontent.com/Arlequiin/resurrection/master/src/data/text/abilities.h')).text)
    with open("data/abilities.h",'r') as f:
        content=f.readlines()
        for row in content:
            if ability.upper() in row:
                row=row.replace('''("''',"<").replace('''")''',">")
                french_ability=re.search("<(.*)>,",row).group(1)
                break
            else:
              french_ability="ERROR"
    return french_ability
def removebg(url):
    file=get_image_from_link(url)
    im = Image.open("data/temp.png")
    im = im.convert('RGBA')
    pixels = im.load()
    width, height = im.size
    t=pixels[0,0]
    for j in range(height):
        for i in range(width):
            if t[0]+30>pixels[i,j][0]>t[0]-30 and t[1]+30>pixels[i,j][1]>t[1]-30 and t[2]+30>pixels[i,j][2]>t[2]-30:
                pixels[i,j]=(0,0,0,0)
    im.save(file)
    return file
def get_learnset(pokemon):
    pokemon=get_name(pokemon)[0].lower().capitalize()
    with open("data/learnsets.h",'w') as f:
        f.write((requests.get('https://raw.githubusercontent.com/Arlequiin/resurrection/master/src/data/pokemon/level_up_learnsets.h')).text)
    with open("data/learnsets.h",'r') as f:
        content=f.readlines()
        learnset={}
        in_pokemon_scope=False
        for row in content:
            if pokemon+'Level' in row:
                in_pokemon_scope=True
            if in_pokemon_scope and 'LEVEL_UP_MOVE' in row:
                    in_pokemon_scope=True
                    prov_list=row.replace('LEVEL_UP_MOVE(','').replace('),','').split(",")
                    if prov_list[0].strip()=='0':
                      prov_list[0]='Évolution'
                    learnset[prov_list[0].strip()]=get_move_name(prov_list[1].strip())
            if in_pokemon_scope and '}' in row:
                in_pokemon_scope=False
                break
    return learnset
def get_move_name(moveId):
    with open("data/moves_names.h",'w') as f:
        f.write((requests.get('https://raw.githubusercontent.com/Arlequiin/resurrection/master/src/data/text/move_names.h')).text)
    with open("data/moves_names.h",'r') as f:
        content=f.readlines()
        names=[]
        for row in content:
            if moveId in row and 'Z_MOVE' not in row:
                result=re.search('<(.*)>',row.replace('''("''',"<").replace('''")''',">"))
                names.append(result.group(1))
    return names[0]
def capturable_percent():
    i=0
    j=0
    i2=0
    gens=[]
    for elem in loca.values():
        j+=1
        if elem!="*Localisation inconnue*":
            i+=1
            i2+=1
        if j in [151,252,386,494,649,721,810,898]:
            gens.append(i2)
            i2=0
    return [i/len(loca.values())*100,gens]