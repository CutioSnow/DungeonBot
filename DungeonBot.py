import discord, logging, json

from discord.ext import commands

#Initialize logging information
logging.basicConfig(level=logging.INFO)

#Sets intents for discord server
intents = discord.Intents(messages=True, message_content=True, guilds=True)

#Initialize discord bot via discord ext commands interface
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    """
    Displays connection information in the terminal when the client finishes
    preparing the data recieved from the Discord Server
    """
    #Display login information
    print(f"Logged in as\n{bot.user.name}\n{bot.user.id}\n{'-':-^10}")

@bot.command()
async def roll(ctx):
    print('test')

def main():
    #Activate bot via Private TOKEN. Method varies based on needs
    #For this version, the TOKEN constent is stored in a private JSON file
    file = open("./.token/token.json",'r')
    data = json.load(file)
    file.close()

    #Connect Bot using above config
    try:
        bot.run(data['TOKEN'])
    except:
        print("ERROR: Invalid token entry")

if __name__ == "__main__":
    main()