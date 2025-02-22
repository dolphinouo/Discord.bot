from http import client
import random
import discord
from discord.ext import commands
import asyncio

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

@bot.command()
async def timer(ctx, seconds: int):
    if seconds <= 0:
        await ctx.send("⏰ 請輸入大於0的秒數！")
        return
    await ctx.send(f"⏳ 倒數計時開始：{seconds}秒")
    await asyncio.sleep(seconds)
    await ctx.send(f"🔔 時間到！{ctx.author.mention}，你的 {seconds} 秒計時結束啦！")

@bot.command()
async def inspire(ctx):
    quotes = [
        "🌟 每一步都算數，即使是小步子也能帶你走向遠方！",
        "💪 不要害怕失敗，失敗只是成功的前奏！",
        "🌈 生活就像彩虹，需要陽光和雨水才能顯現美麗。",
        "✨ 相信自己，你比你想像的還要厲害！"
    ]
    await ctx.send(random.choice(quotes))

@bot.command()
async def guess(ctx):
    number = random.randint(1, 100)
    attempts = 0
    await ctx.send("🎮 我已經想好了一個1到100之間的數字，開始猜吧！你有10次機會！")
    
    while attempts < 10:
        try:
            msg = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)
            guess = int(msg.content)
            attempts += 1
            
            if guess < number:
                await ctx.send(f"⬆️ 太小了！還有 {10 - attempts} 次機會。")
            elif guess > number:
                await ctx.send(f"⬇️ 太大了！還有 {10 - attempts} 次機會。")
            else:
                await ctx.send(f"🎉 恭喜你！猜對了，答案是 {number}，你用了 {attempts} 次！")
                return
        except ValueError:
            await ctx.send("❌ 請輸入一個有效的數字！")
        except asyncio.TimeoutError:
            await ctx.send("⏰ 時間到！你太慢啦～")
            return
    
    await ctx.send(f"😢 遊戲結束！機會用完了，正確答案是 {number}。")

@bot.command()
async def time(ctx):
    from datetime import datetime
    now = datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
    await ctx.send(f"⏲️ 現在時間是：{now}")

bot.run("Your_bot_token")
