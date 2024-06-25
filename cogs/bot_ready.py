from __future__ import annotations

import disnake
from disnake.ext import commands

from configuration import Conf


class BotReady(commands.Cog):
    def __init__(self, bot: commands.Bot = None) -> None:
        self.bot: commands.Bot = bot

    @commands.Cog.listener('on_ready')
    async def set_bot_status(self) -> None:
        if Conf.BOT_ACTIVITY_TYPE == "play":
            await self.bot.change_presence(activity=disnake.Game(
                name=Conf.BOT_ACTIVITY_STRING), status=Conf.BOT_STATUS)
        elif Conf.BOT_ACTIVITY_TYPE == "listen":
            await self.bot.change_presence(activity=disnake.Activity(
                type=disnake.ActivityType.listening,
                name=Conf.BOT_ACTIVITY_STRING), status=Conf.BOT_STATUS)
        elif Conf.BOT_ACTIVITY_TYPE == "watch":
            await self.bot.change_presence(activity=disnake.Activity(
                type=disnake.ActivityType.watching,
                name=Conf.BOT_ACTIVITY_STRING), status=Conf.BOT_STATUS)


def setup(bot: commands.Bot) -> None:
    bot.add_cog(BotReady(bot))
