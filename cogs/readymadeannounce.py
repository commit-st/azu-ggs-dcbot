# cogs/readymadeannounce.py
import discord
from discord.ext import commands

class ReadyMadeAnnounce(commands.Cog):
    """
    !rma — 미리 정의된 여러 공지(섹션)를 한 번에 출력합니다.
    """
    def __init__(self, bot):
        self.bot = bot

        # 여기에 미리 만들어 둘 공지들을 리스트로 정의하세요.
        # 각각의 dict에 "title" 과 "content" 키를 넣으면 됩니다.
        self.sections = [
            {
                "title": "1️⃣ Respect Everyone",
                "content": (
                    "Be kind to fellow members. **Harassment**, **hate speech**, "
                    "slurs, or bullying of any kind **won’t be tolerated.**\n"
                    "Obvious trolling, baiting, low-effort drama, …"
                )
            },
            {
                "title": "2️⃣ DM Etiquette & Privacy",
                "content": (
                    "• This applies to DMs too. **Do NOT** send weird, …\n"
                    "• DMs stay in DMs. …"
                )
            },
            {
                "title": "3️⃣ Keep It PG-13 (and TOS-Compliant)",
                "content": (
                    "No NSFW or extremely sexually suggestive content.\n"
                    "No excessive gore, violence, …\n"
                    "Use respectful language."
                )
            },
            # 원하는 만큼 섹션을 추가...
        ]

    @commands.command(name="rma")
    @commands.has_permissions(administrator=True)
    async def rma(self, ctx: commands.Context):
        """
        !rma — 모든 미리 정의된 공지를 한 번에 Embed 형태로 출력합니다.
        """
        # 1) 기본 Embed — 사이드 컬러 바만 설정
        embed = discord.Embed(
            title="📢 Server Rules & Notices",
            description="아래 내용은 미리 정의된 공지(공지사항)입니다.",
            color=discord.Color.blue()
        )

        # 2) 각 섹션을 field로 추가
        for section in self.sections:
            embed.add_field(
                name=section["title"],
                value=section["content"],
                inline=False
            )

        # 3) 원하는 경우 맨 밑에 공통 안내문구
        embed.set_footer(text="위 규칙을 준수해 주세요. 문의는 @Staff 채널로.")

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(ReadyMadeAnnounce(bot))
