# cogs/readymadeannounce.py
import discord
from discord.ext import commands

class ReadyMadeAnnounce(commands.Cog):
    """
    !rma — 미리 정의된 여러 공지를 첫 번째 예시처럼 출력합니다.
    """
    def __init__(self, bot):
        self.bot = bot
        # 섹션 정의: 이모지, 제목, 내용
        self.sections = [
            {
                "emoji": "1️⃣",
                "title": "Respect Everyone",
                "content": (
                    "Be kind to fellow members. **Harassment**, **hate speech**, slurs, "
                    "or bullying of any kind **won’t be tolerated.**\n"
                    "Obvious trolling, baiting, low-effort drama, …"
                )
            },
            {
                "emoji": "2️⃣",
                "title": "DM Etiquette & Privacy",
                "content": (
                    "• This applies to DMs too. **Do NOT** send weird, …\n"
                    "• DMs stay in DMs. **Contact staff** if needed."
                )
            },
            {
                "emoji": "3️⃣",
                "title": "Keep It PG-13 (and TOS-Compliant)",
                "content": (
                    "No NSFW or extremely sexually suggestive content.\n"
                    "No excessive gore, violence, …\n"
                    "Use respectful language."
                )
            },
            # 필요하신 섹션을 추가…
        ]

    @commands.command(name="rma")
    @commands.has_permissions(administrator=True)
    async def rma(self, ctx: commands.Context):
        # 1) Embed 생성 (사이드 컬러 바만 설정)
        embed = discord.Embed(color=discord.Color.gold())

        # 2) 헤더 필드: 가장 크게 보이는 영역
        embed.add_field(
            name="📜 RULES /",
            value="\u200b",    # zero-width space: 제목만 띄우기
            inline=False
        )

        # 3) 헤더 아래 얇은 분리선
        thin_sep = "\u2500" * 40  # U+2500 ('─') 40개
        embed.add_field(
            name="\u200b",
            value=thin_sep,
            inline=False
        )

        # 4) 각 섹션을 순서대로 추가
        for sec in self.sections:
            embed.add_field(
                name=f"{sec['emoji']} **{sec['title']}**",
                value=sec["content"],
                inline=False
            )

        # 5) 푸터 안내
        embed.set_footer(text="위 규칙을 준수해 주세요. 문의는 @Staff 채널로.")

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(ReadyMadeAnnounce(bot))
