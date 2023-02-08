# DEPRECATED
This version of the bot is **deprecated** meaning it does not reflect current versions anymore. The bot will still work with discord.py 2.0 and above, but it is a lot harder to use and messy in organization. Please go to https://github.com/LucientZ/DiscordPyBot in order to see the latest version of my bot. Thank you.

If you must use this version since it's the only version that has the bad apple playing on the status, here are the instructions for how to use the bot:

# Instructions

Everything here is run in Python 3.8.10 and above which can be found here:
- https://www.python.org/downloads/

### <ins>Dependencies</ins>
- discord.py

### <ins>How to setup</ins>
Everything here is assuming that you already have a discord application set up with a bot token. Make sure the bot has all intents enabled.

Before starting the bot, install python on your machine. The bot is written in python 3.8.10, but it will work with most versions of python that are supported by discord.py. Once python is installed, check to ensure you're running the desire version by entering the following command into your terminal without the dollar sign:
```
$ python3 --version
```
The output should be something like the following:
```
Python 3.8.10
```
To install the dependencies, install discord.py by entering the following:
```
$ pip install discord.py
```
Having a python environment tool like virtualenv or pipenv is recommended to keep things from conflicting from other possible python projects you may have.

Once everything is setup, run main.py in the root directory with python. This can easily be done in the console using:
```
$ python3 ./main.py
```
When the program is run, you should see this output:
```
Would you like to sync the bot globally? (Only do this if the bot has been updated or a command has changed) [Y/n]
```
If this is your first time running the bot, type 'y' since none of the commands should be synced yet. 

Afterwards, you'll be prompted with whether or not a file named '.token' should be created in the directory. '.token' is used by the program so that the bot token does not need to be entered every single time. If you happen to only want to use the token once, type 'n'. Otherwise, type 'y'. 

Once you make this decision, you'll be prompted to enter your token. If the token is valid, the bot will log in and you should get an output like this:
```
2022-11-23 22:41:10 INFO     discord.client logging in using static token
2022-11-23 22:41:10 INFO     discord.gateway Shard ID None has connected to Gateway (Session ID: ID).   
2022-11-23 22:41:10 STATUS   I'm initializing myself as a bot :)
2022-11-23 22:41:12 INFO     Awaiting command tree syncing...
2022-11-23 22:41:13 INFO     Tree Synced. Elapsed time: 0.18 seconds
2022-11-23 22:41:13 STATUS   I exist as user 'BOT_ID' and can talk to people! :D
```
Once you get the message where the bot says "I exist...", then you're all good to go.

### <ins>How to customize</ins>
Certain commands like /fumo and /copypasta don't have much functionality by default. This is because the outputs are stored locally in the directory './textdata/'. In order to add functionality, run ./setup.py in the terminal.
```
$ python3 ./setup.py
```
Once ran, you should see an output like this:
```
Welcome to this bot's setup application.

------------------------------------------------------------
Here are the available setup options:

1: Copypasta List Modification
2: Fumo Image URL List Modification
3: WIP

Please enter an option (q to quit):
```
Type the number corresponding to what you want to modify. Note that this tool is relatively limited at the moment and more is expected to be added later.
