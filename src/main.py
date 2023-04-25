# Packages
import discord, os, time
from discord import app_commands
from dotenv import load_dotenv

# Other Files
import helper, datahandling, userinterfaces, init
from helper import cl, Logger
from textfunctions import *

# Environment Variables
if __name__ == "__main__":
    while(not os.path.isfile("./config/.env")):
        init.query_env_vars()
    load_dotenv("./config/.env")
else:
    load_dotenv("./src/tests/test_vars.env")

class ENV_VARS:
    TOKEN = os.environ.get("TOKEN")
    STATUS = os.environ.get("STATUS")
    SYNC_ON_START= os.environ.get("SYNC_ON_START").lower() in ('true', '1', 't')

#=====================================================
# Discord Client Section
#=====================================================
class aclient(discord.Client):
    def __init__(self): # pragma: no cover
        super().__init__(activity = discord.Game(name = ENV_VARS.STATUS), intents=discord.Intents.all())

        if ENV_VARS.SYNC_ON_START:
            self.synced = False
        else:
            self.synced = True

    async def on_ready(self): # pragma: no cover
        """
        When the bot is ready, checks if the bot's commands should be synced or not.
        Once commands are synced, the bot will be fully ready.
        """

        await self.wait_until_ready()

        # Once the bot is ready, will attempt to sync commands globally if self.synced is false
        if not self.synced:
            Logger.log_info("Awaiting command tree syncing...")
            a = time.time()
            # Syncs command tree globally
            await tree.sync()
            b = time.time()
            Logger.log_info(f"Tree Synced. Elapsed time: {int((b - a) * 100) / 100} seconds")
            self.synced = True
        Logger.log_info(f"I exist as user '{self.user}' and can talk to people! :D")
        
    async def on_connect(self): # pragma: no cover
        """
        States when the bot has connected to discord
        """
        Logger.log_info("I'm initializing myself as a bot...")

    async def on_message(self, ctx: discord.message.Message):
        """
        When a user sends a message to a channel the bot has access to, processes the message and responds accordingly.
        """

        # Bot doesn't respond to itself
        # Protection for if a message parsed by the bot is too long.
        ctx_size = len(ctx.content)
        if ctx.author.bot or ctx_size > 1500:
            return

        if isinstance(ctx.channel, discord.channel.DMChannel):
            await ctx.channel.send("Hi, I am a bot :)") # No behavior when in a dm channel
        else:
            guild = datahandling.GuildProfile(ctx.guild.id, helper.auto_features)
            if guild.is_enabled("sus", ctx.channel.id) and 'sus' in ctx.content.lower():
                if(not ctx_size > 250):
                    await ctx.channel.send("Amogus detected: " + format_msg(ctx.content, 'sus','***'))
                else:
                    await ctx.channel.send("__Amogus Detected in Message__")
                    await ctx.channel.send(ctx.content)
            elif guild.is_enabled("morbius", ctx.channel.id) and 'morb' in ctx.content.lower():
                await ctx.channel.send(morbius())
            elif guild.is_enabled("sad", ctx.channel.id) and 'sad' in ctx.content.lower():
                await ctx.channel.send("https://cdn.discordapp.com/attachments/390692666897203211/970382349617483856/293.jpg")
            elif guild.is_enabled("trade", ctx.channel.id) and 'trade' in ctx.content.lower():
                await ctx.channel.send("yeah i trade :smile:")
            elif guild.is_enabled("mom", ctx.channel.id) and (ctx.content.lower().endswith(("do", "doin", "doing", "wyd", "did", "done")) or (ctx.content.lower()[:-1].endswith(("do", "doin", "doing", "wyd", "did", "done"))) and not ctx.content.lower()[-1].isalnum()):
                await ctx.channel.send(mom())


client = aclient()


#=====================================================
# Command Tree Section
#=====================================================

tree = app_commands.CommandTree(client)


@tree.error
async def on_app_command_error(ctx: discord.Interaction, error: discord.app_commands.AppCommandError):
    """
    Handles errors on the bot's command tree.
    """
    # If the command doesn't exist, then the most likely culprit is due to a command being synced globally and then ceasing to exist and the bot informs the user. 
    # Otherwise, give a generic response for the user to file a bug report.
    if isinstance(error, discord.app_commands.errors.CommandNotFound):
        Logger.log_error(f"Ignoring error in command tree: {error}")
        await ctx.response.send_message(f"The command you just tried using doesn't seem to exist. This is either due to a global sync issue or my developer was too lazy to fix it. :dolphin::dolphin::dolphin:\n\nTo report an issue, please go to <https://github.com/LucientZ/DiscordPyBot>", ephemeral = True)
    elif isinstance(error, discord.app_commands.errors.MissingPermissions):
        await ctx.response.send_message(f"You lack the required administrator permissions for this command.\n\nIf this is unexpected, please file an issue report at <https://github.com/LucientZ/DiscordPyBot>", ephemeral = True)
    else:
        Logger.log_error(f"An error occurred in command tree: {error}")
        await ctx.response.send_message(f"An error occurred while trying to process a command.\n\n[{error}]\n\nIf this is unexpected, please file an issue report at <https://github.com/LucientZ/DiscordPyBot>", ephemeral = True)


@tree.command(name = "help", description = "Responds with a list of commands and features. Can be used for specific commands")
async def help(ctx: discord.Interaction, item_name: str = "", page_index: int = 1):
    """
    Returns information about the bot in general or about a specific command/feature/category.
    """
    print(page_index)

    if(item_name == ""): # When item name is empty, produce default help menu
        view = userinterfaces.HelpMenu()
        embed = view.get_page_embed(page_index - 1) # Gets the embed of the specific page. Because the page is indexed as a list, subtract one from what the user gives. discord.py will ensure that this is an integer 
    else: # If the item name isn't empty, produces help menu for the specific command
        embed = discord.Embed(title = item_name.lower(), description = userinterfaces.HelpMenu.item_descriptions.get(item_name.lower(), "Command could not be found."), color = 0xffab00)
        view = discord.ui.View()

    view.add_item(discord.ui.Button(label="Documentation", style = discord.ButtonStyle.link, url = "https://lucientz.github.io/DiscordPyBot"))

    await ctx.response.send_message(embed = embed, view = view)


@tree.command(name = "copypasta", description = "Returns a copypasta from a select list the bot has.")
async def copypasta(ctx: discord.Interaction):
    """
    Returns a copypasta from a list of copypastas
    """
    await ctx.response.send_message(copypasta_text())


@tree.command(name = "fumo", description = "Gives an image of a fumo doll with the option of specifying the character")
async def fumo(ctx: discord.Interaction, name: str = "NA"):
    """
    Obtains a url for an image of a fumo (specified or not) and makes the bot send the url as a message
    """
    await ctx.response.send_message(get_fumo_url(name))


@tree.command(name = "echo", description = "Makes bot echo what the user said. Adds small string at beginning to avoid issues with other bots.")
async def echo(ctx: discord.Interaction, message: str):
    """
    Makes the bot echo an input from the user as long as the message is below 1500 characters
    """
    if len(message) > 1500:
        await ctx.response.send_message("This message is too long.\n\nIf this is unexpected, please file an issue report at <https://github.com/LucientZ/DiscordPyBot>", ephemeral=True)
    else:
        await ctx.response.send_message(f"Echo: {message}")


@tree.command(name = "ping", description = "Responds and states client latency in milliseconds")
async def ping(ctx: discord.Interaction):
    """
    Makes the bot respond to the user and reply with the client latency in ms
    """
    await ctx.response.send_message(f"Pong!\nClient Latency: {int(client.latency * 1000)} ms")


@tree.command(name = "server-enable", description = "Enables an automatic feature server-wide. Enable 'all' for all features to be enabled.")
@app_commands.checks.has_permissions(administrator = True)
async def server_enable(ctx: discord.Interaction, feature_name: str):
    """
    Enables a feature guild-wide. This is called 'server'-enable because guilds are known as servers by most people.
    """
    guild = datahandling.GuildProfile(str(ctx.guild_id), helper.auto_features)
    feature_name = feature_name.lower()

    if feature_name == 'a' or feature_name == "all":
        for feature in helper.auto_features:
            guild.guild_enable_auto(feature)
        await ctx.response.send_message("All features have been enabled guild-wide.", ephemeral = True)
    else:
        try:
            guild.guild_enable_auto(feature_name)
            await ctx.response.send_message(f"'{feature_name}' has been enabled guild-wide.", ephemeral = True)
        except ValueError:
            await ctx.response.send_message(f"'{feature_name}' is NOT a valid feature to enable. Valid features include {helper.auto_features}.", ephemeral = True)
    

@tree.command(name = "server-disable", description = "Disables an automatic feature server-wide. Disable 'all' to disable all features.")
@app_commands.checks.has_permissions(administrator = True)
async def server_disable(ctx: discord.Interaction, feature_name: str):
    """
    Disables a feature guild-wide. This is called 'server'-disable because guilds are known as servers by most people.
    """
    guild = datahandling.GuildProfile(str(ctx.guild_id), helper.auto_features)
    feature_name = feature_name.lower()

    if feature_name == 'a' or feature_name == "all":
        for feature in helper.auto_features:
            guild.guild_disable_auto(feature)
        await ctx.response.send_message("All features have been disabled guild-wide (This does not affect features enabled in specific channels).", ephemeral = True)
    else:
        try:
            guild.guild_disable_auto(feature_name)
            await ctx.response.send_message(f"'{feature_name}' has been disabled guild-wide (This does not affect channels that have this feature enabled).", ephemeral = True)
        except ValueError:
            await ctx.response.send_message(f"'{feature_name}' is NOT a valid feature to disable. Valid features include {helper.auto_features}", ephemeral = True)


@tree.command(name = "channel-enable", description = "Enables an automatic feature in this channel. Enable 'all' for all features to be enabled.")
@app_commands.checks.has_permissions(administrator = True)
async def channel_enable(ctx: discord.Interaction, feature_name: str):
    """
    Enables a feature in a specific channel.
    """
    guild = datahandling.GuildProfile(str(ctx.guild_id), helper.auto_features)
    feature_name = feature_name.lower()

    if feature_name == 'a' or feature_name == "all":
        for feature in helper.auto_features:
            guild.channel_enable_auto(feature, str(ctx.channel_id))
        await ctx.response.send_message("All features have been enabled in this channel.", ephemeral = True)
    else:
        try:
            guild.channel_enable_auto(feature_name, str(ctx.channel_id))
            await ctx.response.send_message(f"'{feature_name}' has been enabled in this channel.", ephemeral = True)
        except ValueError:
            await ctx.response.send_message(f"'{feature_name}' is NOT a valid feature to enable. Valid features include {helper.auto_features}.", ephemeral = True)


@tree.command(name = "channel-disable", description = "Disables an automatic feature in this channel. Enable 'all' for all features to be enabled.")
@app_commands.checks.has_permissions(administrator = True)
async def channel_disable(ctx: discord.Interaction, feature_name: str):
    """
    Disables a feature in a specific channel.
    """
    guild = datahandling.GuildProfile(str(ctx.guild_id), helper.auto_features)
    feature_name = feature_name.lower()

    if feature_name == 'a' or feature_name == "all":
        for feature in helper.auto_features:
            guild.channel_disable_auto(feature, str(ctx.channel_id))
        await ctx.response.send_message("All features have been disabled in this channel.", ephemeral = True)
    else:
        try:
            guild.channel_disable_auto(feature_name, str(ctx.channel_id))
            await ctx.response.send_message(f"'{feature_name}' has been disabled in this channel.", ephemeral = True)
        except ValueError:
            await ctx.response.send_message(f"'{feature_name}' is NOT a valid feature to enable. Valid features include {helper.auto_features}.", ephemeral = True)
    

def main():
    try:
        # Initializes all files the bot will work with
        datahandling.init_file("data/textdata/copypasta.dat", True)
        datahandling.init_json("data/textdata/urls.json", True)
        datahandling.add_json_dict_keys("data/textdata/urls.json", "fumo", "misc")
        datahandling.add_fumo_url("example", "https://cdn.discordapp.com/attachments/390692666897203211/979153065259175946/Screenshot_20220520-193448_Gallery.jpg")

        # Obtains bot token and uses it to log in
        client.run(ENV_VARS.TOKEN, log_handler = Logger.log_file_handler, log_formatter = Logger.log_file_formatter)
    except discord.LoginFailure as e:
        #This error is raised when the token is not valid
        Logger.log_error(f"Login failure while attempting to log into bot: {e}")
        print("This is likely an issue with the bot token being invalid. Please recreate the .env file in ./config/.env or delete it and re-run ./src/init.py")
        input("Press ENTER to exit program")
        exit()
    except Exception as e:
        Logger.log_error(f"Issue logging into bot: {e}")
        input("Press ENTER to exit program")
        exit()
        

if __name__ == '__main__':
    main()
    