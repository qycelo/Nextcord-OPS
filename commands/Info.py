import nextcord
from nextcord.ext import commands

import config
from config import *


class Info(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{Info.__name__} is loaded')

    @nextcord.slash_command(
        name="info",
        description="Bot info",
        dm_permission=False,
        force_global=True,
    )
    async def info(self, interaction: nextcord.Interaction):
        info_embed = nextcord.Embed(
            title="Info",
            description=f"Bot info",
            color=EmbedColor
        )
        info_embed.add_field(
            name="Project Source",
            value=f"[Github](https://github.com/qycelo/nextcord-ops)",
            inline=True
        )
        info_embed.add_field(
            name="Version",
            value=f"{Version}",
            inline=True
        )
        info_embed.add_field(
            name="\u200b",
            value=f"\u200b"
        )
        info_embed.add_field(
            name="Contact",
            value=f"qycelo@proton.me",
            inline=True
        )
        info_embed.add_field(
            name="License",
            value="MIT License",
            inline=True
        )
        info_embed.set_author(name=f"Requested by {interaction.user}")
        info_embed.set_footer(text=EmbedFooter)

        await interaction.response.send_message(
            embed=info_embed,
            ephemeral=True
        )


def setup(bot):
    bot.add_cog(Info(bot))
