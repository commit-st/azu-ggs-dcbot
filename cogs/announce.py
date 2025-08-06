```python
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
        관리자 권한이 있는 사용자만 사용 가능
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
        # 공개 응답
        await interaction.response.send_message(embed=embed)

    @app_commands.command(
        name="colorchat",
        description="Embed 공지 미리보기 (호출자만 보임)"
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
        관리자 권한이 있는 사용자만 사용 가능
        """
        try:
            c = int(color.lstrip("#"), 16)
        except ValueError:
            return await interaction.response.send_message(
                "❌ 유효한 색상 코드를 입력하세요. ex) #FF69B4",
                ephemeral=True
            )
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
```
