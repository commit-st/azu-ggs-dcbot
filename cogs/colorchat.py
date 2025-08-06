import discord
from discord import app_commands
from discord.ext import commands

class Announce(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="colorchat",
        description="색상 바 포함 임베드 전송 (호출자만 보임)"
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
        """
        사용법 예시:
        /colorchat color:#FFD700 content:"점검이 오후 2시에 시작됩니다."
        """
        # 색상 파싱
        try:
            c = int(color.lstrip("#"), 16)
        except ValueError:
            await interaction.response.send_message(
                "❌ 유효한 색상 코드를 입력하세요. ex) #FF69B4",
                ephemeral=True
            )
            return

        # Embed 구성: 컬러 바 + 본문
        embed = discord.Embed(
            description=content,
            color=discord.Color(c)
        )

        # Ephemeral 응답 (호출자만 보임)
        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )

async def setup(bot):
    await bot.add_cog(Announce(bot))
