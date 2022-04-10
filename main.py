import discord
from discord.ext import commands
import datahandling as dt


client = commands.Bot(command_prefix = '%')

@client.event
async def on_connect():
    print('I exist!')

@client.event
async def on_ready():
    print('I can talk to friends now! :)')

# Login information for the bot requires a token.
# token is taken from a file named 'token.dat'
# If this file does not exist, user will be prompted to input token
is_running = False

# TODO: Figure out how to recover from 'Improper token has been passed.' error
# Error turns into RuntimeError('Even loop is closed')
while(not is_running):
    try:
        TOKEN = dt.get_token()
        client.run(TOKEN)
        is_running = True
    except discord.LoginFailure as e:
        #This error is raised when the token is not valid
        print("[ERROR] Issue logging into bot:",e,'\n')
        print("The program will exit.")
        choice = input("Would you like to enter a new token? [Y/n] ")
        while(choice != "Y" and choice != "n"):
            choice = input("\nWould you like to write a new token? [Y/n] ")    
        if(choice == "Y"):
            TOKEN = input("Please enter bot token: ")
            dt.write_token(TOKEN)
        print("Terminating program...\n")
        exit()
    except Exception as e:
        print("[ERROR] Issue logging into bot:",e,'\n')
        print("Terminating program...\n")
        exit()
