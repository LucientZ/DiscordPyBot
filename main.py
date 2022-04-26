import discord
from discord.ext import commands
import datahandling as dt
from textfunctions import *

client = commands.Bot(command_prefix = 's-')

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

    if 'run' in message.content.lower() or 'fitness' in message.content.lower():
        await message.channel.send("The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly but gets faster each minute after you hear this signal bodeboop. A sing lap should be completed every time you hear this sound. ding Remember to run in a straight line and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark. Get ready!… Start.")

    if 'morbius' in message.content.lower():
        await message.channel.send(morbius())
    
    if message.content == 's-copypasta':
        await message.channel.send(copypasta())



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
