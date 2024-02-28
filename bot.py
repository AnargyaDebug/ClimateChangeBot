import discord
import random
from discord.ext import commands

from classification import classify

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=";", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command("classify")
async def classify(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            image_path = attachment.filename
            await attachment.save(f"./{image_path}")
            result = classify(model_path="res/classify/keras_model.h5", labels_path="res/classify/labels.txt", img_path=image_path)
            await ctx.send(result)
    else:
        await ctx.send("You forgot to upload the image >:(")

@bot.command("chemical_waste")
async def chemical_waste(ctx):
    images = ("sample1.jpg", "sample2.jpg", "sample3.jpg", "sample4.jpg", "sample5.jpg", "sample6.jpg", "sample7.jpg", "sample8.jpg", "sample9.jpg", "sample10.jpg")
    with open(f"res/img/chemical_waste/{random.choice(images)}", "rb") as f:
        img = discord.File(f)

    await ctx.send("These are waste products that contain harmful chemicals and are bad for the environment.")
    await ctx.send("Types of chemical waste include pharmaceutical waste, nuclear waste, and more.")
    await ctx.send("Examples of chemical waste include unused batteries, oils of all kinds, and more.")
    await ctx.send(file=img)

@bot.command("greenhouse_gas")
async def greenhouse_gas(ctx):
    images = ("sample1.jpg", "sample2.jpg", "sample3.jpg", "sample4.jpg", "sample5.jpg", "sample6.jpg", "sample7.jpg", "sample8.jpg", "sample9.jpg", "sample10.jpg")
    with open(f"res/img/greenhouse_gas/{random.choice(images)}", "rb") as f:
        img = discord.File(f)

    await ctx.send("These are gasses released through pollution which ruin the atmosphere and may cause lung cancer and other diseases.")
    await ctx.send("Some examples include carbon dioxide (CO2), sulfur dioxide (SO2), nicotine (C10H14N2), carbon monoxide (CO), CFC's (chlorofluorocarbons), and more. These gasses can also trigger acid rain by converting the water (H2O) into acids such as sulfuric acid and carbonic acid.")
    await ctx.send("Greenhouse gasses like CFC's can ruin the ozone layer which protects Earth from UV rays by turning the ozone molecules (O3) into normal oxygen (O2)")
    await ctx.send(file=img)

@bot.command("inorganic_waste")
async def inorganic_waste(ctx):
    images = ("sample1.jpg", "sample2.jpg", "sample3.jpg", "sample4.jpg", "sample5.jpg", "sample6.jpg", "sample7.jpg", "sample8.jpg", "sample9.jpg", "sample10.jpg")
    with open(f"res/img/inorganic_waste/{random.choice(images)}", "rb") as f:
        img = discord.File(f)

    await ctx.send("These are waste products that don't come from living things.")
    await ctx.send("Examples of inorganic waste include leftover packaging, aluminium cans, spoons, yogurt cups, and many-many types of plastics.")
    await ctx.send(file=img)

@bot.command("organic_waste")
async def organic_waste(ctx):
    images = ("sample1.jpg", "sample2.jpg", "sample3.jpg", "sample4.jpg", "sample5.jpg", "sample6.jpg", "sample7.jpg", "sample8.jpg", "sample9.jpg", "sample10.jpg")
    with open(f"res/img/organic_waste/{random.choice(images)}", "rb") as f:
        img = discord.File(f)

    await ctx.send("These are waste products that do come from living things.")
    await ctx.send("Examples of organic waste include leftover food, fruit peels, tissue/toilet paper, paper, and more.")
    await ctx.send(file=img)
