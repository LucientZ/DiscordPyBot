# DiscordPyBot
This is a small discord bot that has basic functionality.

Everything here is run in Python 3.8.10 and above which can be found here:
- https://www.python.org/downloads/

This bot uses the discord.py api in which the documentation can be found here:
- https://discordpy.readthedocs.io/en/stable/api.html
- To install: pip install discord.py


Notes:

    -The bot will prompt the user for a token. This token is used for login and verification purposes on the discord client.
    The token is stored in a .token file. Temporary login is an option that is prompted, but this isn't recommended since discord tokens are only able to be viewed once on the devportal.

    -setup.py is a work in progress console that can add or remove copypastas from a list for the /copypasta command. This will have more functionality in the future, but for now it is a very rudimentary program.

    -In order for the bot to work, the client the bot is logging into must have all intents enabled or intents must be changed in main.py to reflect the permissions of the bot.


