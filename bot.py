from __future__ import annotations

import disnake
from disnake.ext import commands

from configuration import ENV
from os import listdir

intents: disnake.Intents = disnake.Intents.all()
bot: commands.Bot = commands.Bot(':', intents=intents)

for filename in listdir('./cogs'):
    if not filename.endswith('.py'):
        continue
    bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(ENV.TOKEN)
