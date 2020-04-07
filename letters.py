import discord
from discord.ext import commands

class LettersCmds(commands.Cog):

    @commands.command()  # use commands.command in a cog
    async def whois(self, ctx: commands.Context, who: discord.Member = None):
        """ Returns someone's nickname, or if none, their tag. """
        if who:
            name = who.display_name
        else:
            name = ctx.author.display_name
        await ctx.send(f"Why it's {name}, of course") 


    @commands.command()
    async def role(self, ctx, role: discord.Role):
        """ Returns info about a role. """
        embed = discord.Embed(
            title=role.name,
            color=role.color
        )
        embed.add_field(name='Hex color code', value=f"**{role.color}**")  # inline is true by default
        embed.add_field(name="Permission bitfield", value=role.permissions.value)
        await ctx.send(embed=embed)
    

def setup(bot):
    bot.add_cog(LettersCmds(bot))