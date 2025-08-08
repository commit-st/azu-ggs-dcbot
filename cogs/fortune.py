import random
import discord
from discord.ext import commands
from discord import app_commands
from discord.utils import escape_markdown as esc

class Fortune(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        # 운세 멘트 리스트 (예시)
        self.fortunes = [
            "오늘은 행복한 하루가 될 거예요!",
            "대화를 할 때 신중해야 할 것 같아요.",
            "작은 행운이 연달아 찾아올 수 있어요.",
            "새로운 제안을 받을 수 있어요. 열린 마음으로!",
            "휴식이 필요한 날. 컨디션 조절에 신경 쓰세요.",
            "뜻밖의 사람에게서 도움을 받을 수 있어요.",
            "지출 관리가 필요한 날. 충동구매 주의!",
            "집중력이 높아져 성과가 납니다.",
            "오래 미룬 일을 시작하기 아주 좋아요.",
            "연락이 끊겼던 사람과 인연이 닿을지도.",
            "작은 실수가 큰 교훈이 됩니다.",
            "아이디어가 반짝! 메모해 두세요.",
            "건강운 상승. 가벼운 운동이 행운을 불러요.",
            "주변 정리를 하면 좋은 기운이 들어옵니다.",
            "협업운 좋음. 혼자보다 함께가 효율적!",
            "감정 기복 주의. 깊게 숨 쉬고 천천히.",
            "기다리던 소식이 도착합니다.",
            "새로운 취미가 좋은 변화의 신호가 돼요.",
            "감사 인사가 또 다른 행운을 부릅니다.",
            "작은 선물이 큰 기쁨을 가져와요."
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
            "평소보다 직감이 정확해요. 첫 느낌을 믿어보세요.",
            "작은 정리가 큰 행운을 부릅니다. 책상부터 가볍게.",
            "연락하고 싶던 사람에게 먼저 안부를 전해보세요.",
            "금전운 무난. 쓰기보다 아끼는 쪽이 이득이에요.",
            "컨디션 관리가 포인트. 물과 스트레칭 자주 하기.",
            "아이디어가 실물이 될 조짐. 메모하고 한 걸음 실행!",
            "돌아가면 더 빨라요. 기본기 점검이 효율을 올립니다.",
            "작은 선의가 돌아옵니다. 감사 인사를 아끼지 마세요.",
            "새로운 도구 배우기 좋은 날. 30분만 투자해도 성과.",
            "타이밍이 핵심. 중요한 결정은 오후로 미루는 게 유리.",            
        ]

    # 접두사(!) 명령어
    @commands.command(name="운세")
    async def fortune_prefix(self, ctx: commands.Context):
        """!운세: 오늘의 운세를 알려줍니다."""
        choice = random.choice(self.fortunes)
        await ctx.send(f"🍀 {ctx.author.mention}님의 운세: **{esc(choice)}**")

    # 슬래시 명령어(ASCII name) + 한국어 로컬라이징으로 "/운세" 표기
    @app_commands.command(name="fortune", description="오늘의 운세를 알려줍니다.")
    async def fortune_slash(self, interaction: discord.Interaction):
        choice = random.choice(self.fortunes)
        await interaction.response.send_message(f"🍀 {interaction.user.mention}님의 운세: **{esc(choice)}**")

    # (선택) 동기화 커맨드 — 봇 소유자만
    @commands.command(name="sync")
    @commands.is_owner()
    async def sync_app_commands(self, ctx: commands.Context):
        await self.bot.tree.sync()
        await ctx.send("✅ 슬래시 명령어 동기화 완료.")

# --- 한국어 로컬라이징 (discord.py 2.3+)
class SimpleKoTranslator(app_commands.Translator):
    async def translate(self, string: app_commands.locale_str, locale: discord.Locale, context: app_commands.TranslationContext):
        if locale is discord.Locale.korean:
            table = {
                # 슬래시 명령어 이름
                "fortune": "운세",
                # 설명
                "오늘의 운세를 알려줍니다.": "오늘의 운세를 알려줍니다.",
            }
            return table.get(str(string))
        return None

async def setup(bot: commands.Bot):
    try:
        await bot.tree.set_translator(SimpleKoTranslator())
    except Exception:
        pass
    await bot.add_cog(Fortune(bot))
