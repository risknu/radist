from __future__ import annotations

import disnake
from disnake.ext import commands

import ollama

class OllamaAPI(commands.Cog):
    def __init__(self, bot: commands.Bot = None) -> None:
        self.bot: commands.Bot = bot
        
    @commands.slash_command(name="ask_ollama", description="Ask something from Ollama3")
    async def ask_ollama(self, inter: disnake.ApplicationCommandInteraction = None, ask_string_text: str = None) -> None:
        try:
            await inter.response.send_message(f'`> {ask_string_text}`\n```\nhmmmm, I need time to respond\n```')
            
            full_text_string: str = ''
            stream = ollama.chat(
                model="llama3",
                messages=[{'role': 'user', 'content': ask_string_text}],
                stream=True)

            for chunk in stream:
                full_text_string += chunk['message']['content']
                await inter.edit_original_response(content=f'`> {ask_string_text}`\n```\n{full_text_string}\n```')
        except Exception as e:
            print(f"An error occurred: {e}")

def setup(bot: commands.Bot) -> None:
    bot.add_cog(OllamaAPI(bot))
    