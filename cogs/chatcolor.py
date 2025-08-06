import discord
from discord.ext import commands

class MultiAnnounce(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="multi_announce")
    @commands.has_permissions(administrator=True)
    async def multi_announce(self, ctx, *, body: str):
        embeds = []
        current_color = None
        current_lines = []

        for line in body.splitlines():
            line = line.strip()
            if not line:
                continue

            # 새 색상코드가 등장했을 때
            if line.startswith("#") and " " in line:
                # 기존에 모아둔 블록이 있으면 Embed로 변환
                if current_color and current_lines:
                    # description에 join된 여러 줄을 넣기
                    embed = discord.Embed(
                        description="\n".join(current_lines),
                        color=discord.Color(int(current_color.lstrip("#"), 16))
                    )
                    embeds.append(embed)
                # 새 블록 초기화
                parts = line.split(" ", 1)
                current_color = parts[0]
                current_lines = [parts[1]]

            # 색상코드가 아니라면, 같은 블록에 이어붙이기
            else:
                if current_lines is not None:
                    current_lines.append(line)

        # 마지막 블록 처리
        if current_color and current_lines:
            embed = discord.Embed(
                description="\n".join(current_lines),
                color=discord.Color(int(current_color.lstrip("#"), 16))
            )
            embeds.append(embed)

        if not embeds:
            return await ctx.send("❌ 형식 오류: `#색상코드 내용` 형식을 지켜주세요.")

        # 한 번에 여러 Embed 전송
        await ctx.send(embeds=embeds)

async def setup(bot):
    await bot.add_cog(MultiAnnounce(bot))
