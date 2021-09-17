#bot startup
import discord
import os
import random
from discord.ext import commands
from webserver import keep_alive
from discord.ext import tasks



client = commands.Bot(command_prefix = 's.')

client.remove_command('help')

intents = discord.Intents.default()
intents.members = True


@client.event
async def on_ready():
    await client.wait_until_ready()
    change_presence.start()

@client.event
async def on_guild_join(guild):
    await chng_pr()

async def chng_pr():
    """Changes presences"""
    statuses = [f"s.help | {len(client.guilds)} servers", f"s.vote | {len(client.guilds)} servers", f"s.help | {len(client.guilds)} servers", f"!   𝐒𝐞𝐤𝐨ᵀᴾ#6592 my developer | {len(client.guilds)} servers"]

    status = random.choice(statuses)

    await client.change_presence(activity=discord.Game(status))


@tasks.loop(minutes=1)
async def change_presence():
    """Will loop every two minutes and change presences"""
    await chng_pr()


@client.event
async def on_ready():
    await client.wait_until_ready()
    # Starting the loop
    change_presence.start()


inital_extensions = []

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    inital_extensions.append("cogs." + filename[:-3])

if __name__ == '__main__':
  for extension in inital_extensions:
    client.load_extension(extension)


keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run('ODAwMDEzMTMxMTY2MTIxOTg0.YAL8SQ.EDUh8QdBhAyU9gLxkTp-3glpbxg')