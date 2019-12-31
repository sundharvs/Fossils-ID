import discord
from discord.ext import commands
from data import db
from operator import itemgetter

class Scoreboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def scoreboard(self,ctx):
        leaderboard = ''
        try:
            scores = sorted(db.readallscores(), key = itemgetter(1), reverse = True)
        except TypeError:
            await ctx.send("It doesn't look like anyone has played yet")

        users = [i[0] for i in scores]
        server = ctx.message.guild
        
        embed = discord.Embed(type="rich", colour=discord.Color.blurple())
        embed.set_author(name="Fossil ID - A Paleontology Bot")

        if(len(scores) > 0):
                for index, score in enumerate(scores[:10]):
                    try:
                        user = server.get_member(int(scores[index][0]))
                        leaderboard += f"{index + 1}. **{user.name}#{user.discriminator}**\n" #f'\n{index + 1}. {server.get_member(int(scores[index][0])).display_name}'
                    except AttributeError:
                        pass
                
                embed.add_field(name=f"Leaderboard (global)", value=leaderboard, inline=False)
                
                usr_index = users.index(str(ctx.author.id))
                if usr_index is not None:
                    placement = usr_index + 1
                    distance = (scores[usr_index][1] - 1) - scores[usr_index][1]

                    if placement is 1:
                        embed.add_field(name="You:", value=f"You are #{str(placement)} on the leaderboard.\n" + f"You are in first place.", inline=False)
                    elif distance is 0:
                        embed.add_field(name="You:", value=f"You are #{str(placement)} on the leaderboard.\n" + f"You are tied with #{str(placement-1)}", inline=False)
                    else:
                        embed.add_field(name="You:", value=f"You are #{str(placement)} on the leaderboard.\n" + f"You are {str(distance)} away from #{str(placement-1)}", inline=False)
                else:
                    embed.add_field(name="You:", value="You haven't answered any correctly.")
                
                await ctx.send(embed=embed)
        else:
            await ctx.send("It doesn't look like anyone has played yet")

def setup(bot):
    bot.add_cog(Scoreboard(bot))
