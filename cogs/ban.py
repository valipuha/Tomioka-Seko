import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord import Member

class Ban(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member, *, reason=None):
          await member.ban(reason=reason)
          await ctx.send(f'🎆 **User {member} has been banned >:D**')

  @ban.error
  async def ban_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send("🦺 **You don't have permissions to ban this user!**")

def setup(client):
  client.add_cog(Ban(client))
    


