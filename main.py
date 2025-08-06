import asyncio
import aiohttp
from aiohttp import web
import discord, os, logging
from discord.ext import commands
from dotenv import load_dotenv

# Health Check API
async def health_check(request):
    return web.Response(text="OK", status=200)

async def start_web_server():
    app = web.Application()
    app.router.add_get('/health', health_check)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8000)
    await site.start()

# Self-Ping to stay awake
async def ping_self():
    await bot.wait_until_ready()
    url = os.environ.get('KOYEB_URL')
    while not bot.is_closed():
        try:
            async with aiohttp.ClientSession() as session:
                await session.get(url)
        except Exception:
            pass        
        await asyncio.sleep(180)

# Discord Bot setup
load_dotenv()
token = os.getenv("DISCORD_TOKEN")
handler = logging.FileHandler("discord.log", encoding="utf-8", mode="w")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# 동기화할 서버 ID 두 개
GUILD_IDS = [
    1376600438899478639,  # 테스트 서버 ID
    1342270063759196210,  # 그그수 서버 ID
]

class MyBot(commands.Bot):
    async def setup_hook(self):
        # Cog 로드
        for fn in os.listdir("./cogs"):
            if fn.endswith(".py"):
                await self.load_extension(f"cogs.{fn[:-3]}")

        # 슬래시 커맨드 각 길드에 동기화
        for guild_id in GUILD_IDS:
            guild = discord.Object(id=guild_id)
            await self.tree.sync(guild=guild)
        print(f"Slash commands synced to guilds: {GUILD_IDS}")

bot = MyBot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} 연결 완료!🩵")
    bot.loop.create_task(start_web_server())
    bot.loop.create_task(ping_self())

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
