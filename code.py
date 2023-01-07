from rembg import remove
from PIL import Image
from pokemon import *
import urllib.request
import cv2
import re
#pip install git+https://github.com/Pycord-Development/pycord
def pokemon_name(pokemon):
  if pokemon in data_en.keys():
   pass
  else:
   pokemon=data_fr[pokemon.capitalize()]
  return pokemon
def get_front_sprite(pokemon):
      pokemon=pokemon_name(pokemon)
      url = f'https://raw.githubusercontent.com/Arlequiin/pokeemerald-expansion/master/graphics/pokemon/{pokemon.lower()}/front.png'
      with urllib.request.urlopen(url) as url:
          image_data = url.read()
      with open('temp.png', 'wb') as f:
          f.write(image_data)
      return "temp.png"

def get_data(pokemon):
    import requests
    with open("temp_stats.h",'w') as f:
        f.write((requests.get('https://raw.githubusercontent.com/Arlequiin/pokeemerald-expansion/master/src/data/pokemon/base_stats.h')).text)
    with open("temp_stats.h",'r') as f:
        content=f.readlines()
        pokemon_data=[]
        in_pokemon_scope=False
        for row in content:
            if in_pokemon_scope:
                print(row)
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
  