from rembg import remove
from PIL import Image
from pokemon import *
import urllib.request
import cv2
import re
import requests
#pip install git+https://github.com/Pycord-Development/pycord
def get_name(pokemon):
  pokemon=pokemon.lower()
  region=''
  if "de galar" in pokemon.lower():
    pokemon.replace(" de galar","")
    region="galarian/"
  if "d'Alola" in pokemon.lower():
    pokemon.replace(" d'alola","")
    region="alolan/"
  if "de Hisui" in pokemon.lower():
    pokemon.replace(" de hisui","")
    region="hisuian/"
  if pokemon.lower().capitalize() in data_en.keys():
   pokemon_fr=data_en[pokemon.lower().capitalize()]
   pokemon=pokemon.lower().capitalize()
  else:
   pokemon_fr=pokemon.lower().capitalize()
   pokemon=data_fr[pokemon.capitalize()]
  return [pokemon,pokemon_fr,region]
def get_front_sprite(pokemon):
      pokemon=get_name(pokemon)[0]
      url = f'https://raw.githubusercontent.com/Arlequiin/pokeemerald-expansion/master/graphics/pokemon/{pokemon.lower()}/front.png'
      with urllib.request.urlopen(url) as url:
          image_data = url.read()
      with open('temp.png', 'wb') as f:
          f.write(image_data)
      return "temp.png"

def get_data(pokemon):
    with open("temp_stats.h",'w') as f:
        f.write((requests.get('https://raw.githubusercontent.com/Arlequiin/pokeemerald-expansion/master/src/data/pokemon/base_stats.h')).text)
    with open("temp_stats.h",'r') as f:
        content=f.readlines()
        pokemon_data=[]
        in_pokemon_scope=False
        for row in content:
            if in_pokemon_scope:
                pokemon_data.append(row)
            if pokemon.upper() in row:
                in_pokemon_scope=True
            if in_pokemon_scope and '}' in row:
                in_pokemon_scope=False
    return pokemon_data
def get_info(pokemon):
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
        if ".type1" in row:
            stats['type1']=re.search("= (.*),",row).group(1)
        if ".type2" in row:
            stats['type2']=re.search("= (.*),",row).group(1)
        if ".catchRate" in row:
            stats['catch']=re.search("= (.*),",row).group(1)
        if ".abilities" in row:
            stats['ability']=re.search("= (.*),",row).group(1)
    return stats
def get_ability(ability):
    ability=ability.upper()
    with open("abilities.h",'w') as f:
        f.write((requests.get('https://raw.githubusercontent.com/Arlequiin/pokeemerald-expansion/master/src/data/text/abilities.h')).text)
    with open("abilities.h",'r') as f:
        content=f.readlines()
        for row in content:
            if ability.upper() in row:
                row=row.replace('''("''',"<").replace('''")''',">")
                french_ability=re.search("<(.*)>,",row).group(1)
                break
            else:
              french_ability="ERROR"
    return french_ability