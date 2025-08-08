import random
import discord
from discord.ext import commands
from discord import app_commands

class LuckyItem(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        # 행운의 아이템 목록
        self.lucky_items = [
            "패턴 양말", "파란 펜", "500원 동전", "고양이 털뭉치", "키링", "감자칩", "추리 소설책", "영화 티켓", "WD-40", "지갑", "1000짜리 지폐 1장",
            "우산", "헤어핀", "노트 1장", "목걸이", "오렌지주스", "보조배터리", "향수", "워치 스트랩", "lp판",
            "손수건", "종이학", "네잎클로버 스티커", "반지", "핸드크림", "비타민", "게임기", "압정", "띠부띠부씰", "키캡", "부채", "코스터",
            "폰 스트랩", "하트 스티커", "책갈피", "슬리퍼", "머그컵", "SF 소설책", "만화책", "장미꽃", "향초", "별자리 관련 아이템",
            "버튼뱃지", "포스트잇", "지우개", "동전지갑", "키링", "피규어", "봉제인형", "가챠 캡슐", "포토카드", "귀여운 코롯토",
            "네임펜", "별 모양 스티커", "물티슈", "텀블러", "이어폰", "캔 음료", "스프링 노트", "가습기", "인공눈물", "마스킹 테이프",
        ]

    # 내부 공용 포맷터
    def _lucky_message(self, user_mention: str, item: str) -> str:
        return f"🍀 {user_mention} 오늘의 행운 아이템: **{item}**"

    # 접두사(!) 명령어 — 한글 가능
    @commands.command(name="행운아이템")
    async def lucky_prefix(self, ctx: commands.Context):
        item = random.choice(self.lucky_items)
        await ctx.send(self._lucky_message(ctx.author.mention, item))

    # 슬래시 명령어 — 기본 이름은 ASCII, 현지화로 한글 노출 지원
    @app_commands.command(name="luckyitem", description="오늘의 행운 아이템을 뽑아요!")
    async def lucky_slash(self, interaction: discord.Interaction):
        item = random.choice(self.lucky_items)
        await interaction.response.send_message(self._lucky_message(interaction.user.mention, item))

    # 컨텍스트 메뉴 — 유저 우클릭
    @app_commands.context_menu(name="행운 아이템 뽑기")
    async def lucky_user_ctx(self, interaction: discord.Interaction, member: discord.Member):
        item = random.choice(self.lucky_items)
        await interaction.response.send_message(self._lucky_message(member.mention, item))

# --- 한국어 로컬라이징 설정 (discord.py 2.3+)
class SimpleKoTranslator(app_commands.Translator):
    async def translate(self, string: app_commands.locale_str, locale: discord.Locale, context: app_commands.TranslationContext):
        # 한국어 UI에서만 치환
        if locale is discord.Locale.korean:
            table = {
                # 명령어 이름
                "luckyitem": "행운아이템",
                # 설명(그대로 노출)
                "오늘의 행운 아이템을 뽑아요!": "오늘의 행운 아이템을 뽑아요!",
            }
            return table.get(str(string))
        return None

async def setup(bot: commands.Bot):
    # 번역기 등록 (지원 버전에서만 작동). 미지원이면 조용히 패스.
    try:
        await bot.tree.set_translator(SimpleKoTranslator())
    except Exception:
        pass
    await bot.add_cog(LuckyItem(bot))
