import random
import discord
from discord.ext import commands
from discord import app_commands
from discord.utils import escape_markdown as esc

class LuckyItem(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.lucky_items = [
            "패턴 양말", "파란 펜", "500원 동전", "고양이 털뭉치", "키링", "감자칩", "추리 소설책", "영화 티켓", "WD-40", "지갑", "1000짜리 지폐 1장",
            "우산", "헤어핀", "노트 1장", "목걸이", "오렌지주스", "보조배터리", "향수", "워치 스트랩", "lp판",
            "손수건", "종이학", "네잎클로버 스티커", "반지", "핸드크림", "비타민", "게임기", "압정", "띠부띠부씰", "키캡", "부채", "코스터",
            "폰 스트랩", "하트 스티커", "책갈피", "슬리퍼", "머그컵", "SF 소설책", "만화책", "장미꽃", "향초", "별자리 관련 아이템",
            "버튼뱃지", "포스트잇", "지우개", "동전지갑", "키링", "피규어", "봉제인형", "가챠 캡슐", "포토카드", "귀여운 코롯토",
            "네임펜", "별 모양 스티커", "물티슈", "텀블러", "이어폰", "캔 음료", "스프링 노트", "가습기", "인공눈물", "마스킹 테이프",
            "체스 말", "도토리", "폴라로이드 사진", "스티커북", "콘택트렌즈", "단풍잎 책갈피", "룸 스프레이",
            "열쇠고리 손전등", "미니 초콜릿", "손소독제", "바람개비", "헤어 스프레이", "바디 오일", "프로폴리스 캔디", "메뉴판",
            "자물쇠 열쇠", "모래시계", "퍼즐 조각", "미니카", "머리띠", "머그컵", "재활용 빨대", "카드", "안약", "마우스 패드", 
            "칫솔", "라디오", "단추", "계산기", "타블렛 펜", "영어책",
            "석고방향제", "리본핀", "노란색 형광펜", "종이컵", "뽀모도로 타이머",
            "차 티백", "손거울", "네컷사진", "마그넷", "실타래",
            "우드 스푼", "손목시계", "퍼즐큐브", "옛날 동전", "무드등",
            "이쑤시개", "면봉", "레고 블럭", "헤드셋", "미스트",

        ]

    def _lucky_message(self, user_mention: str, item: str) -> str:
        return f"🍀 {user_mention} 오늘의 행운 아이템: **{esc(item)}**"

    @commands.command(name="행운아이템")
    async def lucky_prefix(self, ctx: commands.Context):
        item = random.choice(self.lucky_items)
        await ctx.send(self._lucky_message(ctx.author.mention, item))

    @app_commands.command(name="luckyitem", description="오늘의 행운 아이템을 뽑아요!")
    async def lucky_slash(self, interaction: discord.Interaction):
        item = random.choice(self.lucky_items)
        await interaction.response.send_message(self._lucky_message(interaction.user.mention, item))


# ✅ 클래스 밖으로 이동한 컨텍스트 메뉴
@app_commands.context_menu(name="행운 아이템 뽑기")
async def lucky_user_ctx(interaction: discord.Interaction, member: discord.Member):
    bot = interaction.client  # type: ignore
    cog = bot.get_cog("LuckyItem")
    if cog is None:
        await interaction.response.send_message("⚠️ LuckyItem cog가 아직 로드되지 않았어요.", ephemeral=True)
        return
    item = random.choice(cog.lucky_items)
    await interaction.response.send_message(cog._lucky_message(member.mention, item))


# (선택) 한국어 로컬라이징
class SimpleKoTranslator(app_commands.Translator):
    async def translate(self, string: app_commands.locale_str, locale: discord.Locale, context: app_commands.TranslationContext):
        if locale is discord.Locale.korean:
            table = {"luckyitem": "행운아이템", "오늘의 행운 아이템을 뽑아요!": "오늘의 행운 아이템을 뽑아요!"}
            return table.get(str(string))
        return None


async def setup(bot: commands.Bot):
    try:
        await bot.tree.set_translator(SimpleKoTranslator())
    except Exception:
        pass
    await bot.add_cog(LuckyItem(bot))
    bot.tree.add_command(lucky_user_ctx)
