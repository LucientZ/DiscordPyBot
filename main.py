import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '%')


@client.event
async def on_connect():
    print('I exist!')

@client.event
async def on_ready():
    print('I can talk to friends now! :)')

# Login information for the bot requires a token.
# Because this repository is public, this token is inputted by the user.
TOKEN = input('Please enter the bot token: ')

# TODO: Come up with more elegant method of user-input verification
# This will work for now
while(True):
    try:
        client.run(TOKEN)
        break
    except Exception as e:
        print("[ERROR] Issue logging into bot:",e,'\n')
        print("Exiting program...")
        exit()