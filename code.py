from PIL import Image
from pokemon import *
import urllib.request
from removebg import RemoveBg
def get_front_sprite(pokemon):
      if pokemon in data_en.keys():
        pass
      else:
        pokemon=data_fr[pokemon.capitalize()]
      url = f'https://raw.githubusercontent.com/Arlequiin/pokeemerald-expansion/master/graphics/pokemon/{pokemon.lower()}/front.png'
      with urllib.request.urlopen(url) as url:
          image_data = url.read()
      with open('temp.png', 'wb') as f:
          f.write(image_data)
      input = Image.open('temp.png')
      rmbg = RemoveBg("YOUR-API-KEY", "error.log")
      rmbg.remove_background_from_img_file("temp.png")
      output.save("temp.png")
      return "temp.png"