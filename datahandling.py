from helper import *
import json
from datetime import datetime

##################
# TOKEN HANDLING #
##################

def write_token(TOKEN: str, filename: str) -> None:
    """
    Writes a token to a specified file.
    If filename does not exist, creates filename and writes the token.

    Parameters:
    TOKEN (str): Token to be written to file
    filename (str): File for TOKEN to be written

    Returns:
    None
    """
    with open(filename, "w") as tokenfile:
        tokenfile.write(TOKEN)
        tokenfile.close()

def get_token(filename: str, use_case = "Unspecified") -> str:
    """
    Obtains token from a file specified asks the user.
    If the file does not have a token or is empty, asks the user if they would like to write to the file

    Parameters:
    filename (str): name of file to be used in obtaining token

    Returns:
    str: token to be used by bot
    """
    # Initializes TOKEN and choice as empty strings
    TOKEN = ""
    choice = ""

    #Currently, this code assumes the only error is the file not existing
    try:
        # opens up filename which should only contain the bot token
        with open(filename) as tokenfile:
            print(f"Using token from {cl.BOLD}'{filename}'{cl.END} for use case: {use_case}")
            TOKEN = tokenfile.read()

            if(TOKEN == ""):
                # If TOKEN == "", this means that the file is empty
                
                while(choice.lower() != "y" and choice.lower() != "n"):
                    choice = input(f"\nIt looks like there isn't anything in {cl.BOLD}'{filename}'{cl.END}.\nWould you like to add a token to this file? [Y/n] ")
                
                if(choice.lower() == 'y'):
                    TOKEN = input('\nPlease enter the bot token: ')
                    write_token(TOKEN, filename)
                else:
                    print(f"\nNo token will be added to {cl.BOLD}'{filename}'{cl.END}")
                    TOKEN = input('Please enter the bot token: ')                
    except OSError:
        # Handling when the file does not exist.
        while(choice.lower() != "y" and choice.lower() != "n"):
            choice = input(f"\nIt looks like there isn't a file named {cl.BOLD}'{filename}'{cl.END} in this directory.\nWould you like to create this file? [Y/n] ")

        if(choice.lower() == 'y'):
            TOKEN = input('\nPlease enter the bot token: ')
            write_token(TOKEN, filename)
        else:
            print("\n.dat will not be created")
            TOKEN = input('Please enter the bot token: ')

    return TOKEN


##########################
# Server Config Handling #
##########################

def blacklist_feature(command_name: str, guildID: str, channelID: str = "\0") -> str:
    """
    Adds a command name in a blacklist linked to the specified guild id. If a channel id is specified, adds command to a specific channel in a guild.

    Parameters:
    command_name (str): name of command to be blacklisted
    guildID (str): guild id to be checked in configdata/guildconfig.json
    channelID (str)[OPTIONAL]: guild id to be checked in guildconfig.json

    Returns:
    str: response for the bot to say when command, guildID, and channelID are parsed
    """
    command_name = command_name.lower()
    # Function doesn't need to blacklist a command if it is already blacklisted
    # is_blacklisted() also adds the guildID in guildconfig.json if needed
    if is_blacklisted(command_name, guildID, channelID):
        return f"'{command_name}' already disabled"

    if command_name in all_features:
        data: dict
        with open("configdata/guildconfig.json", "r") as f:
            data = json.load(f)
            # If the command is not in channel blacklist, adds command to blacklist
            if channelID == "\0":
                data["guilds"][guildID]['blacklist'].append(command_name)
            else:
                # If channelID isn't in data, add a default construction
                if not channelID in data['guilds'][guildID]['channels']:
                    data['guilds'][guildID]['channels'][channelID] = {
                        'blacklist': []
                    }
                data['guilds'][guildID]['channels'][channelID]['blacklist'].append(command_name)
        # New with open() resets pointer to beginning of file to overwrite
        with open("configdata/guildconfig.json", "w") as f:
            json.dump(data, f, indent=2)
            return f"'{command_name}' added to blacklist"
    else:
        return "Command does not exist"

def whitelist_feature(command_name: str, guildID: str, channelID: str = "\0") -> str:
    """
    Deletes a command name in a blacklist linked to the specified guild id. If a channel id is specified, deletes command to a specific channel in a guild.

    Parameters:
    command_name (str): name of command to be whitelisted
    guildID (str): guild id to be checked in configdata/guildconfig.json
    channelID (str)[OPTIONAL]: guild id to be checked in guildconfig.json

    Returns:
    str: response for the bot to say when command, guildID, and channelID are parsed
    """
    command_name = command_name.lower()
    # Function doesn't need to blacklist a command if it is already blacklisted
    if not is_blacklisted(command_name, guildID, channelID):
        return f"'{command_name}' already enabled"

    if command_name in all_features:
        data: dict
        with open("configdata/guildconfig.json", "r") as f:
            data = json.load(f)
            # If the command is not in channel blacklist, adds command to blacklist
            if channelID == "\0":
                data["guilds"][guildID]['blacklist'].remove(command_name)
            else:
                # If channelID isn't in data, add a default construction
                if not channelID in data['guilds'][guildID]['channels']:
                    data['guilds'][guildID]['channels'][channelID] = {
                        'blacklist': []
                    }
                else:
                    data['guilds'][guildID]['channels'][channelID]['blacklist'].remove(command_name)
        # New with open() resets pointer to beginning of file to overwrite
        with open("configdata/guildconfig.json", "w") as f:
            json.dump(data, f, indent=2)
            return f"'{command_name}' removed from blacklist"
    else:
        return "Command does not exist"


def is_blacklisted(command_name: str, guildID: str, channelID: str) -> bool:
    """
    Returns if a command is blacklisted in a specific channel in a guild.

    Parameters:
    command_name (str): name of command to be checked
    guildID (str): guild id to be checked in configdata/guildconfig.json
    channelID (str)[OPTIONAL]: guild id to be checked in guildconfig.json

    Returns:
    bool: boolean whether or not command is blacklisted
    """
    with open("configdata/guildconfig.json", "r") as f:
        data = json.load(f)
        try:
            if (channelID in data['guilds'][guildID]['channels']) and (command_name in data['guilds'][guildID]['channels'][channelID]['blacklist']):
                return True
            else:    
                return command_name in data['guilds'][guildID]['blacklist']
        except KeyError:
            # If a guild id isn't detected, add guild id to dictionary
            # Return False since guilds are default false for every feature/command
            add_guild(guildID)
            return False


def add_guild(guildID: str) -> None:
    """
    Adds a default template of a guildID in configdata/guildconfig.json

    Parameters:
    guildID (str): guild id to be added to configdata/guildconfig.json

    Returns:
    none
    """
    data: dict
    with open("configdata/guildconfig.json", "r") as f:
        data = json.load(f)
        # If guildID isn't in list, adds a default server template attached to guildID
        if not guildID in data['guilds']:
            data["guilds"][guildID] = {
                "blacklist": [],
                "channels": dict()
            }
    # New with open() resets pointer to beginning of file to overwrite
    with open("configdata/guildconfig.json", "w") as f:
        json.dump(data, f, indent=2)


############################
# Data File Initialization #
############################

def init_guild_config() -> None:
    """
    If configdata/guildconfig.json does not exists, creates a template file.
    Skips the process if configdata/guildconfig.json exists.
    """
    try:
        with open("configdata/guildconfig.json", "x") as f:
            data = {
                "guilds": dict()
            }
            # Example guild with restrictions on certain commands and features
            data["guilds"]["EXAMPLE_SERVER_ID"] ={
                "blacklist": ["sus", "morbius", "fumo"],
                "channels": {"EXAMPLE_CHANNEL_ID": {"blacklist": ["copypasta"]}, "EXAMPLE_CHANNEL_ID_2": {"blacklist": ["sad"]}}
            }
            json.dump(data, f, indent=2)
            print(f"{cl.GREEN}{cl.BOLD}configdata/guildconfig.json{cl.END}{cl.GREEN} created :){cl.END}")
    except FileExistsError:
        print(f'{cl.YELLOW}{cl.BOLD}configdata/guildconfig.json{cl.END}{cl.YELLOW} exists. Skipping creation of file...{cl.END}')

def init_file(filename: str, logging: bool = False) -> None:
    """
    If filaname does not exists, creates a blank file.
    Skips the process if filename exists.

    Parameters:
    filename (str): name of file to be created

    Returns:
    none
    """
    try:
        with open(filename, "x") as f:
            if logging:
                print(f"{cl.GREEN}{cl.BOLD}{filename}{cl.END}{cl.GREEN} created.{cl.END}")
    except FileExistsError:
        if logging:
            print(f'{cl.YELLOW}{cl.BOLD}{filename}{cl.END}{cl.YELLOW} exists. Skipping creation of file...{cl.END}')


def init_json(filename: str, logging: bool = False) -> None:
    try:
        with open(filename, "x") as f:
            # Adds a blank dictionary into the file
            data = {}
            json.dump(data, f, indent = 2)

            if logging:
                print(f"{cl.GREEN}{cl.BOLD}{filename}{cl.END}{cl.GREEN} created.{cl.END}")
    except FileExistsError:
        if logging:
            print(f'{cl.YELLOW}{cl.BOLD}{filename}{cl.END}{cl.YELLOW} exists. Skipping creation of file...{cl.END}')


def add_json_dict_keys(filename: str, *keynames: str):
    data: dict
    for i in range(len(keynames)):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
    
            with open(filename, "w") as f:
                data[keynames[i]] = {}
                json.dump(data, f, indent = 2)
    
        except Exception as e:
            print(f"{cl.GREY}{cl.BOLD}{str(datetime.now())[:-7]}{cl.RED} ERROR{cl.END}    Issue adding key as dictionary to {filename}: {e}")


#################
# Miscellaneous #
#################

def get_copypasta_list() -> list:
    with open("textdata/copypasta.dat", "r") as f:
        data = f.read()
        data = data.split('\n\n')
        data.pop(len(data) - 1)
        i = 0
        for copy in data:
            copy = copy.replace("\\n","\n")
            data[i] = copy
            i += 1
        return data

print(f"{cl.GREEN}{cl.BOLD}datahandling.py{cl.END}{cl.GREEN} initialized{cl.END}")
