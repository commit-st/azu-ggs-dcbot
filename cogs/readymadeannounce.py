import discord
from discord.ext import commands

class CustomAnnounce(commands.Cog):
    """
    !rma
    """
    def __init__(self, bot):
        self.bot = bot
        self.embeds = [
            discord.Embed()
                .set_image(url="https://cdn.discordapp.com/attachments/1405328897259733143/1405375300530864339/gif-discord.gif?ex=689e993e&is=689d47be&hm=067bf3838fe77503f40cc11adc080221dc4de376409c15989a9af017c44a0b1e&"),

            discord.Embed(
                color=7850751,
                title="✦ 규칙 및 공지사항 ✦\n",
                description=(
                    ". · . · . ·  . · . · . · . · . ·  . · . · . ·  . · . · . ·  . · . · . ·  . · . · . ·  . · . · .\n"
                    "1️⃣　그림방에서 **게임 화면 공유**를 오래하거나 여럿이서 할 경우는 **휴식으로 이동**해 주세요.\n\n"
                    "2️⃣　정치적이나 **사회적으로 쉽지 않은 이야기는 금지** 🚫\n\n"
                    "3️⃣　갤러리에 업로드 되는 **그림 유출 금지** 🚫\n\n"
                    "4️⃣　수위제한은 따로 없지만 지속적이거나 **극심한 수위의 채팅 분위기는 지양**합니다.\n\n"
                    "5️⃣　방 분위기를 심각하게 해치거나 **다른 이용자의 활동을 방해하는 행위**는 **관리자의 경고 후 추방**될 수 있습니다.\n\n"
                    "6️⃣　서로 작업 환경이 맞지 않거나, **다른 대화 주제로 떠들고 싶을 경우 다른 방을 사용**합니다. (그림2, 휴식2 등)\n\n"
                    "7️⃣　**마이크, 화면 공유는 자유**입니다.\n　*📢  음성 채팅에 들어온 이력이 있어야 개편 조치되지 않습니다.*\n\n"
                    ". · . · . ·  . · . · . · . · . ·  . · . · . ·  . · . · . ·  . · . · . ·  . · . · . ·  . · . · .\n\n"
                    "✦ 웬만해서는 프리한 분위기입니다!  자유롭게 활동해 주세요! ✦"
                )
            )
                .set_author(
                    name="𖤐⭒๋࣭ ⭑",
                    icon_url="https://cdn.discordapp.com/attachments/1405328897259733143/1405328897473511525/1.png?ex=689e6e06&is=689d1c86&hm=02ca41c753d0e12a4b1613f7105ac8fec5cf233d14e34df66cffc246ab3db1fb&",
                )
                .set_footer(
                    text="건의사항 - @구운감자 @샥 @숯 @복진명 ",
                    icon_url="https://media.discordapp.net/attachments/1405328897259733143/1405358068501581897/22.png?ex=689e8931&is=689d37b1&hm=a9381f3c0f16f517162fffeb6c648235cb8e941393fe1fd65c93a1fc85f4119b&=&format=webp&quality=lossless&width=900&height=900",
                ),

            discord.Embed()
                .set_image(url="https://cdn.discordapp.com/attachments/1405328897259733143/1405375299645866045/pastel-divider.gif?ex=689e993e&is=689d47be&hm=b7e9a048944d361b6fe5f7c993a95812da0517e4d7c89a4d5fa00098adac0360&"),

            discord.Embed(
                color=12168447,
                title="활성화를 위한 멤버 개편 안내",
                description=(
                    ". · . · . ·  . · . · . · . · . ·  . · . · . ·  . · . · . ·  . · . · . ·  . · . · . ·  . · . · .\n\n"
                    "디코방 활성화를 위해 **매달마다 멤버 개편이 진행**됩니다!\n"
                    "기준에 따라 퇴장될 예정이니 활동에 참고해 주세요! \n"
                    "개편으로 나가신 분은 **입장 재신청 가능**합니다!\n\n"
                    "**🔹 기준: 최근 1개월 동안 음성 채팅방 접속 기록이 없는 멤버 🔹**\n"
                    "　　　　*>> 마이크를 켜지 않은 상태로 듣고 채팅만 해도 가능합니다!*\n\n"
                    "✦ 개인적인 사정으로 접속이 어려운 분 → 관리자에게 DM\n"
                    "✦ 불가피하게 퇴장한 분 → 관리자 [오픈카톡](https://open.kakao.com/o/sBqK1Aoc)\n\n"
                    "더욱 즐거운 방을 만들어갈 수 있도록 여러분의 이해와 협조 부탁드려요!"
                )
            )
                .set_author(
                    name="𖤐⭒๋࣭ ⭑",
                    icon_url="https://cdn.discordapp.com/attachments/1405328897259733143/1405328897473511525/1.png?ex=689e6e06&is=689d1c86&hm=02ca41c753d0e12a4b1613f7105ac8fec5cf233d14e34df66cffc246ab3db1fb&",
                ),

            discord.Embed()
                .set_image(url="https://cdn.discordapp.com/attachments/1405328897259733143/1405375299645866045/pastel-divider.gif?ex=689e993e&is=689d47be&hm=b7e9a048944d361b6fe5f7c993a95812da0517e4d7c89a4d5fa00098adac0360&"),

            discord.Embed()
                .set_thumbnail(url="https://media.discordapp.net/attachments/1405328897259733143/1405375300166094970/Original.webp?ex=689e993e&is=689d47be&hm=f6d4a0b3639260bcd87e171333f4d8557df1166caf85479928c5e3561102992c&=&animated=true&width=503&height=554"),
        ]

    @commands.command(name="rma")
    @commands.has_permissions(administrator=True)
    async def rma(self, ctx: commands.Context):
        for embed in self.embeds:
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(CustomAnnounce(bot))
