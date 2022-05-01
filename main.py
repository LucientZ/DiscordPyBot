import discord
from discord.ext import commands
import datahandling as dt
from textfunctions import *
from helper import colors as cl



client = commands.Bot(command_prefix = 's-', activity = discord.Game(name = "s-help"))

@client.event
async def on_connect():
    print('I exist!')

# Once the bot is ready, console commands are able to be used.
@client.event
async def on_ready():
    print('I can talk to friends now! :)')


# TODO add more functionality to this. Currently placeholder to not let improper commands print to console.
@client.event 
async def on_command_error(ctx, error): 
    if isinstance(error, commands.CommandNotFound): 
        pass


@client.event
async def on_message(ctx):
    # Bot doesn't respond to itself
    if ctx.author == client.user:
        return

    ctx_size = len(ctx.content)

    # These are funny responses to if a user happens to type a certain phrase.
    if 'sus' in ctx.content.lower():
        await ctx.channel.send("Amogus detected: " + format_msg(ctx.content, 'sus','***'))
        return

    if 'morbius' in ctx.content.lower():
        await ctx.channel.send(morbius())
        return

    if 'sad' in ctx.content.lower():
        await ctx.channel.send("https://cdn.discordapp.com/attachments/390692666897203211/970382349617483856/293.jpg")

    # Temporary request from a user. Will delete in future version
    if 'do' in ctx.content.lower()[ctx_size - 2:] or 'doing' in ctx.content.lower()[ctx_size - 5:] or 'doin' in ctx.content.lower()[ctx_size - 4:] or 'did' in ctx.content.lower()[ctx_size - 3:] or 'wyd' in ctx.content.lower()[ctx_size - 3:]:
        await ctx.channel.send("Your Mom")

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
        "echo": ">>> __**Description**__\nThis command makes the bot echo anything.\n\n__**Usage**__\ns-echo <sentence>",
        "funky": ">>> __**Description**__\nThis command gives an image of a fumo with the optional argument of a specific character\n\n__**Usage**__\ns-funky <optional name>\nexample: s-funky cirno",
        "boowomp": ">>> __**Description**__\nThis command sends sad spongebob.\n\n__**Usage**__\ns-boowomp <no arguments>"
    }

    if(not arg == ""):
        if arg.lower() in desc:
            await ctx.channel.send(desc[arg.lower()])
        else:
            await ctx.channel.send(arg,"is not a valid command. Type 's-help' for a list of commands.")
    else:
        await ctx.send(">>> __**Command List**__\necho\ncopypasta\nfunky\nboowomp\n\nType s-help command for more info on a command.")

@client.command()
async def echo(ctx, *, arg):
    await ctx.channel.send(arg)

@client.command()
async def copypasta(ctx):
    await ctx.channel.send(copypasta_text())

@client.command()
async def funky(ctx,arg = "null"):
    await ctx.channel.send(fumo(arg))

@client.command()
async def boowomp(ctx):
    await ctx.channel.send("https://cdn.discordapp.com/attachments/390692666897203211/970382349617483856/293.jpg")


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
