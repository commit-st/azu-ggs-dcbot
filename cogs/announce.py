import discord
from discord import app_commands
from discord.ext import commands

class Announce(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="announce",
        description="Embed 공지 전송 (호출자에게만 보임)"
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
        """
        사용법 예시:
        /announce color:#FFD700 title:"📢 서버 공지" content:"점검이 오후 2시에 시작됩니다."
        """
        # 색상 파싱
        try:
            c = int(color.lstrip("#"), 16)
        except ValueError:
            return await interaction.response.send_message(
                "❌ 유효한 색상 코드를 입력하세요. ex) #FF69B4",
                ephemeral=True
            )
        # 구분선 생성
        separator = "─" * 30
        # Embed 구성
        embed = discord.Embed(
            title=title,
            description=f"{separator}\n{content}",
            color=discord.Color(c)
        )
        # Ephemeral 응답 (호출자만 보임)
        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )

async def setup(bot):
    await bot.add_cog(Announce(bot))
