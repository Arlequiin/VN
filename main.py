from keep_alive import keep_alive
import discord
import os # default module
from dotenv import load_dotenv
from pokemon import *
from PIL import Image
import urllib.request
import numpy as np

bot = discord.Bot()
@bot.command(description="Envoie la latence du bot") 
async def ping(ctx):
    await ctx.respond(f"Pong! {bot.latency}")
@bot.command(description="Envoie le sprite d'un Pokémon") 
async def sprite(ctx,pokemon):
    if pokemon in data_en.keys():
      pass
    else:
      pokemon=data_fr[pokemon.capitalize()]
    url = f'https://raw.githubusercontent.com/Arlequiin/pokeemerald-expansion/master/graphics/pokemon/{pokemon.lower()}/front.png'
    with urllib.request.urlopen(url) as url:
        image_data = url.read()
    with open('temp.png', 'wb') as f:
        f.write(image_data)
    im = Image.open('temp.png')
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    image_data = np.array(im)
    mask = (image_data[:, :, 3] < 255)
    image_data[mask] = (0, 0, 0, 0)
    im = Image.fromarray(image_data)
    im.save('image_with_transparency.png')
    await ctx.send(file=discord.File('image_with_transparency.png'))
keep_alive()
bot.run(os.getenv("TOKEN"))