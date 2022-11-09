from discord.ext import commands

@commands.command()
async def roll(ctx):
    print("test")

async def setup(bot):
    bot.add_command(roll)