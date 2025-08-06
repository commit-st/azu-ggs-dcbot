# cogs/announce.py
import discord
from discord import app_commands
from discord.ext import commands

class Announce(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="announce",
        description="Embed 공지 전송 (공개 채널에 전송)"
        default_member_permissions=discord.Permissions(administrator=True)
    )
    @app_commands.describe(
        color="HEX 색상 코드 (#RRGGBB)",
        title="제목(큰 글씨)",
        content="본문"
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def announce(
        self,
        interaction: discord.Interaction,
        color: str,
        title: str,
        content: str
    ):
        # 색상 파싱
        try:
            c = int(color.lstrip("#"), 16)
        except ValueError:
            await interaction.response.send_message(
                "❌ 유효한 색상 코드를 입력하세요. ex) #FF69B4",
                ephemeral=True
            )
            return
        # 구분선 생성
        separator = "─" * 30
        # Embed 구성: 제목 + 구분선 + 본문
        embed = discord.Embed(
            title=title,
            description=f"{separator}\n{content}",
            color=discord.Color(c)
        )
        # 공개 응답
        await interaction.response.send_message(embed=embed)

    @app_commands.command(
        name="colorchat",
        description="Embed 메시지 전송 (공개 채널에 전송, 제목 없이)"
    )
    @app_commands.describe(
        color="HEX 색상 코드 (#RRGGBB)",
        content="본문"
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def colorchat(
        self,
        interaction: discord.Interaction,
        color: str,
        content: str
    ):
        # 색상 파싱
        try:
            c = int(color.lstrip("#"), 16)
        except ValueError:
            await interaction.response.send_message(
                "❌ 유효한 색상 코드를 입력하세요. ex) #FF69B4",
                ephemeral=True
            )
            return
        # Embed 구성: 본문만
        embed = discord.Embed(
            description=content,
            color=discord.Color(c)
        )
        # 공개 응답
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Announce(bot))
