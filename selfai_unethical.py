import subprocess
import time
import discord
from discord.ext import commands

TOKEN = ""
PREFIX = ">"



intents = discord.Intents.all()
client = commands.Bot(command_prefix=PREFIX, self_bot=True, intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name} ({client.user.id})")


@client.command()
async def ai(ctx, *, prompt: str):
    await ctx.message.delete()

    cock = subprocess.run(["ollama", "run", "llama2-uncensored:7b-chat-q8_0", prompt], capture_output=True, text=True, encoding='utf-8', shell=True) 


    preresult = cock.stdout

    result = preresult.replace("failed to get console mode for stdout: The handle is invalid.\n", "") \
                        .replace("failed to get console mode for stderr: The handle is invalid.\n", "")
    
    
    user = str(client.user.id)
    # await ctx.send(f"<@{user}>" + result) -- if you wanna @them
    await ctx.send(result)


client.run(TOKEN, bot=False)


