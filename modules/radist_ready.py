from __future__ import annotations

import disnake
from disnake.ext import commands

class radist_ready(commands.Cog):
    def __init__(self, bot: commands.Bot, /) -> None:
        self._bot: commands.Bot = bot

    @commands.Cog.listener('on_ready')
    async def set_bot_status(self, /) -> None:
        await self._bot.change_presence(activity=disnake.Activity(
            type=disnake.ActivityType.watching, name="r/radist"), status=disnake.Status.online)
        return None

def setup(bot: commands.Bot) -> None:
    bot.add_cog(radist_ready(bot))
