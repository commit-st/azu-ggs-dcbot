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
        content="본문",
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def announce(…):
        …

    @app_commands.command(
        name="colorchat",
        description="Embed 메시지 전송 (공개 채널에 전송, 제목 없이)"
    )
    @app_commands.describe(
        color="HEX 색상 코드 (#RRGGBB)",
        content="본문",
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def colorchat(…):
        …
