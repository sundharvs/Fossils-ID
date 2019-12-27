import discord
from discord.ext import commands
from data import db
from string import punctuation

class Check(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def check(self, ctx):
        userid = ctx.message.author.id
        response = ctx.message.content[8:]
        ans = db.readplaintext(userid)
        
        if(ans == "" or ans is None):
            await ctx.send("You must ask for a fossil first!")
        
        elif(response == ""):
            pass
        
        elif(ans.lower() == response.lower().replace("-", " ")):
            await ctx.send(f'**{str(ctx.author.mention)}**, you are correct!')
            db.changescore(userid,1)
        
        elif(ans.lower() != response.lower().replace("-", " ")):
            await ctx.send('Sorry, that wasn\'t the right answer.')

def setup(bot):
    bot.add_cog(Check(bot))
