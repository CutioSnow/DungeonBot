# Dungeon;Bot
Dungeon;Bot provides a powerful toolset to assist in remote play for RPG's such as Dungeons and Dragons, Monster of the Week, and many more! This handy server bot comes with resources such as a d2 to d100 dice roller, initiative order calculator, damage calculator, and much more.

# Requirements
Must have a uniquie discord bot token. In this version, the token was mapped within the main method of the DungeonBot.py file using a secret .json file called token.json.

This bot was built using Python 3.10.6 within a virtual environment. Activate venv in,
Ubuntu:
 - ```source env/bin/activate```
 - ```python3 DungeonBot.py```
 - To terminate: ```deactivate```
For other operating systems you must reconstruct the venv or run on your full install of python

# Package Requirements
 - discord.py
 - NumPy
 
# Discord Client Commands
Dungeon;Bot utilizes the discord.ext.commands package to generate a set of commands that interact with the discord client based on various user inputs. The current command list is as follows:
 - !roll: Accepts user argument in the form NdN, where N1 represents the number of dice the user wishes to roll and N2 represents the type of die being rolled (d2-d100). One to six die values are generated and displayed in the client with a calculated total.

# RandomNumberGenerator Class
Provides organized and simplified utilities for generating random numbers using both the python built-in random class and the default NumPy random number generator. All sets of random numbers are returned and operated on within NumPy Arrays. NumPy Arrays have been shown to have various advantages over lists, including lower memory demands and faster computation speeds. 
