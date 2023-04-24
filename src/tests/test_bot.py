import os, json, sys, pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Adds parent directory to PATH
import datahandling, helper
from main import client, tree
from test_utils import *

@pytest.mark.asyncio
async def test_on_message():
    """
    Tests default behavior when a message is sent and shouldn't be responded to
    """
    message = MockMessage("This is a test message")
    await client.on_message(message)
    assert(message.channel.sent_response == "")

    clean()

@pytest.mark.asyncio
async def test_on_message_dm():
    """
    Tests behavior when sent a message in a dm channel
    """
    message = MockMessage("Hello bot. What is going on with you? sus :smile:", is_dm = True)
    await client.on_message(message)
    assert(message.channel.sent_response == "Hi, I am a bot :)")

@pytest.mark.asyncio
async def test_on_message_bot_author():
    """
    Tests behavior when message sent by a bot
    """
    message = MockMessage("Hi user, what is going on today. Are you alright? This is just a test. Please do not be alarmed.", is_dm = True, is_bot = True)
    await client.on_message(message)
    assert(message.channel.sent_response == "")

@pytest.mark.asyncio
async def test_on_message_sus():
    """
    Tests 'sus' auto-feature
    """
    guild = datahandling.GuildProfile(string_guild_ids[0], helper.auto_features)

    message1 = MockMessage("sus", guild_id = integer_guild_ids[0], channel_id = integer_channel_ids[0])
    message2 = MockMessage("According to all known laws of aviation, there is no way a bee should be able to fly.", guild_id = integer_guild_ids[0], channel_id = integer_channel_ids[0])

    # Tests when sus is disabled
    await client.on_message(message1)
    await client.on_message(message2)

    assert(message1.channel.sent_response == "")
    assert(message2.channel.sent_response == "")

    # Tests when sus is enabled
    guild.guild_enable_auto("sus")
    await client.on_message(message1)
    await client.on_message(message2)

    assert(message1.channel.sent_response == "Amogus detected: ***sus***")
    assert(message2.channel.sent_response == "")

    # Tests when message is very large (charcount > 250)
    message3 = MockMessage("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwsus", guild_id = integer_guild_ids[0], channel_id = integer_channel_ids[0])
    await client.on_message(message3)

    assert(message3.channel.sent_response == message3.content)
    
    clean()
