"""
This is a file meant to test the functionality of various processes that the bot runs on.
"""
import os, logging, json
import datahandling as dt, helper as hlp, textfunctions as txtfunc

# Globally scoped variables to indicate how many tests passed, failed, and were skipped
skipped: int = 0
passed: int = 0
failed: int = 0

# Collection of fake data used for testing.
test_guild_ids = ["1234567890", "0987654321", "089764534231"]
test_channel_ids = ["132435465768709", "1093274389237532"]
test_user_ids = ["234987253856239", "2194873285608792"]

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def test(func: callable, skip: bool = False) -> None:
    """
    Test whether a function throws an error or not when called. Increments skipped, passed, or failed global variables depending on the result.
    """
    global skipped
    global passed
    global failed
    if(skip):
        print(f"{hlp.cl.YELLOW}[SKIP]{hlp.cl.END} {func.__name__}() skipped")
        skipped += 1
        return
    try:
        func()
        print(f"{hlp.cl.GREEN}[PASS]{hlp.cl.END} {func.__name__}() passed")
        passed += 1
    except AssertionError as err:
        print(f"{hlp.cl.RED}[FAIL]{hlp.cl.END} incorrect value in function {func.__name__}()")
        logger.exception(err)
        failed += 1
    except Exception as err:
        print(f"{hlp.cl.RED}[FAIL]{hlp.cl.END} error in function {func.__name__}()")
        logger.exception(err)
        failed += 1
    clean()


def clean():
    """
    Removes temporary files created for function testing.
    """
    for guild_id in test_guild_ids:
        try:
            os.remove(f"./data/guild-profiles/{guild_id}.json")
        except FileNotFoundError:
            pass
        except Exception as err:
            print(f"{hlp.cl.RED}[ERROR]{hlp.cl.END} There was an issue removing temporary guild profile file {guild_id}.json")
            logger.exception(err)
    
    for user_id in test_user_ids:
        try:
            os.remove(f"./data/user-profiles/{user_id}.json")
        except FileNotFoundError:
            pass
        except Exception as err:
            print(f"{hlp.cl.RED}[ERROR]{hlp.cl.END} There was an issue removing temporary user profile file {guild_id}.json")
            logger.exception(err)


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


def guild_interface_init() -> None:
    """
    Tests behavior when guild profile is initialized.
    """
    guild1 = dt.GuildProfile(test_guild_ids[0], hlp.all_features)
    guild2 = dt.GuildProfile(test_guild_ids[1], hlp.all_features)
    
    
    # Makes sure both objects initialized correctly
    assert(guild1.get_data()["enabled_auto_features"] == [])
    assert(guild1.get_data()["channels"] == {})
    assert(guild1.get_id() == test_guild_ids[0])
    assert(guild2.get_data()["enabled_auto_features"] == [])
    assert(guild2.get_data()["channels"] == {})
    assert(guild2.get_id() == test_guild_ids[1])

    assert(guild1 != guild2)
    guild2.get_data()["enabled_auto_features"].append("test")
    assert(guild1.get_data() != guild2.get_data())

    guild2.load(test_guild_ids[0])
    assert(guild2.get_id() == test_guild_ids[0])

    assert(guild1.get_data() == guild2.get_data())
    assert(get_json_dict(f"./data/guild-profiles/{test_guild_ids[0]}.json") == guild1.get_data())
    assert(get_json_dict(f"./data/guild-profiles/{test_guild_ids[1]}.json") == guild2.get_data())

    
def guild_interface_add_channel() -> None:
    """
    Tests behavior when channel is added
    """
    guild = dt.GuildProfile(test_guild_ids[0], hlp.all_features)

    guild.add_channel(test_channel_ids[0])
    assert(guild.get_data()["channels"][test_channel_ids[0]] == {"enabled_auto_features": []})

    guild.add_channel(test_channel_ids[0])
    assert(guild.get_data()["channels"][test_channel_ids[0]] == {"enabled_auto_features": []})
    assert(get_json_dict(f"./data/guild-profiles/{test_guild_ids[0]}.json") == guild.get_data())


def guild_interface_guild_enable_auto() -> None:
    guild = dt.GuildProfile(test_guild_ids[0], hlp.all_features)

    guild.guild_enable_auto("fumo") # Should add to enable list
    guild.guild_enable_auto("fumo") # Should NOT add again to enable list

    assertRaises(guild.guild_enable_auto, ValueError, "not-real-command")
    assertRaises(guild.guild_enable_auto, ValueError, "")

    assert(guild.get_data()["enabled_auto_features"] == ["fumo"])
    assert(get_json_dict(f"./data/guild-profiles/{test_guild_ids[0]}.json") == guild.get_data())


def guild_interface_guild_disable_auto() -> None:
    guild = dt.GuildProfile(test_guild_ids[0], hlp.all_features)
    enabled_features = []

    # Enable all features iteratively
    for feature in hlp.all_features:
        guild.guild_enable_auto(feature)
        enabled_features.append(feature)
        assert(guild.get_data()["enabled_auto_features"] == enabled_features)
    
    # Disable all features iteratively in reverse
    for feature in reversed(hlp.all_features):
        guild.guild_disable_auto(feature)
        enabled_features.remove(feature)
        assert(guild.get_data()["enabled_auto_features"] == enabled_features)

    # Attempts to disable all features again to see if any errors are thrown
    for feature in reversed(hlp.all_features):
        guild.guild_disable_auto(feature)
        assert(guild.get_data()["enabled_auto_features"] == [])

    assert(get_json_dict(f"./data/guild-profiles/{test_guild_ids[0]}.json") == guild.get_data())


def guild_interface_channel_enable_auto() -> None:
    guild = dt.GuildProfile(test_guild_ids[0], hlp.all_features)
    guild.add_channel(test_channel_ids[0])

    guild.channel_enable_auto("fumo", test_channel_ids[0])
    guild.channel_enable_auto("fumo", test_channel_ids[0])

    assertRaises(guild.channel_enable_auto, ValueError, "not_A-real_commAnD", test_channel_ids[0])
    assertRaises(guild.channel_enable_auto, ValueError, "", test_channel_ids[0])

    assert(guild.get_data()["channels"][test_channel_ids[0]]["enabled_auto_features"] == ["fumo"])

    assert(get_json_dict(f"./data/guild-profiles/{test_guild_ids[0]}.json") == guild.get_data())

    # Same behavior with a channel that wasn't already added to the server
    guild.channel_enable_auto("sad", test_channel_ids[1])
    guild.channel_enable_auto("fumo", test_channel_ids[1])
    guild.channel_enable_auto("fumo", test_channel_ids[1])

    assertRaises(guild.channel_enable_auto, ValueError, "not_A-real_commAnD", test_channel_ids[1])
    assertRaises(guild.channel_enable_auto, ValueError, "", test_channel_ids[1])

    assert(guild.get_data()["channels"][test_channel_ids[0]]["enabled_auto_features"] == ["fumo"])
    assert(guild.get_data()["channels"][test_channel_ids[1]]["enabled_auto_features"] == ["sad", "fumo"])

    assert(get_json_dict(f"./data/guild-profiles/{test_guild_ids[0]}.json") == guild.get_data())



def guild_interface_channel_disable_auto() -> None:
    guild = dt.GuildProfile(test_guild_ids[0], hlp.all_features)
    guild.add_channel(test_channel_ids[0])
    enabled_features = []

    # Enable all features iteratively
    for feature in hlp.all_features:
        guild.channel_enable_auto(feature, test_channel_ids[0])
        enabled_features.append(feature)
        assert(guild.get_data()["channels"][test_channel_ids[0]]["enabled_auto_features"] == enabled_features)
    
    # Disable all features iteratively in reverse
    for feature in reversed(hlp.all_features):
        guild.channel_disable_auto(feature, test_channel_ids[0])
        enabled_features.remove(feature)
        assert(guild.get_data()["channels"][test_channel_ids[0]]["enabled_auto_features"] == enabled_features)

    # Attempts to disable all features again to see if any errors are thrown
    for feature in reversed(hlp.all_features):
        guild.channel_disable_auto(feature, test_channel_ids[0])
        assert(guild.get_data()["channels"][test_channel_ids[0]]["enabled_auto_features"] == [])

    assert(get_json_dict(f"./data/guild-profiles/{test_guild_ids[0]}.json") == guild.get_data())


if __name__ == "__main__":
    test(guild_interface_init)
    test(guild_interface_add_channel)
    test(guild_interface_guild_enable_auto)
    test(guild_interface_guild_disable_auto)
    test(guild_interface_channel_enable_auto)
    test(guild_interface_channel_disable_auto)

    # Cleans up any possible stray files
    clean()

    print(f"\n{hlp.cl.BOLD}Tests Complete\n=================={hlp.cl.END}")
    print(f"{hlp.cl.GREEN}Total successes:{hlp.cl.END}", passed)
    print(f"{hlp.cl.RED}Total failures: {hlp.cl.END}", failed)
    print(f"{hlp.cl.YELLOW}Total skips:    {hlp.cl.END}", skipped)

