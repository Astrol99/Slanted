import discord
from discord.ext import commands
try:
    import pyfiglet as fig
    import_status = True
except ImportError:
    import_status = False
    import os

class sLanted:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pkg(self, ctx):
        if import_status == True:
            return await ctx.send("Pyfiglet is already installed!")
        await ctx.send("Installing pyfiglet...")
        os.system("pip3 install pyfiglet")
        await ctx.send("Finished installing pyfiglet!")
    
    @commands.command()
    async def slant(self, ctx, *, arg:str=None):
        if import_status == False:
            await ctx.send("Pyfiglet isn't installed!")
            return await ctx.send("Please enter the command: ./pkg to install pyfiglet, otherwise, this command is not usable")
        if arg == None or arg == " ":
            return await ctx.send("Invalid text!")
        text = fig.figlet_format(arg, font='slant')
        await ctx.send(f"```\n{text}\n```")
        

def setup(bot):
    bot.add_cog(sLanted(bot))