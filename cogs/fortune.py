import random
import discord
from discord.ext import commands

class Fortune(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # 운세 멘트 리스트 (20가지)
        self.fortunes = [
            "오늘은 행복한 하루가 될 거예요!",
            "조금 느긋하게 움직여도 좋은 결과가 기다려요.",
            "새로운 인연이 찾아올 징조가 보여요.",
            "기분 전환으로 짧은 산책을 추천해요.",
            "물건을 잃어버리지 않게 주의하세요!",
            "뜻하지 않은 행운이 다가오고 있어요.",
            "책을 읽어보는 걸 추천해요! 도움이 될지도!",
            "서두르지 말고 차분히 계획하세요.",
            "친구와의 대화에서 중요한 단서를 얻을 수 있어요.",
            "건강 관리를 소홀히 하지 마세요.",
            "주변 사람들에게 친절을 베풀어 볼까요?",
            "새로운 일이나 취미를 시작하기 좋은 시기예요.",
            "금전운이 상승세를 타고 있어요.",
            "오늘의 선택이 내일의 기쁨이 될 거예요.",
            "감정을 솔직히 표현해보세요.",
            "문제가 생기면 도움을 청하는 게 답일 수 있어요.",
            "목표를 달성할 방법이 보입니다.",
            "작은 도전이 큰 변화를 가져올 거예요.",
            "오늘 밤은 충분한 휴식으로 마무리하세요.",
            "좋은 꿈을 꿀 거 같아요!"
        ]

    @commands.command(name="운세")
    async def fortune(self, ctx):
        """!운세: 오늘의 운세를 알려줍니다."""
        choice = random.choice(self.fortunes)
        # 멘션과 결과 조합
        await ctx.send(f"🍀 {ctx.author.mention}님의 운세: {choice}")

async def setup(bot):
    await bot.add_cog(Fortune(bot))
