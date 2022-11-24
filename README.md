# DiscordPyBot
This is a small discord bot that has basic functionality. Most of the features are for fun with the main purpose being to entertain.

Everything here is run in Python 3.8.10 and above which can be found here:
- https://www.python.org/downloads/

### <u>Dependencies</u>
- discord.py


### <u>How to setup</u>
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
$ pip install 
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

Afterwards, you'll be prompted with whether or not a file named '.token' should be created in the directory. '.token' is used by the program so that the bot token does not need to be entered every single time. If you happen to only want to use the token once, type 'n'. Otherwise, type 'y'. Once you make this decision, you'll be prompted to enter your token. If the token is valid, the bot will log in and you should get an output like this:
```
2022-11-23 22:41:10 INFO     discord.client logging in using static token
2022-11-23 22:41:10 INFO     discord.gateway Shard ID None has connected to Gateway (Session ID: ID).   
2022-11-23 22:41:10 STATUS   I'm initializing myself as a bot :)
2022-11-23 22:41:12 INFO     Awaiting command tree syncing...
2022-11-23 22:41:13 INFO     Tree Synced. Elapsed time: 0.18 seconds
2022-11-23 22:41:13 STATUS   I exist as user 'BOT_ID' and can talk to people! :D
```
Once you get the message where the bot says "I exist...", then you're all good to go.

### <u>How to customize</u>