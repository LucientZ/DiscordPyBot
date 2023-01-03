# Packages
import discord
from discord import app_commands
import time
from datetime import datetime

# Other Files
import datahandling as dt
from textfunctions import *
from helper import *


class aclient(discord.Client):
    def __init__(self):
        super().__init__(activity = discord.Game(name = "/help"), intents=discord.Intents.all())

        # Asks user if global sync for commands should occur
        choice = ""
        while choice.lower() != "y" and choice.lower() != "n":
            choice = input("Would you like to sync the bot globally? (Only do this if the bot has been updated or a command has changed) [Y/n] ")

        if choice.lower() == "y":
            self.synced = False
        else:
            self.synced = True

    async def on_ready(self):
        """
        When the bot is ready, checks if the bot's commands should be synced or not.
        Once commands are synced, the bot will be fully ready.
        """

        await self.wait_until_ready()

        # Once the bot is ready, will attempt to sync commands globally if self.synced is false
        if not self.synced:
            print(f"{cl.GREY}{cl.BOLD}{str(datetime.now())[:-7]}{cl.BLUE} INFO{cl.END}     Awaiting command tree syncing...")
            a = time.time()
            # Syncs command tree globally
            await tree.sync()
            b = time.time()
            print(f"{cl.GREY}{cl.BOLD}{str(datetime.now())[:-7]}{cl.BLUE} INFO{cl.END}     Tree Synced. Elapsed time: {int((b - a) * 100) / 100} seconds")
            self.synced = True
        print(f"{cl.GREY}{cl.BOLD}{str(datetime.now())[:-7]}{cl.BLUE} STATUS{cl.END}   I exist as user '{self.user}' and can talk to people! :D")

    async def on_connect(self):
        """
        States when the bot has connected to discord
        """
        print(f"{cl.GREY}{cl.BOLD}{str(datetime.now())[:-7]}{cl.BLUE} STATUS{cl.END}   I'm initializing myself as a bot :)")

    async def on_message(self, ctx: discord.Interaction):
        """
        When a user sends a message to a channel the bot has access to, processes the message and responds accordingly.
        """

        # Bot doesn't respond to itself
        # Protection for if a message parsed by the bot is too long.
        ctx_size = len(ctx.content)
        if ctx.author.bot or ctx_size > 1500:
            return

        # Current response in DMs is simply to say "Hello"
        if isinstance(ctx.channel, discord.channel.DMChannel):
            await ctx.channel.send("Hello")
        # Default response
        else:
            if not dt.is_blacklisted("sus", str(ctx.guild.id), str(ctx.channel.id)) and 'sus' in ctx.content.lower():
                if(not ctx_size > 665):
                    await ctx.channel.send("Amogus detected: " + format_msg(ctx.content, 'sus','**'))
                else:
                    await ctx.channel.send("__Amogus Detected in Message__")
                    await ctx.channel.send(ctx.content)
            elif not dt.is_blacklisted("morbius", str(ctx.guild.id), str(ctx.channel.id)) and 'morb' in ctx.content.lower():
                await ctx.channel.send(morbius())
            elif not dt.is_blacklisted("sad", str(ctx.guild.id), str(ctx.channel.id)) and 'sad' in ctx.content.lower():
                await ctx.channel.send("https://cdn.discordapp.com/attachments/390692666897203211/970382349617483856/293.jpg")
            elif not dt.is_blacklisted("trade", str(ctx.guild.id), str(ctx.channel.id)) and 'trade' in ctx.content.lower():
                await ctx.channel.send("yeah i trade :smile:")
            elif not dt.is_blacklisted("mom", str(ctx.guild.id), str(ctx.channel.id)) and (ctx.content.lower().endswith(("do", "doin", "doing", "wyd", "did", "done")) or (ctx.content.lower()[:-1].endswith(("do", "doin", "doing", "wyd", "did", "done"))) and not ctx.content.lower()[-1].isalnum()):
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
        print(f"{cl.GREY}{cl.BOLD}{str(datetime.now())[:-7]}{cl.RED} ERROR{cl.END}    Ignoring error in command tree:", error)
        await ctx.response.send_message(f"The command you just tried using doesn't seem to exist. This is either due to a global sync issue or my developer was too lazy to fix it. :dolphin::dolphin::dolphin:\n\nTo report an issue, please go to <https://github.com/LucientZ/DiscordPyBot>", ephemeral = True)
    elif isinstance(error, discord.app_commands.errors.MissingPermissions):
        await ctx.response.send_message(f"You lack the required administrator permissions for this command.\n\nIf this is unexpected, please file an issue report at <https://github.com/LucientZ/DiscordPyBot>", ephemeral = True)
    else:
        print(f"{cl.GREY}{cl.BOLD}{str(datetime.now())[:-7]}{cl.RED} ERROR{cl.END}    An error occurred in command tree. Ignoring for now:", error)
        await ctx.response.send_message(f"An error occurred while trying to process a command.\n\n[{error}]\n\nIf this is unexpected, please file an issue report at <https://github.com/LucientZ/DiscordPyBot>", ephemeral = True)


####################
# Commands Section #
####################

@tree.command(name = "help", description = "Responds with a list of commands and features. Can be used for specific commands")
async def help(ctx: discord.Interaction, item_name: str = "NA"):
    """
    Returns information about the bot in general or about a specific command/feature/category.
    """
    desc = {
        "auto": ">>> __**Automatic Features Description**__\nThis is a set of automatic processes that the bot can do. Note that these are __not__ commands happen passively.\n\nTo prevent the bot from spamming, only one of these is usually called. The general hierarchy of what process is called is the order in which the automatic features are listed in the default /help section.",
        #####################################################
        "mom": ">>> __**Description**__\nAnytime a user sends a message that has a string similar to 'do' at the end, the bot responds with 'Your Mom'.\nExample: What are you doing?\nResponse: Your Mom\n\nKeywords: do, doin, doing, wyd, did",
        "morbius": ">>> __**Description**__\nAnytime a user sends a message that has the string 'morbius', the bot responds with a morbius-themed copypasta.\nExample: I am morbius\nResponse: I love Morbius so much <3",
        "sad": ">>> __**Description**__\nAnytime a user sends a message that has the string 'sad', the bot responds and sends a picture of sad Spongebob.\nExample: I am sad\nResponse: *picture of sad spongebob*",
        "sus": ">>> __**Description**__\nAnytime a user sends a message that has the string 'sus', the bot responds and highlights the message.\nExample: I am sus\nResponse: Amogus detected: I am ***sus***",
        "trade": ">>> __**Description**__\nAnytime a user sends a message that has the string 'trade', the bot responds with 'yeah i trade :smile:'.\nExample: I trade\nResponse: Amogus detected: yeah i trade :smile:",
        
        "fun": ">>> __**Fun Commands Description**__\nThis section is full of commands that either serve no real functional purpose. They are just here for fun.",
        #####################################################
        "copypasta": ">>> __**Description**__\nThis command makes the bot say a random copypasta from a list.\n\n__**Usage**__\n/copypasta <no arguments>",
        "fumo": ">>> __**Description**__\nThis command gives an image of a fumo with the optional argument of a specific character\n\n__**Usage**__\n/fumo <optional name>\nExample: /fumo cirno",

        "utility": ">>> __**Utility Commands Description**__\nThis section has commands that mainly serve server admins and bot testers.",
        #####################################################
        "echo": ">>> __**Description**__\nThis command makes the bot echo anything.\n\n__**Usage**__\n/echo <sentence>",
        "ping": ">>> __**Description**__\nResponds to command and says time for response\n\n__**Usage**__\n/ping <no arguments>",
        "enable": ">>> __**Description**__\nThis command removes a command/feature from the blacklist for a server. Use flag -c to enable for specific channel.\nUser must have **admin** permission to use\n\n__**Usage**__\n/enable <command/feature name>\n/enable <command/feature name> <-c>\n\nThis command **cannot** be disabled!",
        "disable": ">>> __**Description**__\nThis command blacklists a command/feature for a server. Use flag -c to disable for specific channel.\nUser must have **admin** permission to use\n\n__**Usage**__\n/disable <command/feature name>\n/disable <command/feature name> <-c>\n\nThis command **cannot** be disabled!",
        "help": ">>> __**Description**__\nOh? Getting meta are we? This command lists every command/feature possible for the bot. Optionally, a command/feature/section name may be added as an argument to get info on said command/feature/section\n\n__**Usage**__\n/help <optional command/feature/section name>\n\nThis command **cannot** be disabled!"
    }

    if not item_name == "NA":
        if item_name.lower() in desc:
            await ctx.response.send_message(desc[item_name.lower()])
        else:
            await ctx.response.send_message(f"{item_name} is not a valid command or feature. Type '/help' for a list of things I can do")
    else:
        await ctx.response.send_message(">>> __**Automatic Features**__ :sparkles: [auto]\nsus\nmorbius\nsad\ntrade\nmom\n\n__**Fun Commands**__ :sunglasses: [fun]\nboowomp\ncopypasta\nfumo\n\n__**Utility Commands**__ :tools: [utility]\necho\nenable\ndisable\nhelp\nping\n\nUse / as the prefix for commands.\nType /help [command] for more info on a command or feature.\nYou may also use /help for categories.\n\nTo disable or enable an entire category, enter the keyword associated with the category.\n\nAny issues with the bot should be reported on GitHub at <https://github.com/LucientZ/DiscordPyBot> or directly to LucienZ#3376")


@tree.command(name = "copypasta", description = "Returns a copypasta from a select list the bot has.")
async def copypasta(ctx: discord.Interaction):
    if dt.is_blacklisted("copypasta", str(ctx.guild_id), str(ctx.channel_id)):
        await ctx.response.send_message("This command has been disabled in this server or channel.\n\nIf this is unexpected, please file an issue report at <https://github.com/LucientZ/DiscordPyBot>", ephemeral=True)
        return
    await ctx.response.send_message(copypasta_text())


@tree.command(name = "fumo", description = "Gives an image of a fumo doll with the option of specifying the character")
async def fumo(ctx: discord.Interaction, name: str = "NA"):
    """
    Obtains a url for an image of a fumo (specified or not) and makes the bot send the url as a message
    """
    if dt.is_blacklisted("fumo", str(ctx.guild_id), str(ctx.channel_id)):
        await ctx.response.send_message("This command has been disabled in this server or channel.\n\nIf this is unexpected, please file an issue report at <https://github.com/LucientZ/DiscordPyBot>", ephemeral=True)
        return
    await ctx.response.send_message(get_fumo_url(name))


@tree.command(name = "echo", description = "Makes bot echo what the user said. Adds small string at beginning to avoid issues with other bots.")
async def echo(ctx: discord.Interaction, message: str):
    """
    Makes the bot echo an input from the user as long as the message is below 1500 characters
    """
    if dt.is_blacklisted("echo", str(ctx.guild_id), str(ctx.channel_id)) or len(message) > 1500:
        await ctx.response.send_message("This command has been disabled in this server or channel.\n\nIf this is unexpected, please file an issue report at <https://github.com/LucientZ/DiscordPyBot>", ephemeral=True)
        return
    await ctx.response.send_message(f"Echo: {message}")


@tree.command(name = "ping", description = "Responds and states client latency in milliseconds")
async def ping(ctx: discord.Interaction):
    """
    Makes the bot respond to the user and reply with the client latency in ms
    """
    if dt.is_blacklisted("ping", str(ctx.guild_id), str(ctx.channel_id)):
        await ctx.response.send_message("This command has been disabled in this server or channel.\n\nIf this is unexpected, please file an issue report at <https://github.com/LucientZ/DiscordPyBot>", ephemeral=True)
        return
    await ctx.response.send_message(f"Pong!\nClient Latency: {int(client.latency * 1000)} ms")

@tree.command(name = "enable", description = "Enables a feature/command with optional flag [-c]")
@app_commands.checks.has_permissions(administrator = True)
async def enable(ctx: discord.Interaction, command_name: str, flag: str = "\0"):
    channel_id = ""
    msg_end = ""
    if flag == "-c":
        channel_id = str(ctx.channel_id)
        msg_end = " in this channel."
    else:
        channel_id = "\0"
        msg_end = " globally in the server."
    # Whitelists all automatic features
    if "auto" in command_name.lower():
        for command in features:
            dt.whitelist_feature(command, str(ctx.guild_id), channel_id)
        await ctx.response.send_message("All automatic features enabled" + msg_end)
    # Whitelists all fun commands
    elif "fun" in command_name.lower():
        for command in fun_commands:
            dt.whitelist_feature(command, str(ctx.guild_id), channel_id)
        await ctx.response.send_message("All fun commands enabled" + msg_end)
    # Whitelists all utility commands
    elif "utility" in command_name.lower():
        for command in utility_commands:
            dt.whitelist_feature(command, str(ctx.guild_id), channel_id)
        await ctx.response.send_message("All utility commands enabled" + msg_end)
    else:
        await ctx.response.send_message(dt.whitelist_feature(command_name, str(ctx.guild_id), channel_id))

@tree.command(name = "disable", description = "Disables a feature/command with optional flag [-c]")
@app_commands.checks.has_permissions(administrator = True)
async def disable(ctx: discord.Interaction, command_name: str, flag: str = "\0"):
    channel_id = ""
    msg_end = ""
    if flag == "-c":
        channel_id = str(ctx.channel_id)
        msg_end = " in this channel."
    else:
        channel_id = "\0"
        msg_end = " globally in the server."
    # Whitelists all automatic features
    if "auto" in command_name.lower():
        for command in features:
            dt.blacklist_feature(command, str(ctx.guild_id), channel_id)
        await ctx.response.send_message("All automatic features disabled" + msg_end)
    # Whitelists all fun commands
    elif "fun" in command_name.lower():
        for command in fun_commands:
            dt.blacklist_feature(command, str(ctx.guild_id), channel_id)
        await ctx.response.send_message("All fun commands disabled" + msg_end)
    # Whitelists all utility commands
    elif "utility" in command_name.lower():
        for command in utility_commands:
            dt.blacklist_feature(command, str(ctx.guild_id), channel_id)
        await ctx.response.send_message("All utility commands disabled" + msg_end)
    else:
        await ctx.response.send_message(dt.blacklist_feature(command_name, str(ctx.guild_id), channel_id))

@tree.command(name="get-blacklist", description="Returns a list of blacklisted features in the channel and server")
async def get_blacklist(ctx: discord.Interaction):
    # initializes the blacklist of server and channel
    server_dict = dt.get_json_dict("configdata/guildconfig.json")["guilds"][str(ctx.guild_id)]
    server_blacklist = server_dict["blacklist"]
    

    # Builds string to be sent to user
    msg = ">>> __Server Blacklist__\n"
    if len(server_blacklist) == 0:
        msg += " - None\n"
    else:
        for item in server_blacklist:
            msg += f" - {item}\n"
    msg += "\n __Channel Blacklist__\n"

    try:
        channel_blacklist = server_dict["channels"][str(ctx.channel_id)]["blacklist"]
        if len(channel_blacklist) == 0:
            msg += " - None\n\n"
        else:
            for item in channel_blacklist:
                msg += f" - {item}\n"
    except KeyError:
        msg += " - None\n\n"

    await ctx.response.send_message(msg)



def main():
    try:
        # Initializes all files the bot will work with
        dt.init_guild_config()
        dt.init_file("textdata/copypasta.dat", True)
        dt.init_json("textdata/urls.json", True)
        dt.add_json_dict_keys("textdata/urls.json", "fumo", "misc")
        dt.add_fumo_url("example", "https://cdn.discordapp.com/attachments/390692666897203211/979153065259175946/Screenshot_20220520-193448_Gallery.jpg")

        # Obtains bot token and uses it to log in
        TOKEN = dt.get_token(".token", "Logging In")
        client.run(TOKEN)
    except discord.LoginFailure as e:
        #This error is raised when the token is not valid
        print(f"{cl.GREY}{cl.BOLD}{str(datetime.now())[:-7]}{cl.RED} ERROR{cl.END}    Issue logging into bot:{cl.BLUE} {e}{cl.END}\n")
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
        print(f"{cl.GREY}{cl.BOLD}{str(datetime.now())[:-7]}{cl.RED} ERROR{cl.END}    Issue logging into bot:{cl.BLUE} {e}{cl.END}\n")
        print("Terminating program...\n")
        exit()
        
if __name__ == '__main__':
    main()
    