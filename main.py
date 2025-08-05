import discord, os, logging
from discord.ext import commands
from dotenv import load_dotenv

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

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
