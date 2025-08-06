# cogs/image.py
import discord
from discord.ext import commands

class ImageSender(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="image")
    @commands.has_permissions(administrator=True)
    async def image_prefix(self, ctx: commands.Context, url: str):
        """!image URL — 이미지를 Embed로 전송합니다."""
        embed = discord.Embed()
        embed.set_image(url=url)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(ImageSender(bot))
