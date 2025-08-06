import discord
from discord.ext import commands

class ReadyMadeAnnounce(commands.Cog):
    """
    !rma — '📜 RULES /' 헤더를 크게, 선택 가능한 텍스트로
    각 섹션을 예시 1번 스타일처럼 출력합니다.
    """
    def __init__(self, bot):
        self.bot = bot
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
            # 추가 항목...
        ]

    @commands.command(name="rma")
    @commands.has_permissions(administrator=True)
    async def rma(self, ctx: commands.Context):
        # 1) Embed 생성 (컬러 바만 설정)
        embed = discord.Embed(color=discord.Color.gold())

        # 2) 헤더: set_author 로 가장 크게, 텍스트 선택 가능
        embed.set_author(
            name="📜 RULES /"
            # icon_url=None  # 필요 없으면 생략
        )

        # 3) 얇은 분리선 (옵션)
        thin_sep = "\u2500" * 40
        embed.add_field(name="\u200b", value=thin_sep, inline=False)

        # 4) 섹션들
        for sec in self.sections:
            embed.add_field(
                name=f"{sec['emoji']} **{sec['title']}**",
                value=sec["content"],
                inline=False
            )

        # 5) 푸터
        embed.set_footer(text="위 규칙을 준수해 주세요. 문의는 @Staff 채널로.")

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(ReadyMadeAnnounce(bot))
