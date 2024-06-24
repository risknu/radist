from __future__ import annotations

import disnake
from disnake.ext import commands

from ollama import AsyncClient

class OllamaAPI(commands.Cog):
    def __init__(self, bot: commands.Bot = None) -> None:
        self.bot: commands.Bot = bot
        
    async def ollama_search(self, ask_string_text: str = None) -> None:
        if ask_string_text is None:
            return ""
        return await AsyncClient().chat(model='llama3', messages=[{'role': 'user', 'content': ask_string_text}], stream=True)
    
    async def create_editable_interaction_message(self, inter: disnake.ApplicationCommandInteraction = None, ask_string_text: str = None) -> None:
        await inter.response.send_message(f'```\nhmmmm, I need time to respond\n```')
        
        full_text_string: str = ''
        stream = await self.ollama_search(ask_string_text)

        async for chunk in stream:
            full_text_string += chunk['message']['content']
            await inter.edit_original_response(content=f'```\n{full_text_string}\n```')
            
    async def create_editable_message(self, ctx: disnake.Message = None, ask_string_text: str = None) -> None:
        message: disnake.Message = await ctx.reply(f'```\nhmmmm, I need time to respond\n```')
        
        full_text_string: str = ''
        stream = await self.ollama_search(ask_string_text)

        async for chunk in stream:
            full_text_string += chunk['message']['content']
            await message.edit(content=f'```\n{full_text_string}\n```')
        
    @commands.Cog.listener("on_message")
    async def ask_ollama_reply(self, ctx: disnake.Message = None) -> None:
        if self.bot.user.mentioned_in(ctx) and not ctx.author.bot:
            await self.create_editable_message(ctx, ctx.content)
            return None
            
        if ctx.reference:
            replied_message: disnake.Message = await ctx.channel.fetch_message(ctx.reference.message_id)
            if replied_message.author == self.bot.user:
                await self.create_editable_message(ctx, ctx.content)
        
    @commands.slash_command(name="ask_ollama", description="Ask something from Ollama3")
    async def ask_ollama_slash(self, inter: disnake.ApplicationCommandInteraction = None, ask_string_text: str = None) -> None:
        try:
            await self.create_editable_interaction_message(inter, ask_string_text)
        except Exception as e:
            print(f"An error occurred: {e}")

def setup(bot: commands.Bot) -> None:
    bot.add_cog(OllamaAPI(bot))
    