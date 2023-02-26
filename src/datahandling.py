import helper as hlp
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
        

#===========================================================
# Data File Initialization #
#===========================================================

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
                print(f"{hlp.cl.GREEN}{hlp.cl.BOLD}{filename}{hlp.cl.END}{hlp.cl.GREEN} created.{hlp.cl.END}")
    except FileExistsError:
        if logging:
            print(f'{hlp.cl.YELLOW}{hlp.cl.BOLD}{filename}{hlp.cl.END}{hlp.cl.YELLOW} exists. Skipping creation of file...{hlp.cl.END}')

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
                print(f"{hlp.cl.GREEN}{hlp.cl.BOLD}{filename}{hlp.cl.END}{hlp.cl.GREEN} created.{hlp.cl.END}")
    except FileExistsError:
        if logging:
            print(f'{hlp.cl.YELLOW}{hlp.cl.BOLD}{filename}{hlp.cl.END}{hlp.cl.YELLOW} exists. Skipping creation of file...{hlp.cl.END}')


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
            print(f"{hlp.cl.GREY}{hlp.cl.BOLD}{str(datetime.now())[:-7]}{hlp.cl.RED} ERROR{hlp.cl.END}    Issue adding key as dictionary to {filename}: {e}")

    with open(filename, "w") as f:
                json.dump(data, f, indent = 2)


#===========================================================
# Textdata Handling
#===========================================================


def add_copypasta(text: str, logging: bool = False) -> None:
    # Checks if a given string is too long
    if len(text) > 1999:
        print(f"{hlp.cl.RED}Text is too long to fit in a discord message.{hlp.cl.END}")
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
        print(f"{hlp.cl.RED}Index number [{index}] not in range{hlp.cl.END}")


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
        print(f"{hlp.cl.RED}ERROR: Issue adding fumo url: {e}{hlp.cl.END}")
    
    
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
        print(f"{hlp.cl.RED}ERROR: Index out of range{hlp.cl.END}")
    except Exception as e:
        print(f"{hlp.cl.RED}ERROR: Issue removing fumo url: {e}{hlp.cl.END}")


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
