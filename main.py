import discord
from discord.ext import commands
import datahandling as dt
from textfunctions import *

client = commands.Bot(command_prefix = '%')

@client.event
async def on_connect():
    print('I exist!')

@client.event
async def on_ready():
    print('I can talk to friends now! :)')

@client.event
async def on_message(message):
    #Bot doesn't respond to itself
    if message.author == client.user:
        return

    if 'morbius' in message.content.lower():
        await message.channel.send(morbius())





# Login information for the bot requires a token.
# token is taken from a file named 'token.dat'
# If this file does not exist, user will be prompted to input token

# TODO: Figure out how to recover from 'Improper token has been passed.' error
# Error turns into RuntimeError('Even loop is closed')
def main():
    try:
        TOKEN = dt.get_token()
        client.run(TOKEN)

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

if __name__ == '__main__':
    main()
