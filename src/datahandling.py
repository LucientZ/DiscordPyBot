from helper import *
import json, os
from datetime import datetime

#===========================================================
# Server Config Handling
#===========================================================

class GuildProfile():
    """
    Interface used for modifying and obtaining guild config information
    """
    def __init__(self, guild_id: str, valid_features: list) -> None:
        self._data: dict
        self._guild_id: str = guild_id
        self._valid_features: list = valid_features
        try:
            self.load(guild_id)
        except Exception as e:
            raise ValueError(f"Issue initializing GuildProfile object with id '{guild_id}':\n{e}")

    def load(self, guild_id: str) -> None:
        """
        Loads dictionary from JSON file into interface 
        If file doesn't exist, creates said file
        """
        if(os.path.isfile(f"data/guild-profiles/{guild_id}.json")):
            with open(f"data/guild-profiles/{guild_id}.json", "r") as f:
                self._data: dict = json.load(f)
        else:
            self._data = {
                "enabled_auto_features" : [],
                "channels": {}
            }
            self.save()
        self._guild_id = guild_id

    def save(self) -> None:
        """
        Saves _data dictionary into the guild's respective json
        """
        with open(f"data/guild-profiles/{self._guild_id}.json", "w") as f:
            json.dump(self._data, f, indent=2)
    
    def get_data(self) -> dict:
        """
        Returns _data dictionary member
        """
        return self._data
    
    def get_id(self) -> str:
        """
        Returns _guild_id string member
        """
        return self._guild_id
    
    def get_valid_features(self) -> list:
        """
        Returns _valid_features list member
        """
        return self._valid_features

    def get_guild_enabled_features(self) -> list:
        return self._data["enabled_auto_features"]
    
    def get_channel_enabled_features(self, channel_id: str) -> list:
        """
        Returns a list of valid features in the specific channel
        """
        if not channel_id in self._data["channels"]:
            self.add_channel(channel_id)
        
        return self._data["channels"][channel_id]["enabled_auto_features"]

    def add_channel(self, channel_id: str) -> None:
        """
        Adds a channel to the collection of channels in the guild
        """
        if not channel_id in self._data["channels"]:
            channel_data: dict = {
                "enabled_auto_features" : []
            }
            self._data["channels"][channel_id] = channel_data
            self.save()
    
    def guild_enable_auto(self, feature_name: str) -> None:
        """
        Enables an automatic feature guild-wide
        """
        if not feature_name in self._valid_features:
            raise ValueError("Not a valid feature to enable")
        
        if not (feature_name in self._data["enabled_auto_features"]):
            self._data["enabled_auto_features"].append(feature_name)
            self.save()

    def guild_disable_auto(self, feature_name: str) -> None:
        """
        Disables an automatic feature guild-wide
        """
        if feature_name in self._valid_features and (feature_name in self._data["enabled_auto_features"]):
            self._data["enabled_auto_features"].remove(feature_name)
            self.save()

    def channel_enable_auto(self, feature_name: str, channel_id: str) -> None:
        """
        Enables an automatic feature in a specific channel in a guild
        """
        if not feature_name in self._valid_features:
            raise ValueError("Not a valid feature to enable")
        elif not channel_id in self._data["channels"]:
            self.add_channel(channel_id)
        
        if not (feature_name in self._data["channels"][channel_id]["enabled_auto_features"]):
            self._data["channels"][channel_id]["enabled_auto_features"].append(feature_name)
            self.save()

    def channel_disable_auto(self, feature_name: str, channel_id: str):
        """
        Disables an automatic feature in a specific channel in a guild
        """
        if not channel_id in self._data["channels"]:
            self.add_channel(channel_id)

        if feature_name in self._valid_features and channel_id in self._data["channels"] and (feature_name in self._data["channels"][channel_id]["enabled_auto_features"]):
            self._data["channels"][channel_id]["enabled_auto_features"].remove(feature_name)
            self.save()

    def is_enabled(self, feature_name: str, channel_id: str) -> bool:
        """
        Returns if an automatic feature is enabled (In the enable list)
        """
        if not channel_id in self._data["channels"]:
            self.add_channel(channel_id)

        if feature_name in self._data["enabled_auto_features"] or feature_name in self._data["channels"][channel_id]["enabled_auto_features"]:
            return True
        else:
            return False
        


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

#===========================================================
# Data File Initialization #
#===========================================================

def init_guild_config(logging: bool = False) -> None:
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
            if logging:
                print(f"{cl.GREEN}{cl.BOLD}configdata/guildconfig.json{cl.END}{cl.GREEN} created :){cl.END}")
    except FileExistsError:
        if logging:
            print(f'{cl.YELLOW}{cl.BOLD}configdata/guildconfig.json{cl.END}{cl.YELLOW} exists. Skipping creation of file...{cl.END}')


def init_file(filename: str, logging: bool = False) -> None:
    """
    Creates a file specified.
    If filename does not exists, creates a blank file.
    Skips the process if filename exists.

    Parameters:
    filename (str): name of file to be created.
    logging (bool): option to make function print when file creation is successful or skipped.

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
    """
    Initializes a file as a json dictionary.
    Skips the process if filename exists.

    Parameters:
    filename (str): name of file to be created
    logging (bool): option to make function print when file creation is successful or skipped.

    Returns:
    none
    """
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
    """
    Adds keys to a json dictionary as dictionaries.
    
    """
    data: dict
    with open(filename, "r") as f:
                data = json.load(f)

    # Goes through each key and attempts to add each keyname as a dictionary
    for i in range(len(keynames)):
        try:
            if not keynames[i] in data:
                data[keynames[i]] = {}
        except Exception as e:
            print(f"{cl.GREY}{cl.BOLD}{str(datetime.now())[:-7]}{cl.RED} ERROR{cl.END}    Issue adding key as dictionary to {filename}: {e}")

    with open(filename, "w") as f:
                json.dump(data, f, indent = 2)


#===========================================================
# Textdata Handling
#===========================================================


def add_copypasta(text: str, logging: bool = False) -> None:
    # Checks if a given string is too long
    if len(text) > 1999:
        print(f"{cl.RED}Text is too long to fit in a discord message.{cl.END}")
        return

    with open("textdata/copypasta.dat", "a") as f:
        f.write(text + "\n\n")
        if logging:
            print(f"\n'{text}' added to textdata/copypasta.dat")


def delete_copypasta(index: int, logging: bool = False) -> None:
    try:
        copypastas = get_copypasta_list()
        copy = copypastas.pop(index)
        with open("textdata/copypasta.dat", "w") as f:
            for copies in copypastas:
                f.write(copies + "\n\n")
            if logging:
                print(f"'{copy}'removed from textdata/copypasta.dat")
    except IndexError:
        print(f"{cl.RED}Index number [{index}] not in range{cl.END}")


def get_json_dict(filename: str) -> dict:
    """
    Returns entire dictionary from JSON

    Parameters:
    filename (str): file to obtain dictionary from

    Returns:
    dict: JSON file as a dictionary
    """

    data: dict
    with open(filename, "r") as f:
                data = json.load(f)
    return data


def set_json_dict(filename: str, data: dict) -> None:
    """
    Takes a dictionary and sets a JSON as the dictionary.

    Parameters:
    filename (str): file to be modified
    data (dict): dictionary to be written to json

    Returns:
    none
    """
    with open(filename, "w") as f:
            json.dump(data, f, indent=2)


def add_fumo_url(name: str, url: str, logging: bool = False) -> None:
    """
    Adds a fumo image url to the file textdata/urls.json

    Parameters:
    name (str): name of fumo character
    url (str): url of the image of fumo

    Returns:
    none
    """
    data = get_json_dict("textdata/urls.json")
    try:
        if name in data["fumo"]:
            if not url in data["fumo"][name]:
                data["fumo"][name].append(url)
        else:
            data["fumo"][name] = [url]
        set_json_dict("textdata/urls.json", data)
        if logging:
            print(f"URL '{url}' added to collection of images for character '{name}'")
    except Exception as e:
        print(f"{cl.RED}ERROR: Issue adding fumo url: {e}{cl.END}")
    
    
def remove_fumo_url(name: str, index: int, logging: bool = False) -> None:
    """
    Removes a fumo image url from the file textdata/urls.json

    Parameters:
    name (str): name of fumo character
    index (int): index of url to be removed

    Returns:
    none
    """
    data = get_json_dict("textdata/urls.json")
    try:
        if name in data["fumo"]:
            data["fumo"][name].pop(index)
            set_json_dict("textdata/urls.json", data)
            print(f"URL at index [{index}] removed to collection of images for character '{name}'")
        else:
            print(f"{name} doesn't have any umage URL's")
    except IndexError:
        print(f"{cl.RED}ERROR: Index out of range{cl.END}")
    except Exception as e:
        print(f"{cl.RED}ERROR: Issue removing fumo url: {e}{cl.END}")


#===========================================================
# Miscellaneous #
#===========================================================

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
