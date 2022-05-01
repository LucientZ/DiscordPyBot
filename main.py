import discord
from discord.ext import commands
import datahandling as dt
from textfunctions import *
from helper import colors as cl

client = commands.Bot(command_prefix = 's-')

@client.event
async def on_connect():
    print('I exist!')

# Once the bot is ready, console commands are able to be used.
@client.event
async def on_ready():
    print('I can talk to friends now! :)')


@client.event
async def on_message(ctx):
    # Bot doesn't respond to itself
    if ctx.author == client.user:
        return

    # These are funny responses to if a user happens to type a certain phrase.
    if 'sus' in ctx.content.lower():
        await ctx.channel.send("Amogus detected: " + format_msg(ctx.content, 'sus','***'))
        return

    if 'morbius' in ctx.content.lower():
        await ctx.channel.send(morbius())
        return

    # Note: Since on_message() overrides what the bot does to during a message send, this process the message as a command.
    try:
        await client.process_commands(ctx)
    except:
        pass


##################
#Commands Section#
##################

# Since help is a default command, remove to create a custom version
client.remove_command("help")
@client.command()
async def help(ctx, arg = ""):
    # Dictionary used for descriptions of every command
    desc = {
        "copypasta": ">>> __**Description**__\nThis command makes the bot say a random copypasta from a list.\n\n__**Usage**__\ns-copypasta <no arguments>",
        "echo": ">>> __**Description**__\nThis command makes the bot echo anything.\n\n__**Usage**__\ns-echo <sentence>"
    }

    if(not arg == ""):
        if arg.lower() in desc:
            await ctx.channel.send(desc[arg.lower()])
        else:
            await ctx.channel.send(arg,"is not a valid command. Type 's-help' for a list of commands.")
    else:
        # TODO - Add text for help command
        await ctx.channel.send("Temporary")

@client.command()
async def echo(ctx, *, arg):
    await ctx.channel.send(arg)

@client.command()
async def copypasta(ctx):
    await ctx.channel.send(copypasta_text())






# Login information for the bot requires a token.
# token is taken from a file named '.token'
# If this file does not exist, user will be prompted to input token

# Current bad token handling: Ask for new TOKEN -> write TOKEN to .token -> crash program

def main():
    try:
        TOKEN = dt.get_token()
        client.run(TOKEN)

    except discord.LoginFailure as e:
        #This error is raised when the token is not valid
        print(f"{cl.RED}[ERROR] Issue logging into bot:{cl.BLUE}",e,f'{cl.END}\n')
        print(f"{cl.RED}The program will exit.{cl.END}\n")
        choice = input("Would you like to enter a new token? [Y/n] ")
        while(choice != "Y" and choice != "n"):
            choice = input("\nWould you like to write a new token? [Y/n] ")    
        if(choice == "Y"):
            TOKEN = input("Please enter bot token: ")
            dt.write_token(TOKEN)
        print("Terminating program...\n")
        exit()
    except Exception as e:
        print(f"{cl.RED}[ERROR] Issue logging into bot:{cl.BLUE}",e,f'{cl.END}\n')
        print("Terminating program...\n")
        exit()

if __name__ == '__main__':
    main()
