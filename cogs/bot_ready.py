from __future__ import annotations

import disnake
from disnake.ext import commands

from configuration import configuration

class bot_ready(commands.Cog):
    def __init__(self, bot: commands.Bot = None) -> None:
        self.bot: commands.Bot = bot

    @commands.Cog.listener('on_ready')
    async def set_bot_status(self) -> None:
        await self.bot.change_presence(activity=disnake.Activity(
            type=disnake.ActivityType.watching,
            name=configuration.BOT_ACTIVITY_STRING), status=configuration.BOT_STATUS)

def setup(bot: commands.Bot) -> None:
    bot.add_cog(bot_ready(bot))
