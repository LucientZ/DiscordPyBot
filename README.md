# DiscordPyBot
This is a small discord bot that has basic functionality. Most of the features are for fun with the main purpose being to entertain. Documentation can be found here: https://lucientz.github.io/DiscordPyBot/

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
When in the environment you want to run the bot in, simply run the command `make run` in the console. This will prompt you to enter config variables for the bot including its token, status, and whether it should sync its slash commands on start.

To remove __pycache__, run the command `make clean`

### <ins>How to setup manually</ins>
Everything here is assuming that you already have a discord application set up with a bot token. Make sure the bot has all intents enabled.

To install the dependencies, install the dependencies by entering the following:
```
$ pip install -r requirements.txt
```

Once the dependencies are installed run `init.py` followed by `main.py`. This can be done with the consecutive commands:
```
$ python3 ./src/init.py
$ python3 ./src/main.py
```
When `init.py` is run, you should see this output:
```
Please enter the bot token: 
Please enter the bot's status: 
Should the bot sync on start? (Y/n): 
```
Input the prompted information. If this is your first time running the bot, type 'y' since none of the commands should be synced yet.  

When main is run and if the token is valid, the bot will log in and you should get an output like this:
```
2023-03-26 03:16:21.975304 [INFO]  I'm initializing myself as a bot...
2023-03-26 03:16:24.182726 [INFO]  I exist as user 'Evolved but Untamed#1424' and can talk to people! :D
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
