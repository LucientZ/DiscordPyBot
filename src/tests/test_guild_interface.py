import os, json, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Adds parent directory to PATH
import datahandling as dt, helper as hlp
from test_utils import *


def test_guild_interface_init_string_id() -> None:
    """
    Tests behavior when guild profile is initialized with a string as an id.
    """
    guild1 = dt.GuildProfile(string_guild_ids[0], hlp.auto_features)
    guild2 = dt.GuildProfile(string_guild_ids[1], hlp.auto_features)
    
    
    # Makes sure both objects initialized correctly
    assert(guild1.get_data()["enabled_auto_features"] == [])
    assert(guild1.get_data()["channels"] == {})
    assert(guild1.get_id() == string_guild_ids[0])
    assert(guild2.get_data()["enabled_auto_features"] == [])
    assert(guild2.get_data()["channels"] == {})
    assert(guild2.get_id() == string_guild_ids[1])

    assert(guild1 != guild2)
    guild2.get_data()["enabled_auto_features"].append("test")
    assert(guild1.get_data() != guild2.get_data())

    guild2.load(string_guild_ids[0])
    assert(guild2.get_id() == string_guild_ids[0])

    assert(guild1.get_data() == guild2.get_data())
    assert(get_json_dict(f"./data/guild-profiles/{string_guild_ids[0]}.json") == guild1.get_data())
    assert(get_json_dict(f"./data/guild-profiles/{string_guild_ids[1]}.json") == guild2.get_data())
    clean()


def test_guild_interface_init_integer_id() -> None:
    """
    Tests behavior when guild profile is initialized with an integer as an id. Note that the id should be saved as a string.
    """
    guild1 = dt.GuildProfile(integer_guild_ids[0], hlp.auto_features)
    guild2 = dt.GuildProfile(integer_guild_ids[1], hlp.auto_features)
    
    
    # Makes sure both objects initialized correctly
    assert(guild1.get_data()["enabled_auto_features"] == [])
    assert(guild1.get_data()["channels"] == {})
    assert(guild1.get_id() == string_guild_ids[0])
    assert(guild2.get_data()["enabled_auto_features"] == [])
    assert(guild2.get_data()["channels"] == {})
    assert(guild2.get_id() == string_guild_ids[1])

    assert(guild1 != guild2)
    guild2.get_data()["enabled_auto_features"].append("test")
    assert(guild1.get_data() != guild2.get_data())

    guild2.load(integer_guild_ids[0])
    assert(guild2.get_id() == string_guild_ids[0])

    assert(guild1.get_data() == guild2.get_data())
    assert(get_json_dict(f"./data/guild-profiles/{integer_guild_ids[0]}.json") == guild1.get_data())
    assert(get_json_dict(f"./data/guild-profiles/{integer_guild_ids[1]}.json") == guild2.get_data())
    clean()

    
def test_guild_interface_add_channel() -> None:
    """
    Tests behavior when channel is added
    """
    guild = dt.GuildProfile(string_guild_ids[0], hlp.auto_features)

    guild.add_channel(string_channel_ids[0])
    assert(guild.get_data()["channels"][string_channel_ids[0]] == {"enabled_auto_features": []})

    guild.add_channel(string_channel_ids[0])
    assert(guild.get_data()["channels"][string_channel_ids[0]] == {"enabled_auto_features": []})
    assert(get_json_dict(f"./data/guild-profiles/{string_guild_ids[0]}.json") == guild.get_data())
    clean()


def test_guild_interface_guild_enable_auto() -> None:
    guild = dt.GuildProfile(string_guild_ids[0], hlp.auto_features)

    guild.guild_enable_auto("sad") # Should add to enable list
    guild.guild_enable_auto("sad") # Should NOT add again to enable list

    assertRaises(guild.guild_enable_auto, ValueError, "not-real-command")
    assertRaises(guild.guild_enable_auto, ValueError, "")

    assert(guild.get_data()["enabled_auto_features"] == ["sad"])
    assert(get_json_dict(f"./data/guild-profiles/{string_guild_ids[0]}.json") == guild.get_data())
    clean()


def test_guild_interface_guild_disable_auto() -> None:
    guild = dt.GuildProfile(string_guild_ids[0], hlp.auto_features)
    enabled_features = []

    # Enable all features iteratively
    for feature in hlp.auto_features:
        guild.guild_enable_auto(feature)
        enabled_features.append(feature)
        assert(guild.get_data()["enabled_auto_features"] == enabled_features)
    
    # Disable all features iteratively in reverse
    for feature in reversed(hlp.auto_features):
        guild.guild_disable_auto(feature)
        enabled_features.remove(feature)
        assert(guild.get_data()["enabled_auto_features"] == enabled_features)

    # Attempts to disable all features again to see if any errors are thrown
    for feature in reversed(hlp.auto_features):
        guild.guild_disable_auto(feature)
        assert(guild.get_data()["enabled_auto_features"] == [])

    assert(get_json_dict(f"./data/guild-profiles/{string_guild_ids[0]}.json") == guild.get_data())
    clean()


def test_guild_interface_channel_enable_auto() -> None:
    guild = dt.GuildProfile(string_guild_ids[0], hlp.auto_features)
    guild.add_channel(string_channel_ids[0])

    guild.channel_enable_auto("sad", string_channel_ids[0])
    guild.channel_enable_auto("sad", string_channel_ids[0])

    assertRaises(guild.channel_enable_auto, ValueError, "not_A-real_commAnD", string_channel_ids[0])
    assertRaises(guild.channel_enable_auto, ValueError, "", string_channel_ids[0])

    assert(guild.get_data()["channels"][string_channel_ids[0]]["enabled_auto_features"] == ["sad"])

    assert(get_json_dict(f"./data/guild-profiles/{string_guild_ids[0]}.json") == guild.get_data())

    # Same behavior with a channel that wasn't already added to the server
    guild.channel_enable_auto("sus", string_channel_ids[1])
    guild.channel_enable_auto("sad", string_channel_ids[1])
    guild.channel_enable_auto("sad", string_channel_ids[1])

    assertRaises(guild.channel_enable_auto, ValueError, "not_A-real_commAnD", string_channel_ids[1])
    assertRaises(guild.channel_enable_auto, ValueError, "", string_channel_ids[1])

    assert(guild.get_data()["channels"][string_channel_ids[0]]["enabled_auto_features"] == ["sad"])
    assert(guild.get_data()["channels"][string_channel_ids[1]]["enabled_auto_features"] == ["sus", "sad"])

    assert(get_json_dict(f"./data/guild-profiles/{string_guild_ids[0]}.json") == guild.get_data())

    # is_enabled for channel that doesn't exist
    assert(guild.is_enabled("sus", "40927384575") == False)

    clean()


def test_guild_interface_channel_disable_auto() -> None:
    guild = dt.GuildProfile(string_guild_ids[0], hlp.auto_features)
    guild.add_channel(string_channel_ids[0])
    enabled_features = []

    # Enable all features iteratively
    for feature in hlp.auto_features:
        guild.channel_enable_auto(feature, string_channel_ids[0])
        enabled_features.append(feature)
        assert(guild.get_data()["channels"][string_channel_ids[0]]["enabled_auto_features"] == enabled_features)
    
    # Disable all features iteratively in reverse
    for feature in reversed(hlp.auto_features):
        guild.channel_disable_auto(feature, string_channel_ids[0])
        enabled_features.remove(feature)
        assert(guild.get_data()["channels"][string_channel_ids[0]]["enabled_auto_features"] == enabled_features)

    # Attempts to disable all features again to see if any errors are thrown
    for feature in reversed(hlp.auto_features):
        guild.channel_disable_auto(feature, string_channel_ids[0])
        assert(guild.get_data()["channels"][string_channel_ids[0]]["enabled_auto_features"] == [])

    assert(get_json_dict(f"./data/guild-profiles/{string_guild_ids[0]}.json") == guild.get_data())

    # Disable for channel that doesn't exist
    guild.channel_disable_auto("sus", string_channel_ids[1])

    clean()


def test_guild_interface_is_enabled() -> None:
    """
    Test the behavior of GuildProfile.is_enabled()
    """
    guild = dt.GuildProfile(string_guild_ids[0], hlp.auto_features)
    for feature in hlp.auto_features:
        assert(feature in guild.get_valid_features())

    guild.channel_enable_auto("sad", string_channel_ids[0])
    guild.channel_enable_auto("sus", string_channel_ids[1])

    guild.guild_enable_auto("sad")
    guild.guild_disable_auto("sus")

    assert(guild.get_guild_enabled_features() == ["sad"])
    assert(guild.get_channel_enabled_features(string_channel_ids[0]) == ["sad"])
    assert(guild.get_channel_enabled_features(string_channel_ids[1]) == ["sus"])
    assert(guild.is_enabled("sad", string_channel_ids[0]))
    assert(not guild.is_enabled("trade", string_channel_ids[0]))
    assert(not guild.is_enabled("sus", string_channel_ids[0]))
    assert(guild.is_enabled("sad", string_channel_ids[1]))
    assert(guild.is_enabled("sus", string_channel_ids[1]))

    guild.channel_enable_auto("trade", string_channel_ids[0])

    assert(guild.get_guild_enabled_features() == ["sad"])
    assert(guild.get_channel_enabled_features(string_channel_ids[0]) == ["sad", "trade"])
    assert(guild.get_channel_enabled_features(string_channel_ids[1]) == ["sus"])
    assert(guild.is_enabled("sad", string_channel_ids[0]))
    assert(guild.is_enabled("trade", string_channel_ids[0]))
    assert(not guild.is_enabled("sus", string_channel_ids[0]))
    assert(guild.is_enabled("sad", string_channel_ids[1]))
    assert(guild.is_enabled("sus", string_channel_ids[1]))
    assert(not guild.is_enabled("trade", string_channel_ids[1]))

    clean()

def test_guild_profile_getting_features_unknown_channel() -> None:
    """
    Test behavior when attempting to obtain valid features from an unknown channel
    """
    
    guild = dt.GuildProfile(string_guild_ids[0])

    assert(guild.get_channel_enabled_features(string_channel_ids[1]) == [])

def test_guild_interface_malformed_json() -> None:
    """
    Tests if malformed data is handled correctly.
    
    If the data in the dictionary does not have a key that is in the template data, the GuildProfile object should add the key. Keys that aren't in the object should 
    """
    malformed_guild_format = {
        "enabled_auto_features" : [],
        "Cool_data" : [1,2,3,4]
    }

    with open(f"data/guild-profiles/{string_guild_ids[0]}.json", "w") as f:
            json.dump(malformed_guild_format, f, indent=2)
    
    guild = dt.GuildProfile(string_guild_ids[0], hlp.auto_features)

    assert(guild.get_data() == {"enabled_auto_features" : [], "Cool_data" : [1,2,3,4], "channels" : {}})

    clean()