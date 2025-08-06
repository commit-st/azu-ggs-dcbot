# cogs/readymadeannounce.py
import discord
from discord.ext import commands

class ReadyMadeAnnounce(commands.Cog):
    """
    !rma — 미리 정의된 여러 공지(섹션)를 한 번에 출력합니다.
    """
    def __init__(self, bot):
        self.bot = bot

        # 2️⃣, 3️⃣ … 섹션 정의
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
            # …필요한 만큼 계속 추가
        ]

    @commands.command(name="rma")
    @commands.has_permissions(administrator=True)
    async def rma(self, ctx: commands.Context):
        # 1) Embed 기본 생성
        embed = discord.Embed(color=discord.Color.gold())

        # 2) 최상단 헤더: author를 사용해 크게 표시
        embed.set_author(
            name="📜 RULES /",   # 헤더 이모지 + 텍스트
        )

        # 3) 각 섹션을 add_field로 추가
        for sec in self.sections:
            # 필드 이름에 이모지+굵은 제목
            field_name = f"{sec['emoji']} **{sec['title']}**"
            embed.add_field(
                name=field_name,
                value=sec["content"],
                inline=False
            )

        # 4) 작은 분리선(본문 field로 추가하면 복사 가능)
        separator = "\u2500" * 40
        embed.add_field(
            name="\u200b",    # zero-width space
            value=separator,
            inline=False
        )

        # 5) 마지막 푸터
        embed.set_footer(text="위 규칙을 준수해 주세요. 문의는 @Staff 채널로.")

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(ReadyMadeAnnounce(bot))
