import discord, logging, json
from src.DiscordOppHelper import DiscordOppHelper as opp
from src.RandomNumberGenerator import RandomNumberGenerator as rng
from numpy import ndarray
from discord.ext import commands

#Initialize logging information
logging.basicConfig(level=logging.INFO)

#Sets intents for discord server
#IMPORTANT: Requires presence, guild_members, and message_contents permissions
# to be enabled on the discord developer portal
intents = discord.Intents.all()

#Initialize discord bot via discord ext commands interface
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    """
    Displays connection information in the terminal when the client finishes
    preparing the data received from the Discord Server
    """
    #Display login information
    print(f"Logged in as\n{bot.user.name}\n{bot.user.id}\n{'-':-^10}")

@bot.command()
async def roll(ctx, arg:str):
    """
    Accepts user argument in the form NdN, where N1 represents the number of 
    dice the user wishes to roll and N2 represents the type of die being rolled
    (d2-d100). One to six die values are generated and displayed in the client 
    with a calculated total.
    """
    #Tuple containing accepted dice values
    dice:tuple = ('2','4','6','8','10','12','20','100')

    #Initializes display message
    msg:str = ""

    #stores author data for use in DiscordOppHelper embed generator
    author = ctx.author

    try:
        #Formats the argument passed by client to separate roll and die data
        data = arg.upper().split('D')

        #Ensures arg represents an accepted die type otherwise throws an Exception
        if data[1] in dice:
            #Initializes dice roll count and die type as integer values
            numberOfDice,dieType = int(data[0]), int(data[1])
            #Checks that no more than 6 die are being rolled
            #If greater than 6 die will inform the user only 6 will be rolled
            if numberOfDice > 0:
                if numberOfDice > 6:
                    numberOfDice = 6
                    msg += "**Only 6 die may be rolled!**"
                #Generates a set of random numbers to represent the dice rolls
                rolls:ndarray = rng.randomInt(low=1,high=dieType,size=numberOfDice)
                print(f"Generated rolls: {rolls}")
                #Formats roll message
                for i in rolls:
                    msg += f"\nRoll: {i}"
                #Formats sum display
                msg += f"\n{'-':-^10}\nTotal: {sum(rolls)}"
                #Creates and displays an embed message to discord client
                title = f"Rolling {numberOfDice}d{dieType}:"
                await ctx.message.delete() #Deletes authors command
                await ctx.send(embed=opp.embedGenUserDisplay(
                    auth=author,title=title,msg=msg,color=discord.Colour.green()
                ))
            else:
                raise Exception
        else:
            raise Exception
    except:
        await ctx.send("Must roll in form NdN and be an existing dice! (Only up to 6 die)")
    
def main():
    #Attempts to activate bot via Private TOKEN. Method varies based on needs
    #For this version, the TOKEN constant is stored in a private JSON file
    try:
        with open("./.token/token.json") as f:
            data = json.load(f)
        bot.run(data['TOKEN'])
    except:
        print("ERROR: Invalid token entry")

if __name__ == "__main__":
    main()