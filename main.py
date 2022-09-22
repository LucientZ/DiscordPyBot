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
        super().__init__(activity = discord.Game(name = "s-help"), intents=discord.Intents.all())

        # Asks user if global sync for commands should occur
        choice = ""
        while choice.lower() != "y" and choice.lower() != "n":
            choice = input("Would you like to sync the bot globally? (Only do this if the bot has been updated or a command has changed) [Y/n] ")

        if choice.lower() == "y":
            self.synced = False
        else:
            self.synced = True

    async def on_ready(self):
        await self.wait_until_ready()

        # Once the bot is ready, will attempt to sync commands globally
        if not self.synced:
            print(f"{cl.GREY}{cl.BOLD}{str(datetime.now())[:-7]}{cl.BLUE} INFO{cl.END}     Awaiting command tree syncing...")
            a = time.time()
            # Syncs command tree globally
            await tree.sync()
            b = time.time()
            print(f"{cl.GREY}{cl.BOLD}{str(datetime.now())[:-7]}{cl.BLUE} INFO{cl.END}     Tree Synced. Elapsed time: {int((b - a) * 100) / 100} seconds")
            self.synced = True
        print(f"I exist as '{self.user}' and can talk to people! :D")

    async def on_connect(self):
        print("I'm initializing myself :)")

    async def on_message(self, ctx: discord.Interaction):
        # Bot doesn't respond to itself
        # Protection for if a message parsed by the bot is too long.
        ctx_size = len(ctx.content)
        if ctx.author.bot or ctx_size > 1500:
            return

        # Current response in DMs is simply to say "Hello"
        if isinstance(ctx.channel, discord.channel.DMChannel):
            await ctx.channel.send("Hello")
        # Checks if the first two characters of the message starts with 's-' to either parse message as command or regular message
        elif(not ctx.content.lower()[0:2] == "s-"):
            if 'sus' in ctx.content.lower() and not dt.is_blacklisted("sus", str(ctx.guild.id), str(ctx.channel.id)):
                if(not ctx_size > 665):
                    await ctx.channel.send("Amogus detected: " + format_msg(ctx.content, 'sus','**'))
                else:
                    await ctx.channel.send("__Amogus Detected in Message__")
                    await ctx.channel.send(ctx.content)
            elif 'morb' in ctx.content.lower() and not dt.is_blacklisted("morbius", str(ctx.guild.id), str(ctx.channel.id)):
                await ctx.channel.send(morbius())
            elif 'sad' in ctx.content.lower() and not dt.is_blacklisted("sad", str(ctx.guild.id), str(ctx.channel.id)):
                await ctx.channel.send("https://cdn.discordapp.com/attachments/390692666897203211/970382349617483856/293.jpg")
            elif 'trade' in ctx.content.lower() and not dt.is_blacklisted("trade", str(ctx.guild.id), str(ctx.channel.id)):
                await ctx.channel.send("yeah i trade :smile:")
            elif (('do' in ctx.content.lower()[ctx_size - 2:] or 'doing' in ctx.content.lower()[ctx_size - 5:] or 'doin' in ctx.content.lower()[ctx_size - 4:] or 'did' in ctx.content.lower()[ctx_size - 3:] or 'wyd' in ctx.content.lower()[ctx_size - 3:]) or ('do?' in ctx.content.lower()[ctx_size - 3:] or 'doing?' in ctx.content.lower()[ctx_size - 6:] or 'doin?' in ctx.content.lower()[ctx_size - 5:] or 'did?' in ctx.content.lower()[ctx_size - 4:] or 'wyd?' in ctx.content.lower()[ctx_size - 4:])) and not dt.is_blacklisted("mom", str(ctx.guild.id), str(ctx.channel.id)):
                await ctx.channel.send(mom())


client = aclient()
tree = app_commands.CommandTree(client)

@tree.error
async def on_app_command_error(ctx: discord.Interaction, error: discord.app_commands.AppCommandError):
    """
    Handles errors on the bot's command tree.
    """
    # If the command doesn't exist, then the most likely culprit is due to a command being synced globally and then ceasing to exist and the bot informs the user. 
    # Otherwise, give a generic response for the user to file a bug report.
    if isinstance(error, discord.app_commands.errors.CommandNotFound):
        print(f"{cl.GREY}{cl.BOLD}{str(datetime.now())[:-7]}{cl.RED} ERROR{cl.END}     Ignoring error in command tree:", error)
        await ctx.response.send_message(f"The command you just tried using doesn't seem to exist. This is either due to a global sync issue or my developer was too lazy to fix it. :dolphin::dolphin::dolphin:\n\nTo report an issue, please go to <https://github.com/LucientZ/DiscordPyBot>", ephemeral = True)
    else:
        print(f"{cl.GREY}{cl.BOLD}{str(datetime.now())[:-7]}{cl.RED} ERROR{cl.END}     An error occurred in command tree. Ignoring for now:", error)
        await ctx.response.send_message(f"An error occurred while trying to process a command. If this is unexpected, please file an issue report at <https://github.com/LucientZ/DiscordPyBot>", ephemeral = True)




@tree.command(name = "ping", description = "Responds and states client latency in milliseconds")
async def ping(ctx: discord.Interaction):
    """
    Makes the bot respond to the user and reply with the client latency in ms
    """
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