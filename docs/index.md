# Bot Documentation

### Table of Contents
1. [Introduction](#introduction)
2. [Commands](#commands)
    - [Fun Commands](#fun-commands)
        - copypasta
        - fumo
        - echo
    - [Utility Commands](#utility-commands)
        - server-enable
        - server-disable
        - channel-enable
        - channel-disable
        - help
        - ping
3. [Auto Features](#auto-features)
    - sus
    - morbius
    - sad
    - trade
    - mom
4. [Server Config](#server-config)
    - Front-End
    - Back-End


<a id='introduction'></a>

## Introduction

This is a discord bot developed by [LucienZ](https://github.com/LucientZ) (LucientZ on GitHub). The main function of this bot was originally for the lead developer to learn how to use GitHub and develop software properly. Originally a moderation bot built in JavaScript, DiscordPyBot (aka 'Dumb Stupid Idiot Bad Bot') is used for entertainment purposes. The source code of this bot can be found [here](https://github.com/LucientZ/DiscordPyBot).

<a id='commands'></a>

## Commands

This bot has a variety of commands with different functions. These are invoked by prepending a `/` at the beginning of a message and picking a command from the list given by discord itself.

<a id='fun-commands'></a>

### *Fun Commands*

**Fun Commands** are commands that don't serve a specific purpose to the bot's functionality. These are provide 

#### copypasta

Returns a copypasta from a list of copypastas added by the bot host. 

Ex:
```
Input: 
    /copypasta
Output: 
    My name is Yoshikage Kira. I’m 33 years old. 
    My house is in the northeast section of Morioh, where all the villas are, and I am not married. 
    I work as an employee for the Kame Yu department stores, and I get home every day by 8 PM at the latest. 
    I don’t smoke, but I occasionally drink. I’m in bed by 11 PM, and make sure I get eight hours of sleep, no matter what. 
    After having a glass of warm milk and doing about twenty minutes of stretches before going to bed, I usually have no problems sleeping until morning. 
    Just like a baby, I wake up without any fatigue or stress in the morning.
```

#### fumo

Returns an image of a fumo (plush dolls of characters from the series "Touhou"). The images are stored as a list of urls set by the bot host. If the bot host hasn't set any images, there will only be one with the name "example".

Ex:
```
Input: 
    /fumo name:cirno
Output:
```
![Example Cirno Fumo Image](https://github.com/LucientZ/DiscordPyBot/blob/main/docs/assets/img/Cirno_Example.jpg)

#### echo

Echos specified text from a user. This works similarly to echo in a command prompt.

Ex:

```
Input: 
    /echo message:Hello World
Output: 
    Echo: Hello World
```

<a id='utility-commands'></a>

### *Utility Commands*

**Utility Commands** are commands that affect functionality of the bot or contain useful information to server admins/owners or developers.

#### server-enable

Enables an [auto feature](#auto-features) throughout the entire server.

#### server-disable

Disables an [auto features](#auto-features) throughout the entire server. This will only work on features that have previously been enabled throughout the server and does not keep a feature from being enabled. 

#### channel-enable

Enables an [auto feature](#auto-features) in the specific channel this command is used in.

#### channel-disable

Disables an [auto feature](#auto-features) in the specific channel this command is used in. This will only work on features that have previously been enabled throughout the server and does not keep a feature from being enabled.

#### ping

A classic among discord bots. Returns `Pong!` upon recieving the command and client latency

Ex:

```
Input: 
    /ping
Output:
    Pong!
    Client Latency 62 ms
```

#### help

This command is currently being reworked. Currently, returns a message linking to this page.

Ex:

```
Input:
    /help
Output:
    This command is currently being reworked. Stay tuned for a better help menu!

    Documentation: https://lucientz.github.io/DiscordPyBot
```

<a id='auto-features'></a>

## Auto Features

**Auto Features** are things the bot does passively. Many of these features simply parse user messages and act accordingly.

List of feature arguments for enable/disable:
- **all** - Every automatic feature in this list.
- **a** - Synonym for all.
- **sus** - When a message contains the string 'sus', responds with the original message with 'sus' bolded and italicized.
- **morbius** - When a message contains the string 'morb', responds with a morbius quote.
- **sad** - When a message contains the string 'sad', responds with a sad image of Spongebob.
- **trade** - When a message contains the string 'trade', responds with 'Yeah, I trade :smile:'
- **mom** - When a message ends with the word 'do', 'doing', 'done', etc... responds with the message 'Your Mom' with a 20% chance of saying 'Your Dad :sunglasses:'

<a id='server-config'></a>

## Server Config

### *Front-End*

When the bot joins a new server, by default every [command](#commands) will be enabled, but every [auto feature](#auto-features) will be disabled. Commands can be enabled/disabled through the bot's server settings on discord. Features can be enabled/disabled via the use of various [utility commands](#utility-commands).

### *Back-End*

When a message is sent in a server, the bot will attempt to create a GuildProfile object. This object will save the server config into a JSON file called `{server-id}.json` where server-id is the id given by discord to the guild the message was sent in. This JSON will be accessed anytime further action is taken for server config or messages are sent in the server.

JSON Functions:
- Contains what [auto features](#auto-features) are enabled/disabled.
- Other features not currently implemented.
