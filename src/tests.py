"""
This is a file meant to test the functionality of various processes that the bot runs on.
"""
import os, logging
import datahandling as dt, helper as hlp, textfunctions as txtfunc

# Globally scoped variables to indicate how many tests passed, failed, and were skipped
skipped: int = 0
passed: int = 0
failed: int = 0

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def test(func: callable, skip: bool = False) -> None:
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


def guild_interface_init() -> None:
    pass

def guild_interface_guild_enable() -> None:
    pass

def guild_interface_guild_disable() -> None:
    pass

def guild_interface_channel_enable() -> None:
    pass

def guild_interface_channel_disable() -> None:
    pass


if __name__ == "__main__":
    test(guild_interface_init, skip = False)
    test(guild_interface_guild_enable, skip = True)
    test(guild_interface_guild_disable, skip = True)
    test(guild_interface_channel_enable, skip = True)
    test(guild_interface_channel_disable, skip = True)

    print(f"\n{hlp.cl.BOLD}Tests Complete\n=================={hlp.cl.END}")
    print(f"{hlp.cl.GREEN}Total successes:{hlp.cl.END}", passed)
    print(f"{hlp.cl.RED}Total failures: {hlp.cl.END}", failed)
    print(f"{hlp.cl.YELLOW}Total skips:    {hlp.cl.END}", skipped)

