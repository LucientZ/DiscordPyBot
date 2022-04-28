import discord
from discord.ext import commands
import datahandling as dt
from textfunctions import *
from helper import colors as cl

client = commands.Bot(command_prefix = 's-')

@client.event
async def on_connect():
    print('I exist!')

@client.event
async def on_ready():
    print('I can talk to friends now! :)')

@client.event
async def on_message(message):
    # Bot doesn't respond to itself
    if message.author == client.user:
        return

    # These are funny responses to if a user happens to type a certain phrase.
    if 'sus' in message.content.lower():
        await message.channel.send("Amogus detected: " + format_msg(message.content, 'sus','***'))


    # Start of command section.
    if message.content == 's-copypasta':
        await message.channel.send(copypasta())



# Login information for the bot requires a token.
# token is taken from a file named '.token'
# If this file does not exist, user will be prompted to input token

# TODO: Figure out how to recover from 'Improper token has been passed.' error
# Current handling: Ask for new TOKEN -> write TOKEN to .token -> crash program
# Error turns into RuntimeError('Even loop is closed')
def main():
    try:
        TOKEN = dt.get_token()
        client.run(TOKEN)

    except discord.LoginFailure as e:
        #This error is raised when the token is not valid
        print(f"{cl.RED}[ERROR] Issue logging into bot:{cl.BLUE}",e,f'{cl.END}\n')
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
        print(f"{cl.RED}[ERROR] Issue logging into bot:{cl.BLUE}",e,f'{cl.END}\n')
        print("Terminating program...\n")
        exit()

if __name__ == '__main__':
    main()
