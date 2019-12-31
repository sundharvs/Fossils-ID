import discord
from discord.ext import commands
from data import db

class Race(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def race(self, ctx):
        

def setup(bot):
    bot.add_cog(Race(bot))