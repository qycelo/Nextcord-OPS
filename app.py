import nextcord
from nextcord.ext import commands
import os

from config import *

qyc = commands.Bot()


@qyc.event
async def on_ready():
    print(f"{qyc.user} is online")
    activity = nextcord.Game(name=Game)
    await qyc.change_presence(status=nextcord.Status.online, activity=activity)

for filename in os.listdir("./commands"):
    if filename.endswith(".py"):
        qyc.load_extension(f"commands.{filename[:-3]}")


qyc.run(BoToken)
