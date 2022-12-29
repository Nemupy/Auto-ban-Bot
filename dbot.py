import discord
import json
import os


with open("config.json", "r") as f:
    config = json.load(f)

token = os.environ["token"]

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"{client.user} is online")


@client.event
async def on_member_join(member):
    if str(member.id) in config["users"]:
        await member.ban(reason=f"Auto-ban by {client.user}")
        await member.guild.system_channel.send(f"<@{member.id}> was banned by <@{client.user.id}>")

client.run(token)
