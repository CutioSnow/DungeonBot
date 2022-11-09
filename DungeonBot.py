import discord, logging, json
from numpy.random import default_rng
from discord.ext import commands

#Initialize logging information
logging.basicConfig(level=logging.INFO)

#Sets intents for discord server
#IMPORTANT: Requires guild_members and message_contents permissions to be
# enabled on the discord developer portal
intents = discord.Intents(messages=True, message_content=True, guilds=True, members=True)

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
async def roll(ctx, arg:str):
    """Let's you roll any die (d2-d20) up to 4 times in the format NdN"""
    #Tuple containing accepted dice values
    dice:tuple = ('2','4','6','8','10','12','20','100')

    #Initializes roll data values
    total:int = 0
    msg:str = ""

    try:
        #Formats the argument passed by client
        data = arg.split('d')

        #Ensures arg represents an accepted die type otherwise throws an Exception
        if data[1] in dice:
            #Initializes dice roll count and die type as integer values
            numberOfDice = int(data[0])
            dieType = int(data[1])
            #Checks that no more than 6 die are being rolled
            #If greater than 6 die will inform the user only 6 will be rolled
            if numberOfDice > 0:
                if numberOfDice > 6:
                    numberOfDice = 6
                    msg += "Only 6 dice may be rolled!"

                #Displays the number and type of dice
                msg += f"Rolling {numberOfDice}d{dieType}:"

                #Initialize NumPy Random Number Generator
                ran = default_rng()
                #Generates a set of random numbers for the dice rolls
                rolls:list = ran.integers(low=1,high=dieType+1,size=numberOfDice)
                print(rolls)
                #Formats roll message
                for i in rolls:
                    msg += f"\nRoll: {i}"
                #Formats sum display
                msg += f"\n{'-':-^10}\nTotal: {sum(rolls)}"

                #Creates Embed msg to display on client
                title = f"Rolling {numberOfDice}d{dieType}:"
                embedVar = discord.Embed(title=title,description=msg,colour=discord.Colour.green())
                print(1)
                #Collects author name and profile image for display
                auth = ctx.author.display_name
                img = ctx.message.author.avatar_url
                print(3)
                embedVar.set_author(name=auth, icon_url=img)
                print(4)
                await ctx.send(embed=embedVar)
            else:
                raise Exception
        else:
            raise Exception
    except:
        await ctx.send("Must roll in form NdN and be an existing dice! (Only up to 6 die)")


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