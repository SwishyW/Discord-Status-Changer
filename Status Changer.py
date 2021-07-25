import discord
import colorama
import os
from colorama import Fore
from discord.ext import commands
################################################
token = input("Token: ")
prefix = input("Prefix: ")
tsu = ('https://www.twitch.tv/pokimane')
################################################
intents = discord.Intents.all()
client = discord.Client()
client = commands.Bot(command_prefix=prefix, self_bot=True, help_command=None, intents=intents)
################################################
os.system('cls')

@client.event
async def on_connect():
  print(f"""
{Fore.CYAN}Logged in as: {Fore.RED}{client.user.name}
{Fore.CYAN}Prefix: {Fore.RED}{prefix}
{Fore.RESET}------------------------------------------------------
{Fore.CYAN}{prefix}streaming <message> {Fore.BLUE}- {Fore.MAGENTA}Changes Status To Streaming
{Fore.CYAN}{prefix}listening <message> {Fore.BLUE}- {Fore.MAGENTA}Changes Status To Listening
{Fore.CYAN}{prefix}playing <message> {Fore.BLUE}- {Fore.MAGENTA}Changes Status To Playing
{Fore.CYAN}{prefix}watching <message> {Fore.BLUE}- {Fore.MAGENTA}Changes Status To Watching
{Fore.CYAN}{prefix}competing <message> {Fore.BLUE}- {Fore.MAGENTA}Changes Status To Competing In
{Fore.CYAN}{prefix}stop {Fore.BLUE}- {Fore.MAGENTA}Removes Status
{Fore.RESET}------------------------------------------------------
  """)

@client.command()
async def streaming(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(name=message, url=tsu)
    await client.change_presence(activity=stream)
    print(f"{Fore.GREEN}Streaming: {Fore.MAGENTA}{message}")

@client.command()
async def playing(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(name=message)
    await client.change_presence(activity=game)
    print(f"{Fore.GREEN}Playing: {Fore.MAGENTA}{message}")

@client.command()
async def listening(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=message))
    print(f"{Fore.GREEN}Listening To: {Fore.MAGENTA}{message}")    

@client.command()
async def watching(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=message))
    print(f"{Fore.GREEN}Watching: {Fore.MAGENTA}{message}")

@client.command()
async def competing(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Activity(type=5, name=message))
    print(f"{Fore.GREEN}Compeing In: {Fore.MAGENTA}{message}")


@client.command()
async def stop(ctx):
    await ctx.message.delete()
    await client.change_presence(activity=None, status=discord.Status.dnd)
    print(f"{Fore.RED}Removed Status")


client.run(token, bot=False)