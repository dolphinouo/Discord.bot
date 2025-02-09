from http import client
import random
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "#", intents = intents)

@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

@bot.command()
async def Hello(ctx):
    await ctx.send("Hello, world!")

@bot.command()
async def dice(ctx, sides: int = 6):
    result = random.randint(1, sides)
    await ctx.send(f"🎲 你擲出了 {result} 點")

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f"🏓 Pong! 延遲時間：{latency} ms")

@bot.command()
async def choose(ctx, *choices: str):
    if not choices:
        await ctx.send("請提供選項，例如：#choose 蘋果 香蕉 橘子")
        return
    choice = random.choice(choices)
    await ctx.send(f"🤔 我選擇了：{choice}")


@bot.command()
async def calc(ctx, num1: float, operator: str, num2: float):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            await ctx.send("❌ 無法除以零！")
            return
        result = num1 / num2
    else:
        await ctx.send("❌ 無效的運算符號，請使用 +, -, *, /")
        return
    await ctx.send(f"🧮 計算結果：{result}")

@bot.command()
async def mimic(ctx, *, message: str):
    await ctx.send(f"🗣️ {message}")

@bot.command()
async def cat(ctx):
    cat_images = [
        "https://cataas.com/cat",
        "https://cataas.com/cat/cute",
        "https://cataas.com/cat/sleepy"
    ]
    await ctx.send(random.choice(cat_images))


bot.run("YOUR_BOT_TOKEN")