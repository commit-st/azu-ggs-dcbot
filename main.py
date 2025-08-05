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
    url = os.environ['KOYEB_URL']
    while not bot.is_closed():
        try:
            async with aiohttp.ClientSession() as session:
                await session.get(url)
        except:
            pass
        await asyncio.sleep(180)

# Discord Bot setup…
load_dotenv()
token = os.getenv("DISCORD_TOKEN")
handler = logging.FileHandler("discord.log", encoding="utf-8", mode="w")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

class MyBot(commands.Bot):
    async def setup_hook(self):
        for fn in os.listdir("./cogs"):
            if fn.endswith(".py"):
                await self.load_extension(f"cogs.{fn[:-3]}")

bot = MyBot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} 연결 완료!🩵")
    bot.loop.create_task(start_web_server())
    bot.loop.create_task(ping_self())

bot.run(token, log_handler=handler, log_level=logging.DEBUG)

