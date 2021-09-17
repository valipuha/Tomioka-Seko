import discord
import random
from discord.ext import commands

class Coinflip(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def coinflip(self, ctx):
    n = random.randint(0, 1)
    await ctx.send("🌠 **Heads**" if n == 1 else "☄ **Tails**")

def setup(client):
  client.add_cog(Coinflip(client))