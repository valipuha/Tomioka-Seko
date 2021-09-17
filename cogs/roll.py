import discord
import random
from discord.ext import commands

class Roll(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def roll(self, ctx):
    n = random.randrange(1, 100)
    await ctx.send(n)

def setup(client):
  client.add_cog(Roll(client))