# cogs/readymadeannounce.py
import discord
from discord.ext import commands

class ReadyMadeAnnounce(commands.Cog):
    """
    !rma — 미리 정의된 공지들을 한 번에 Embed로 출력합니다.
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
            # 필요에 따라 추가…
        ]

    @commands.command(name="rma")
    @commands.has_permissions(administrator=True)
    async def rma(self, ctx: commands.Context):
        # 1) 임베드 생성: title이 가장 크게 표시됩니다.
        embed = discord.Embed(
            title="📜 RULES /",
            color=discord.Color.gold()
        )

        # 2) 각 섹션을 field 로 추가 (제목+내용)
        for sec in self.sections:
            embed.add_field(
                name=f"{sec['emoji']} {sec['title']}",
                value=sec["content"],
                inline=False
            )

        # 3) 푸터 (선택)
        embed.set_footer(text="위 규칙을 준수해 주세요. 문의는 @Staff 채널로.")

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(ReadyMadeAnnounce(bot))
