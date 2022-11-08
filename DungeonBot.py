import discord, logging
from discord.ext import commands

def main():
    #Initialize logging information
    logging.basicConfig(level=logging.INFO)

    #Sets intents for discord server
    intents = discord.Intents(messages=True, message_content=True, guilds=True)

    #Used to run bot with a declared set of asyncronous commands
    bot = commands.Bot(command_prefix='!', intents=intents)

if __name__ == "__main__":
    main()