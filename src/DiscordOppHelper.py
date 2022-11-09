import discord

class DiscordOppHelper:
    """
    The DiscordOppHelper class provides a set of static tools to perform common
    discord.py opperations for discord bot managment
    """
    def __init__(self) -> None:
        pass

    def embedGenUserDisplay(auth:discord.Member, title:str, msg:str, color:int) -> discord.Embed:
        """
        The embedGenUserDisplay method is a static method used to generate a
        discord embed object with a set username and image. Requires a discord 
        Member object to find author image url and display name.

        Parameters:
            auth (discord.member): Author of discord client message
            title (str): title of embeded message
            msg (str): contents of embeded message
            color (int): integer value representing embed boarder colour
        
        Returns:
            embed (discord.Embed): Formated discord Embed object
        
        """
        #initialize the embed variable
        embed:discord.Embed = discord.Embed(title=title,description=msg,colour=color)

        #Sets the embed author as the passed Guild Member
        embed.set_author(name=auth.display_name,icon_url=auth.avatar.url)

        #Return formated embed
        return embed


