import discord
from discord.ext import commands
from base import lista
import random
from conections import conection

token = 'NzEwOTA4NDY3MjkxODgxNTcz.XssL5g.YjIuGTzyt8p1cI7_nKzH178Khm8'
bot = commands.Bot(command_prefix= '-')

@bot.event
async def on_ready():
    print ('Hola bienvenidos a la grieta del invoacador')

@bot.command()
async def meme(ctx):
    respuesta = conection()
    embed = discord.Embed(title='')
    embed.set_image(url=random.choice(respuesta))#random.choice(lista))
    await ctx.send(embed = embed)

#@bot.event
#async def on_message(message):
#    autor = message.autor
#    content = message.content
#    await bot.send_message(message.channel, content='{}:{}'.format(autor,content))
bot.run(token)