from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="핑")
    async def ping(self, ctx):
        await ctx.send("퐁! 🏓")

async def setup(bot):
    await bot.add_cog(Example(bot))

