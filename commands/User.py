import nextcord
from nextcord.ext import commands

import config
from config import *


class User(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{User.__name__} is loaded')

    @nextcord.slash_command(
        name="user",
        description="User info",
        dm_permission=False,
        force_global=True,
    )
    async def user(self, interaction: nextcord.Interaction,
                   user: nextcord.Member):
        user_embed = nextcord.Embed(
            title="User",
            description=f"User info",
            color=EmbedColor
        )
        user_embed.add_field(
            name="User",
            value=f"{user.name}",
            inline=False
        )
        user_embed.add_field(
            name="Created at",
            value=f"{user.created_at}",
            inline=True
        )
        user_embed.add_field(
            name="Joined at",
            value=f"{user.joined_at}"
        )
        user_embed.set_thumbnail(url=user.avatar.url)
        user_embed.set_author(name=f"Requested by {interaction.user}")
        user_embed.set_footer(text=EmbedFooter)

        await interaction.response.send_message(
            embed=user_embed,
            ephemeral=True
        )


def setup(bot):
    bot.add_cog(User(bot))
