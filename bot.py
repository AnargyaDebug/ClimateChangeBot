import discord
import random
from discord.ext import commands
from discord import Intents

from classification import classify

# intents = Intents.all()
# intents.message_content = True
intents = Intents.all()
bot = commands.Bot(command_prefix=";", intents=intents)

uploaded_images = {}

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def classify(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            image_path = attachment.filename
            await attachment.save(f"./{image_path}")
            result = classify(model_path="res/classify/keras_model.h5", labels_path="res/classify/labels.txt", img_path=f"./{attachment.filename}")
            await ctx.send(result[0])
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


 async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            image_path = attachment.filename
            await attachment.save(f"../{attachment.filename}")
            result = classify(model_path="res\classify\keras_model.h5", labels_path="res\classify\labels.txt", image_path=f"../{attachment.filename}")
            await ctx.send(result)
    else:
        await ctx.send("You forgot to upload the image >:(")

        
@bot.command("recycletrashtips")
async def recycling_tips(ctx):
    await ctx.send("""
                   1. Recycling or reusing things like plastics is a great way to battle pollution and climate change! Here are 10 tips on how to do so:
                   2. Paper Power: Recycling paper means we can use it again to make new paepr. So, don't throw away those old drawings, school papers, or newspapers. Put them in the recycling bin!
                   3. Clever Cans: Aluminum cans, like soda cans, are like superheroes of recycling. They can be turned into new cans really easily. So, collect them and put them in the recycling bin.
                   4. Plastic Love: Some plastic bottles and containers can be recycled, but not all of them. Look for a recycling symbol on the bottom with a number inside. If it's a 1, 2, or 5, you can recycle it. If not, it goes in the regular trash.
                   5. Glass Goodness: Glass bottles and jars are strong and can be recycled over and over. So, when you're done with a glass jar of peanut butter or a glass bottle of juice, rinse it out and recycle it.
                   6. Cardboard Fun: Big cardboard boxes from packages or pizza can be recycled. Flatten them and put them in the recycling bin. It's like giving them a second life!
                  """)
    await ctx.send("""
                   7. No Greasy Stuff: Things covered in food or grease, like pizza boxes, can't be recycled because they make the other stuff dirty. So, it's better to put them in the trash.
                   8. Battery Care: Batteries from toys or gadgets can be harmful if not recycled properly. Look for special drop-off spots for old batteries or electronic waste.
                   9. Reduce and Reuse: Try to use less stuff that needs to be recycled. Reuse items when you can, like turning an old jar into a pencil holder instead of buying a new one.
                   10. Paper vs. Plastic: At the store, choose reusable bags or paper bags instead of single-use plastic bags. This helps reduce plastic waste.
                   11. Learn and Teach: Share what you know about recycling with your friends and family. The more people know, the better we can take care of our planet!
                   Remember, recycling is like giving things a second chance to be useful. It's a great way to help the environment and make the world a cleaner, better place.
                  """)
