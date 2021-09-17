import discord
from discord.ext import commands


class Clear(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def clear(self, ctx, amount=100):
    await ctx.channel.purge(limit=amount)
    await ctx.send("👔 **Cleared**")


 
def setup(client):
  client.add_cog(Clear(client))