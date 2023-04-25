import os, json, sys, dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Adds parent directory to PATH
import random, discord
from typing import Union, Sequence

# Collection of fake data used for testing. Discord IDs are longer than this, so these shouldn't conflict with any existing ids
integer_guild_ids = random.sample(range(100000000000, 999999999999), 3)
integer_channel_ids = random.sample(range(100000000000, 999999999999), 3)
integer_user_ids = random.sample(range(100000000000, 999999999999), 3)
integer_interaction_ids = random.sample(range(100000000000, 999999999999), 3)          

string_guild_ids = list(map(str, integer_guild_ids))
string_channel_ids = list(map(str, integer_channel_ids))
string_user_ids = list(map(str, integer_user_ids))
string_interaction_ids = list(map(str, integer_interaction_ids))


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


class MockMessage(discord.message.Message):
    """
    Class used for mimicking a discord message in order to test the bot.
    """
    class MockGuild(discord.Guild):
        def __init__(self, *, id: int = 0):
            self.id: int = id

    class MockAuthor(discord.User):
        def __init__(self, *, bot: bool = False):
            self.bot = bot

    class MockTextChannel(discord.channel.TextChannel):
        def __init__(self, *, id: int = 0):
            self.id: int = id
            self.sent_response: str = ""

        async def send(self, 
                 content: Union[str, None],
                 *, 
                 tts: bool = False, 
                 embed: discord.Embed = None, 
                 file: discord.File = None, 
                 stickers: Sequence[Union[discord.GuildSticker, discord.StickerItem]] = None, 
                 delete_after: float = 0, 
                 nonce: Union[str, int] = None, 
                 allowed_mentions: discord.AllowedMentions = None, 
                 reference: Union[discord.Message, discord.MessageReference, discord.PartialMessage] = None, 
                 mention_author: bool = False, 
                 view: discord.ui.View = None, 
                 suppress_embeds: bool = False, 
                 silent: bool = False) -> discord.Message:
            self.sent_response = content

    class MockDMChannel(discord.channel.DMChannel):
        def __init__(self, *, id: int = 0):
            self.id: int = id
            self.sent_response: str = ""

        async def send(self, 
                 content: Union[str, None],
                 *, 
                 tts: bool = False, 
                 embed: discord.Embed = None, 
                 file: discord.File = None, 
                 stickers: Sequence[Union[discord.GuildSticker, discord.StickerItem]] = None, 
                 delete_after: float = 0, 
                 nonce: Union[str, int] = None, 
                 allowed_mentions: discord.AllowedMentions = None, 
                 reference: Union[discord.Message, discord.MessageReference, discord.PartialMessage] = None, 
                 mention_author: bool = False, 
                 view: discord.ui.View = None, 
                 suppress_embeds: bool = False, 
                 silent: bool = False) -> discord.Message:
            self.sent_response = content

    def __init__(self, content: str, *, guild_id: int = 0, channel_id: int = 0, is_dm: bool = False, is_bot = False):
        self.author = MockMessage.MockAuthor(bot = is_bot)
        self.guild = MockMessage.MockGuild(id = guild_id)
        if(is_dm):
            self.channel = MockMessage.MockDMChannel(id = channel_id)
        else:
            self.channel = MockMessage.MockTextChannel(id = channel_id)
        self.content = content

    def __str__(self):
        return self.content

