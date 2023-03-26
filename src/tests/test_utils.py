import os, json, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Adds parent directory to PATH
from random import randint

# Collection of fake data used for testing. Discord IDs are longer than this, so these shouldn't conflict with any existing ids
integer_guild_ids = [randint(100000000000, 999999999999) for i in range(3)]
integer_channel_ids = [randint(100000000000, 999999999999) for i in range(3)]
integer_user_ids = [randint(100000000000, 999999999999) for i in range(3)]

string_guild_ids = list(map(str, integer_guild_ids))
string_channel_ids = list(map(str, integer_channel_ids))
string_user_ids = list(map(str, integer_user_ids))


def clean():
    """
    Removes temporary files created for function testing.
    """
    for guild_id in string_guild_ids:
        try:
            os.remove(f"./data/guild-profiles/{guild_id}.json")
        except FileNotFoundError:
            pass
    
    for user_id in string_user_ids:
        try:
            os.remove(f"./data/user-profiles/{user_id}.json")
        except FileNotFoundError:
            pass


def assertRaises(func: callable, err: Exception, *args, **kwargs):
    """
    Similar to the basic operator assert, assertRaises tests if a function with specific parameters throws a specific exception

    Arguments:
    - func: Function to be called
    - err: Exception to be raised
    - *args: Any arguments that should be 
    """
    try:
        func(*args, **kwargs)
    except err:
        return
    except Exception as e:
        raise AssertionError(f"Expected exception {err}, but {type(e)} raised")


def get_json_dict(filename: str) -> dict:
    """
    Returns dictionary from JSON
    """
    data: dict
    with open(filename, "r") as f:
                data = json.load(f)
    return data
