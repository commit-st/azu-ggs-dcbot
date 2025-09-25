import random
import discord
from discord.ext import commands
from discord import app_commands
from discord.utils import escape_markdown as esc  # 굵게 처리 시 마크다운 이스케이프

class MenuRecommend(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.fortunes = [
            "피자", "로제떡볶이", "토마토파스타", "짜장면", "크림우동", "불닭볶음면", "닭갈비", "제육볶음", "닭볶음탕", "후토마끼", "치즈그라탕",
            "고구마치즈돈까스", "경양식돈까스와 스프", "안심/등심 돈까스", "타코야끼", "까르보불닭", "계란초밥", "장새우초밥", "참치마요", "치킨마요",
            "볶음우동", "차돌짬뽕", "라면", "엽떡", "크리스피도넛", "서브웨이 B.L.T", "키토김밥", "포케", "돈코츠라멘", "치즈김밥", "순두부열라면",
            "에그마요 샌드위치", "김치찌개", "로제찜닭", "참치김밥", "마라샹궈", "마라탕", "야키니쿠", "바질토마토에이드와 잠봉뵈르 샌드위치",
            "비빔밥", "두부김치", "연어초밥", "돈부리", "우삼겹덮밥", "된장찌개", "규카츠", "메밀소바",
            "샤브샤브", "스테이크", "치즈버거", "후라이드치킨", "팟타이", "함박 스테이크", "햄버거", "마파두부", "고추잡채",
            "나시고랭", "부리또", "떡볶이에 튀김", "필라프", "카레", "김치볶음밥", "순두부찌개", "부대찌개", "갈비탕", "비빔밥",
            "피쉬앤칩스", "리조또", "크로크무슈", "클럽샌드위치", "파니니", "생선구이", "오징어/낙지볶음", "양념/간장게장",
            "타코", "뼈해장국", "감자탕", "냉면에 고기", "시리얼", "수제비", "쌀국수", "잔치국수", "감자 샐러드", "토마토달걀볶음",
            "연어 샐러드", "낙지김치죽", "쇠고기야채죽", "호박죽", "삼겹살 구이", "해물짬뽕", "오므라이스", "간장계란밥", "오차즈케",
            "감바스", "마제소바", "갈비만두", "고기만두", "보쌈/족발", "교촌 허니콤보", "굽네 고추바사삭", "BHC 뿌링클", "지코바로 치밥", "BBQ 황금올리브",
            "곱창/대창/막창", "KFC", "짜파구리", "짜계치", "너구리 라면", "오꼬노미야끼", "오야꼬동", "꿔바로우", "캘리포니아롤",
            "라자냐", "투움바 파스타", "전복죽", "훈제오리", "프리타타", "떡만둣국", "오뎅탕", "닭발", "가츠동", "회", "회덮밥",
            "육회비빔밥", "비빔국수", "칼국수", "새우볶음밥", "콩국수", "전/부침개", "순대볶음", "짜장밥", "소시지야채볶음", "그릭 요거트",
            "잡채", "샤오롱바오", "사시미", "간장찜닭", "스키야키", "계란말이", "해물찜", "해물탕", "조개구이", "밀푀유나베", "양꼬치",
            "맥앤치즈", "뿌팟퐁커리", "분짜", "목살김치찜", "계란후라이", "닭가슴살+고구마+야채", "콩나물국밥", "포켓몬빵이랑 우유", "삼각김밥", "컵누들",
            "곤약국수", "컵밥", "밥버거", "노랑통닭 알마치", "열무국수", "열무비빔밥", "굴밥", "조개탕", "물", "생오이/당근에 장 찍어먹기",
        ]

    def _menu_message(self, user_mention: str, choice: str) -> str:
        return f"😋 {user_mention}님을 위한 메뉴 추천! **{esc(choice)}** 어떠세요? 맛있게 드세요!🍽️"

    @commands.command(name="메추")
    async def fortune_prefix(self, ctx: commands.Context):
        choice = random.choice(self.fortunes)
        await ctx.send(self._menu_message(ctx.author.mention, choice))

    @app_commands.command(name="menu", description="메뉴를 추천해드려요!")
    async def fortune_slash(self, interaction: discord.Interaction):
        choice = random.choice(self.fortunes)
        await interaction.response.send_message(self._menu_message(interaction.user.mention, choice))

# 한국어 로컬라이징: /menu → /메추 로 보이게
class SimpleKoTranslator(app_commands.Translator):
    async def translate(self, string: app_commands.locale_str, locale: discord.Locale, context: app_commands.TranslationContext):
        if locale is discord.Locale.korean:
            table = {"menu": "메추", "메뉴를 추천해드려요!": "메뉴를 추천해드려요!"}
            return table.get(str(string))
        return None

async def setup(bot: commands.Bot):
    try:
        await bot.tree.set_translator(SimpleKoTranslator())
    except Exception:
        pass
    await bot.add_cog(MenuRecommend(bot))
