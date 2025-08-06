# cogs/image.py
import discord
from discord import app_commands
from discord.ext import commands

class ImageSender(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="image",
        description="이미지 링크를 임베드로 전송합니다",
        default_member_permissions=discord.Permissions(administrator=True),  # ← 추가
    )
    @app_commands.describe(
        url="전송할 이미지의 URL을 입력하세요",
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def image(self, interaction: discord.Interaction, url: str):
        """이미지를 Embed로 전송합니다"""
        embed = discord.Embed()
        embed.set_image(url=url)
        # 공개 응답
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(ImageSender(bot))
