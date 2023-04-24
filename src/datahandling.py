import json, os
from helper import cl, Logger
from datetime import datetime
from typing import Union

#===========================================================
# JSON Profile Handling Classes
#===========================================================

class JSONProfileInterface(): # pragma: no cover
    def load(self, id: Union[str, int]):
        """
        Loads data from a given JSON file
        """
        pass

    def save(self, id: Union[str, int]):
        """
        Saves data from to given JSON file
        """
        pass

    def get_data(self):
        """
        Returns the dictionary equivalent of the data obtained from a JSON profile
        """
        pass


class UserProfile(JSONProfileInterface):
    def __init__(self, user_id: Union[str, int]) -> None:
        self._user_id: str = str(user_id)
        self._data: dict
        try:
            self.load(self._user_id)
        except Exception as e:
            raise ValueError(f"Issue initializing UserProfile object with id '{self._user_id}':\n{e}")

    def load(self, user_id: Union[str, int]) -> None:
        """
        Loads dictionary from JSON file into profile 

        If file doesn't exist, creates said file
        """
        data_template = {
            "username": "",
            "id": str(user_id)
        }
        
        if(os.path.isfile(f"data/guild-profiles/{user_id}.json")):
            with open(f"data/guild-profiles/{user_id}.json", "r") as f:
                self._data: dict = json.load(f)
        else:
            self._data = data_template
        
        # Deals with malformed data or data that hasn't been updated to the current template
        for key in data_template:
            if not key in self._data:
                self._data[key] = data_template[key]
        self.save()

        self.user_id = str(user_id)

    def save(self) -> None:
        """
        Saves _data dictionary into the user's respective json
        """
        with open(f"data/user-profiles/{self._user_id}.json", "w") as f:
            json.dump(self._data, f, indent=2)

    # Accessor Methods

    def get_username(self) -> str:
        """
        Returns username stored in data dictionary
        """
        return self._data["username"]
    
    def get_data(self) -> dict:
        """
        Returns data dictionary
        """
        return self._data
    
    def get_id(self) -> str:
        """
        Returns user id (string)
        """
        return self._user_id

    # Mutator Methods

    def set_username(self, username: str):
        self._data["username"] = str(username)
        self.save()
    

class GuildProfile(JSONProfileInterface):
    """
    Interface used for modifying and obtaining guild config information
    """
    def __init__(self, guild_id: Union[str, int], valid_features: list = []) -> None:
        self._data: dict
        self._guild_id: str = str(guild_id)
        self._valid_features: list = valid_features
        try:
            self.load(self._guild_id)
        except Exception as e:
            raise ValueError(f"Issue initializing GuildProfile object with id '{self._guild_id}':\n{e}")

    def load(self, guild_id: Union[str, int]) -> None:
        """
        Loads dictionary from JSON file into interface 
        
        If file doesn't exist, creates said file
        """

        data_template = {
            "enabled_auto_features" : [],
            "channels": {},
            "id": str(guild_id)
        }

        if(os.path.isfile(f"data/guild-profiles/{guild_id}.json")):
            with open(f"data/guild-profiles/{guild_id}.json", "r") as f:
                self._data: dict = json.load(f)
        else:
            self._data = data_template
        
        # Deals with malformed data or data that hasn't been updated to the current template
        for key in data_template:
            if not key in self._data:
                self._data[key] = data_template[key]
        self.save()

        self._guild_id = str(guild_id)

    def save(self) -> None:
        """
        Saves _data dictionary into the guild's respective json
        """
        with open(f"data/guild-profiles/{self._guild_id}.json", "w") as f:
            json.dump(self._data, f, indent=2)
    
    # Accessor methods

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
    
    def get_channel_enabled_features(self, channel_id: Union[str, int]) -> list:
        """
        Returns a list of valid features in the specific channel
        """
        channel_id = str(channel_id)

        if not channel_id in self._data["channels"]:
            self.add_channel(channel_id)
        
        return self._data["channels"][channel_id]["enabled_auto_features"]
    
    # Mutator methods

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

    def add_channel(self, channel_id: Union[str, int]) -> None:
        """
        Adds a channel to the collection of channels in the guild
        """
        channel_id = str(channel_id)

        if not channel_id in self._data["channels"]:
            channel_data: dict = {
                "enabled_auto_features" : []
            }
            self._data["channels"][channel_id] = channel_data
            self.save()

    def channel_enable_auto(self, feature_name: str, channel_id: Union[str, int]) -> None:
        """
        Enables an automatic feature in a specific channel in a guild
        """
        channel_id = str(channel_id)

        if not feature_name in self._valid_features:
            raise ValueError("Not a valid feature to enable")
        elif not channel_id in self._data["channels"]:
            self.add_channel(channel_id)
        
        if not (feature_name in self._data["channels"][channel_id]["enabled_auto_features"]):
            self._data["channels"][channel_id]["enabled_auto_features"].append(feature_name)
            self.save()

    def channel_disable_auto(self, feature_name: str, channel_id: Union[str, int]):
        """
        Disables an automatic feature in a specific channel in a guild
        """
        channel_id = str(channel_id)

        if not channel_id in self._data["channels"]:
            self.add_channel(channel_id)

        if feature_name in self._valid_features and channel_id in self._data["channels"] and (feature_name in self._data["channels"][channel_id]["enabled_auto_features"]):
            self._data["channels"][channel_id]["enabled_auto_features"].remove(feature_name)
            self.save()

    def is_enabled(self, feature_name: str, channel_id: Union[str, int]) -> bool:
        """
        Returns if an automatic feature is enabled (In the enable list)
        """
        channel_id = str(channel_id)

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
                Logger.log_info(f"{filename} created.")
    except FileExistsError:
        if logging:
            Logger.log_info(f"{filename} exists. Skipping creation of file...")


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
                Logger.log_info(f"{filename} created.")
    except FileExistsError:
        if logging:
            Logger.log_info(f"{filename} exists. Skipping creation of file...")


def add_json_dict_keys(filename: str, *keynames: str):
    """
    Adds keys to a json dictionary as dictionaries.
    
    """
    data: dict
    with open(filename, "r") as f:
                data = json.load(f)

    # Goes through each key and attempts to add each keyname as a dictionary
    for key in keynames:
        try:
            if not key in data:
                data[key] = {}
        except Exception as e:
            Logger.log_warning(f"Issue adding key as dictionary to {filename}: {e}")

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

    with open("data/textdata/copypasta.dat", "a") as f:
        f.write(text + "\n\n")
        if logging:
            print(f"\n'{text}' added to data/textdata/copypasta.dat")


def delete_copypasta(index: int, logging: bool = False) -> None:
    try:
        copypastas = get_copypasta_list()
        copy = copypastas.pop(index)
        with open("data/textdata/copypasta.dat", "w") as f:
            for copies in copypastas:
                f.write(copies + "\n\n")
            if logging:
                print(f"'{copy}'removed from data/textdata/copypasta.dat")
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
    Adds a fumo image url to the file data/textdata/urls.json

    Parameters:
    name (str): name of fumo character
    url (str): url of the image of fumo

    Returns:
    none
    """
    data = get_json_dict("data/textdata/urls.json")
    try:
        if name in data["fumo"]:
            if not url in data["fumo"][name]:
                data["fumo"][name].append(url)
        else:
            data["fumo"][name] = [url]
        set_json_dict("data/textdata/urls.json", data)
        if logging:
            Logger.log_info(f"URL '{url}' added to collection of images for character '{name}'")
    except Exception as e:
        Logger.log_error(f"Issue adding fumo url: {e}")
    
    
def remove_fumo_url(name: str, index: int, logging: bool = False) -> None:
    """
    Removes a fumo image url from the file data/textdata/urls.json

    Parameters:
    name (str): name of fumo character
    index (int): index of url to be removed

    Returns:
    none
    """
    data = get_json_dict("data/textdata/urls.json")
    try:
        if name in data["fumo"]:
            data["fumo"][name].pop(index)
            set_json_dict("data/textdata/urls.json", data)
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
    with open("data/textdata/copypasta.dat", "r") as f:
        data = f.read()
        data = data.split('\n\n')
        data.pop(len(data) - 1)
        i = 0
        for copy in data:
            copy = copy.replace("\\n","\n")
            data[i] = copy
            i += 1
        return data
