import discord
from discord.ext import commands
import colorama
from colorama import Fore
colorama.init()

zug = commands.Bot(command_prefix = ".")

@zug.event # Bot Starts
async def on_ready():
    print(f"{Fore.GREEN}Bot is online{Fore.RESET}")

@zug.event # Member Join

            #Reset Token After Video
zug.run("NzE3OTY5NTc2NjYyNDAxMDc0.XtnicQ.c2_FhL2HPNOz4CegK30JcsF4iJk")