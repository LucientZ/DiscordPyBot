# Packages
import discord
from discord import app_commands
from discord.ext import commands
import time
from datetime import datetime

# Other Files
import datahandling as dt
from textfunctions import *
from helper import *


class aclient(discord.Client):
    def __init__(self):
        super().__init__(command_prefix = 's-', activity = discord.Game(name = "s-help"), intents=discord.Intents.all())
        choice = ""
        while choice.lower() != "y" and choice.lower() != "n":
            choice = input("Would you like to sync the bot? (Only do this if the bot has been updated or a command has changed) [Y/n] ")

        if choice.lower() == "y":
            self.synced = False
        else:
            self.synced = True

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            print(f"{cl.GREY}{cl.BOLD}{datetime.now()}{cl.BLUE} INFO{cl.END}    Awaiting command tree syncing...")
            a = time.time()
            await tree.sync()
            b = time.time()
            print(f"{cl.GREY}{cl.BOLD}{datetime.now()}{cl.BLUE} INFO{cl.END}    Tree Synced. Elapsed time: {int((b - a) * 100) / 100} seconds")
            self.synced = True
        print(f"I exist as '{self.user}' and can talk to people! :D")

    async def on_connect(self):
        print("I'm initializing myself :)")


client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name = "ping", description = "Responds and states client latency in milliseconds")
async def ping(ctx: discord.Interaction):
    await ctx.response.send_message(f"Pong!\nClient Latency: {int(client.latency * 1000)} ms")


def main():
    try:
        dt.init_guild_config()
        dt.init_file("textdata/copypasta.dat")
        TOKEN = dt.get_token(".token", "Logging In")
        client.run(TOKEN)
    except discord.LoginFailure as e:
        #This error is raised when the token is not valid
        print(f"{cl.RED}[ERROR] Issue logging into bot:{cl.BLUE}",e,f'{cl.END}\n')
        print(f"{cl.RED}The program will exit.{cl.END}\n")
        choice = input("Would you like to enter a new token? [Y/n] ")
        while(choice.lower() != "y" and choice.lower() != "n"):
            choice = input("\nWould you like to write a new token? [Y/n] ")    
        if(choice.lower() == "y"):
            TOKEN = input("Please enter bot token: ")
            dt.write_token(TOKEN, ".token")
        print("Terminating program...\n")
        exit()
    except Exception as e:
        print(f"{cl.RED}[ERROR] Issue logging into bot:{cl.BLUE}",e,f'{cl.END}\n')
        print("Terminating program...\n")
        exit()
        
if __name__ == '__main__':
    main()