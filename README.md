# A Simple Discord.py Bot Template

The barebones of what can become a massive discord bot, this template will guide you to success (hopefully). Follow the steps below to make sure you don't break anything :)

## Requirements

Before starting, you must have:
- Microsoft Visual Studio Code
- Python 3.6+
- Discord Developer Application

If you do not know how to get any, watch the Youtube video on my channel.

## Installing Packages

To begin, download the source code, unzip it, then open a command terminal in that directory. Then, run 
```py
pip install -r requirements.txt
```
or
```
pip install discord.py
```
if you aren't lazy. This will install the one and only required package, Discord.py.

## Editing The Code

Make sure to open up `bot.py` and edit the `prefix` and `token` variables to match your preference and the token you retieved from https://discord.com/developers/applications.
Nothing else needs to be changed, and if you edit anything make sure not to mess with the `bot` variable setup and/or the `bot.run` function.

## Running The Bot

In Visual Studio Code, open the `bot.py` file and in the top right, click the > button to Run the file, then read the Terminal to see `Logged in as <user>`, then open Discord and use your bot.
