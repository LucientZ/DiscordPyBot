# DiscordPyBot
This is a small discord bot that has basic functionality. Most of the features are for fun with the main purpose being to entertain.

This bot is made with python 3.8.
```
$ python3 --version
```
The output should be something like the following:
```
Python 3.8.10
```

Having a python environment tool like virtualenv or pipenv is recommended to keep things from conflicting from other possible python projects you may have.

### <ins>How to setup with make</ins>

```bash
$ make run
```
To remove the 

### <ins>How to setup manually</ins>
Everything here is assuming that you already have a discord application set up with a bot token. Make sure the bot has all intents enabled.

To install the dependencies, install the dependencies by entering the following:
```
$ pip install -r requirements.txt
```

Once everything is setup, run `main.py` in the `./src` directory with python. This can easily be done in the console using:
```
$ python3 ./src/main.py
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
$ python3 ./src/config.py
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
