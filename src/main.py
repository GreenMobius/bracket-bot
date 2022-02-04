import os

import discord
from discord.ext import commands
import json

with open('config.json') as f:
    config_dict = json.load(f)

bot = commands.Bot(command_prefix='!')

@bot.command(name='ping')
async def ping(ctx):
    print(f'Received command ping')
    await ctx.send('pong')

bot.run(config_dict['token'])
