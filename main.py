import asyncio
import aiohttp
from aiohttp import web
import discord, os, logging
from discord.ext import commands
from dotenv import load_dotenv

# ------------------------------
# Health Check API
# ------------------------------
async def health_check(request):
    return web.Response(text="OK", status=200)

async def start_web_server():
    app = web.Application()
    # 루트/헬스 모두 200 반환 (플랫폼/모니터 호환)
    app.router.add_get('/', health_check)
    app.router.add_get('/health', health_check)

    runner = web.AppRunner(app)
    await runner.setup()

    # 호스팅 환경이 요구하는 PORT 사용 (기본 8000)
    port = int(os.getenv('PORT', '8000'))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"[health] web server started on :{port}")

# ------------------------------
# Self-Ping to stay awake (5분)
# ------------------------------
async def ping_self():
    await bot.wait_until_ready()

    base = (os.environ.get('KOYEB_URL') or '').strip()
    if not base:
        print("[keepalive] KOYEB_URL not set. keepalive disabled.")
        return

    # /health 보장
    if base.endswith('/'):
        url = base + 'health'
    else:
        url = base + '/health'

    timeout = aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        while not bot.is_closed():
            try:
                async with session.get(url) as resp:
                    print(f"[keepalive] {url} -> {resp.status}")
            except Exception as e:
                print(f"[keepalive] error: {e!r}")
            # 300초(=5분)로 고정. (플랫폼 정책 우회 목적)
            await asyncio.sleep(300)

# ------------------------------
# Discord Bot setup
# ------------------------------
load_dotenv()
token = os.getenv("DISCORD_TOKEN")
handler = logging.FileHandler("discord.log", encoding="utf-8", mode="w")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

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

        # 슬래시 커맨드 길드 동기화
        for guild_id in GUILD_IDS:
            guild = discord.Object(id=guild_id)
            await self.tree.sync(guild=guild)
        print(f"Slash commands synced to guilds: {GUILD_IDS}")

bot = MyBot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} 연결 완료!🩵")
    # 웹서버 및 keepalive 시작
    bot.loop.create_task(start_web_server())
    bot.loop.create_task(ping_self())

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
