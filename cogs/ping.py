# cogs/ping.py
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="핑")
    async def ping(self, ctx):
        """!핑 → 모두에게 퐁!"""
        await ctx.send("퐁! 🏓")

async def setup(bot):
    await bot.add_cog(Ping(bot))
