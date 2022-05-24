import discord
from discord.ext import commands
import datahandling as dt
from textfunctions import *
from helper import *



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
    # Protection for if a message parsed by the bot is too long.
    # Discord messages may only be under 2000 characters long
    if(ctx_size > 1500):
        return

    # These are funny responses to if a user happens to type a certain phrase.
    if(not ctx.content.lower()[0:2] == "s-"):
        if 'sus' in ctx.content.lower():
            if(not ctx_size > 665):
                await ctx.channel.send("Amogus detected: " + format_msg(ctx.content, 'sus','**'))
                return
            else:
                await ctx.channel.send("__Amogus Detected in Message__")
                await ctx.channel.send(ctx.content)
                return
            

        if 'morbius' in ctx.content.lower():
            await ctx.channel.send(morbius())
            return

        if 'sad' in ctx.content.lower():
            await ctx.channel.send("https://cdn.discordapp.com/attachments/390692666897203211/970382349617483856/293.jpg")
            return

        if 'trade' in ctx.content.lower():
            await ctx.channel.send("yeah i trade :smile:")
            return

        if 'do' in ctx.content.lower()[ctx_size - 2:] or 'doing' in ctx.content.lower()[ctx_size - 5:] or 'doin' in ctx.content.lower()[ctx_size - 4:] or 'did' in ctx.content.lower()[ctx_size - 3:] or 'wyd' in ctx.content.lower()[ctx_size - 3:]:
            await ctx.channel.send(mom())
            return

    else:
        # Note: Since on_message() overrides what the bot does to during a message send, this process the message as a command.
        # Assumes that if command fails, then command syntax was invalid or wasn't a command
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
        "features": ">>> __**Description**__\nThis is a set of automatic processes that the bot can do. Note that these are __not__ commands and happen passively.",
        "morbius": ">>> __**Description**__\nAnytime a user sends a message that has the string 'morbius', the bot responds with a morbius-themed copypasta.\nExample: I am morbius\nResponse: I love Morbius so much <3",
        "sad": ">>> __**Description**__\nAnytime a user sends a message that has the string 'sad', the bot responds and sends a picture of sad Spongebob.\nExample: I am sad\nResponse: *picture of sad spongebob*",
        "sus": ">>> __**Description**__\nAnytime a user sends a message that has the string 'sus', the bot responds and highlights the message.\nExample: I am sus\nResponse: Amogus detected: I am ***sus***",
        "sus": ">>> __**Description**__\nAnytime a user sends a message that has the string 'trade', the bot responds with 'yeah i trade :smile:'.\nExample: I trade\nResponse: Amogus detected: yeah i trade :smile:",

        "fun": ">>> __**Description**__\nThis section is full of commands that either serve no real functional purpose. They are just here for fun.",
        "boowomp": ">>> __**Description**__\nThis command sends a sad spongebob image.\n\n__**Usage**__\ns-boowomp <no arguments>",
        "copypasta": ">>> __**Description**__\nThis command makes the bot say a random copypasta from a list.\n\n__**Usage**__\ns-copypasta <no arguments>",
        "funky": ">>> __**Description**__\nThis command gives an image of a fumo with the optional argument of a specific character\n\n__**Usage**__\ns-funky <optional name>\nExample: s-funky cirno",
        
        "utility": ">>> __**Description**__\nThis section has commands that mainly serve a purpose to bot testers. You can use them tho :>",
        "echo": ">>> __**Description**__\nThis command makes the bot echo anything.\n\n__**Usage**__\ns-echo <sentence>",
        "enable": ">>> __**Description**__\nThis command whitelists a command/feature for a server\n\n__**Usage**__\ns-enable <command/feature name>\n\nThis command **cannot** be disabled!",
        "disable": ">>> __**Description**__\nThis command blacklists a command/feature for a server\n\n__**Usage**__\ns-disable <command/feature name>\n\nThis command **cannot** be disabled!",
        "help": ">>> __**Description**__\nOh? Getting meta are we? This command lists every command/feature possible for the bot. Optionally, a command/feature/section name may be added as an argument to get info on said command/feature/section\n\n__**Usage**__\ns-help <optional command/feature/section name>\n\nThis command **cannot** be disabled!",
        "ping": ">>> __**Description**__\nResponds to command and says time for response\n\n__**Usage**__\ns-ping <no arguments>"
    }

    if(not arg == ""):
        if arg.lower() in desc:
            await ctx.channel.send(desc[arg.lower()])
        else:
            await ctx.channel.send(arg,"is not a valid command or feature. Type 's-help' for a list of things I can do.")
    else:
        await ctx.send(">>> __**Features**__ :sparkles:\nmorbius\nsad\nsus\ntrade\n\n__**Fun Commands**__ :sunglasses:\nboowomp\ncopypasta\nfunky\n\n__**Utility Commands**__ :tools:\necho\nenable (WIP)\ndisable (WIP)\nhelp\nping\n\nUse s- as the prefix for commands.\nType s-help command for more info on a command or feature.\nYou may also use s-help for categories.")

@client.command()
async def copypasta(ctx):
    await ctx.channel.send(copypasta_text())

@client.command()
async def funky(ctx,arg = "null"):
    await ctx.channel.send(fumo(arg))

@client.command()
async def boowomp(ctx):
    await ctx.channel.send("https://cdn.discordapp.com/attachments/390692666897203211/970382349617483856/293.jpg")

@client.command()
async def echo(ctx, *, arg):
    if dt.is_blacklisted("echo", str(ctx.guild.id)):
        return
    await ctx.channel.send(arg)

@client.command()
async def ping(ctx):
    if dt.is_blacklisted("ping", str(ctx.guild.id)):
        return
    await ctx.channel.send(f"Pong! {client.latency} ms")

@client.command()
async def disable(ctx, command_name, flag = "\0"):
    if flag == "-c":
        await ctx.channel.send(dt.blacklist_feature(command_name, str(ctx.guild.id), str(ctx.channel.id)))
    else:
        await ctx.channel.send(dt.blacklist_feature(command_name, str(ctx.guild.id)))

@client.command()
async def enable(ctx, command_name, flag = "-1"):
    pass

# Command used for testing
#@client.command()
#async def info(ctx):
#    print("User ID:", ctx.author.id,"Type:", type(ctx.author.id))
#    print("Guild ID:", ctx.guild.id,"Type:", type(ctx.guild.id))
#    print("Channel ID:", ctx.channel.id,"Type:", type(ctx.channel.id))

# Login information for the bot requires a token.
# token is taken from a file named '.token'
# If this file does not exist, user will be prompted to input token

# Current bad token handling: Ask for new TOKEN -> write TOKEN to .token -> crash program
def main():
    try:
        dt.init_guild_config()
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
