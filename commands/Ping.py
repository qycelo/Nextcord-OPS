import nextcord
from nextcord.ext import commands

from config import *


class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{Ping.__name__} is loaded')

    @nextcord.slash_command(
        name="ping",
        description="Bot Latency",
        dm_permission=False,
        force_global=True,
    )
    async def ping(self, interaction: nextcord.Interaction):
        ping_embed = nextcord.Embed(
            title="Pong :ping_pong:",
            description=f"Ping is `{round(self.bot.latency * 1000)}ms`!",
            color=EmbedColor
        )
        ping_embed.set_author(name=f"Requested by {interaction.user}")
        ping_embed.set_footer(text=EmbedFooter)

        await interaction.response.send_message(
            embed=ping_embed,
            ephemeral=True
        )


def setup(bot):
    bot.add_cog(Ping(bot))
