import discord

class DiscordOppHelper:
    """
    The DiscordOppHelper class provides a set of static tools to perform common
    discord.py opperations for discord bot managment
    """
    def __init__(self) -> None:
        pass

    def embedGen(title:str, msg:str, color:int=0) -> discord.Embed:
        """
        The embedGen method is a static method used to generate a discord embed
        object with set title, message, and boarder color(discord default color if
        none is set).

        Parameters:
            title (str): title of embeded message
            msg (str): contents of embeded message
            color (int): integer value representing embed boarder colour. Discord
                         default if none is set
        
        Returns:
            embed (discord.Embed): Formated discord Embed object
        """
        #Creates and returns discord embed object
        embed:discord.Embed = discord.Embed(title=title,description=msg,colour=color)
        return embed

    def embedGenUserDisplay(auth:discord.Member, title:str, msg:str, color:int=0) -> discord.Embed:
        """
        The embedGenUserDisplay method is a sister used to generate a
        discord embed object with a set username and image. Requires a discord 
        Member object to find author image url and display name.

        Parameters:
            auth (discord.member): Author of discord client message
            title (str): title of embeded message
            msg (str): contents of embeded message
            color (int): integer value representing embed boarder colour. Discord
                         default if none is set
        
        Returns:
            embed (discord.Embed): Formated discord Embed object
        
        """
        #initialize the embed variable
        embed:discord.Embed = discord.Embed(title=title,description=msg,colour=color)

        #Sets the embed author as the passed Guild Member
        embed.set_author(name=auth.display_name,icon_url=auth.avatar.url)

        #Return formated embed
        return embed


