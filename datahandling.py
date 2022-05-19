from helper import *
import json

##################
# TOKEN HANDLING #
##################

def write_token(TOKEN) -> None:
    """
    Writes a token to .token.
    If .token does not exist, creates .token and writes the token.

    Parameters:
    TOKEN (str): Token to be written to file

    Returns:
    None
    """
    tokenfile = open(".token", "w")
    tokenfile.write(TOKEN)
    tokenfile.close()

def get_token() -> str:
    """
    Obtains token from a file named '.token' or from the user.
    If '.token' does not have a token or is empty, asks the user if they would like to write to '.token'

    Parameters:
    None

    Returns:
    str: token to be used by bot
    """
    # Initializes TOKEN and choice as strings
    TOKEN = ""
    choice = ""

    #At the moment, this code assumes the only error is .token not existing
    try:
        # opens up .token which should only contain the bot token
        with open('.token') as tokenfile:
            print(f"Logging in with TOKEN from {cl.BOLD}.token{cl.END}")
            TOKEN = tokenfile.read()

            if(TOKEN == ""):
                # If TOKEN == "", this means that .token is empty
                
                while(choice != "Y" and choice != "n"):
                    choice = input(f"\nIt looks like there isn't anything in {cl.BOLD}'.token'{cl.END}.\nWould you like to add a token to this file? (It is recommended that this is done manually) [Y/n] ")
                
                if(choice == 'Y'):
                    TOKEN = input('\nPlease enter the bot token: ')
                    write_token(TOKEN)
                else:
                    print(f"\nNo token will be added to {cl.BOLD}'.token'{cl.end}")
                    TOKEN = input('Please enter the bot token: ')                
    except:
        # Handling when .token does not exist.
        while(choice != "Y" and choice != "n"):
            choice = input(f"\nIt looks like there isn't a file named {cl.BOLD}'.token'{cl.END} in this directory.\nWould you like to create this file? [Y/n] ")

        if(choice == 'Y'):
            TOKEN = input('\nPlease enter the bot token: ')
            write_token(TOKEN)
        else:
            print("\n.dat will not be created")
            TOKEN = input('Please enter the bot token: ')

        
    return TOKEN


##########################
# Server Config Handling #
##########################

def init_guild_config():
    """
    If configdata\guildconfig.json does not exists, creates a template file.
    Skips the process if configdata\guildconfig.json exists.

    Parameters:
    None

    Returns:
    None
    """
    try:
        with open("configdata\guildconfig.json", "x") as f:
            data = {
                "guilds": dict()
            }
            # Example guild with restrictions on certain commands and features
            data["guilds"]["00000000"] ={
                "blacklist": ["sus", "morbius", "funky"],
                "channels": {"00000000": {"blacklist": ["copypasta"]}, "00000001": {"blacklist": ["sad"]}}
            }
            json.dump(data, f, indent=2)
            print(f"{cl.GREEN}{cl.BOLD}configdata\guildconfig.json{cl.END}{cl.GREEN} created :){cl.END}")
    except FileExistsError as e:
        print(f'{cl.BOLD}{cl.YELLOW}\configdata\guildconfig.json{cl.END}{cl.YELLOW} exists. Skipping creation of file...{cl.END}')




print(f"{cl.GREEN}{cl.BOLD}datahandling.py{cl.END}{cl.GREEN} initialized{cl.END}")
