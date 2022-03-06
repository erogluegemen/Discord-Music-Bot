from discord.ext import commands
import discord
import random

class chance_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

#Coinflip Command

    @commands.command(name="coinflip", help="Yazı-Tura atar.", pass_context=True)
    async def coinflip(self, ctx):
        at = random.randint(0,1)
        if at == 0:
            await ctx.send("Yazı!!")
        if at == 1:
            await ctx.send("Tura!!")

#Dice Command

    @commands.command(name="dice", help="Zar atar.", pass_context=True)
    async def dice(self,ctx):
        zar1 = random.randint(1,6)
        zar2 = random.randint(1, 6)
        await ctx.send("Birinci Zar: {}\nİkinci Zar: {}".format(zar1, zar2))
        if zar1 == zar2 == 1:
            await ctx.send("Hep Yek!")
        if zar1 == zar2 == 2:
            await ctx.send("Dubara!")
        if zar1 == zar2 == 3:
            await ctx.send("Dü Se!")
        if zar1 == zar2 == 4:
            await ctx.send("Dört Cihar!")
        if zar1 == zar2 == 5:
            await ctx.send("Dü Beş!")
        if zar1 == zar2 == 6:
            await ctx.send("Dü Şeş!")

#Rock-Paper-Scissors Command

    @commands.command(name="rps", help="Taş kağıt makas yapar.", pass_context=True)
    async def rps(self, ctx):
        case = ["Taş", "Kağıt", "Makas"]
        await ctx.send("{}!!".format(random.choice(case)))

#Russian Roulette Command
    @commands.command(name="rr", help="Taş kağıt makas yapar.", pass_context=True)
    async def rr(self, ctx):

        slot = ["BAM!!", "click", "click", "click", "click", "click"]
        choice = random.choice(slot)
        dead_messages = ["Öldün çık","Rip","Esselaaaa","Allah rahmet eylesin kanks", "Ölüyorum anlasanaa","Seç: Cennet mi Cehennem mi?"]
        survive_messages = ["Yaşıyosun(şimdilik..)", "Bugün seni öldürmeyen yaradan için naptın","Öldürmeyen Allah öldürmüyo", "Tutukluk yapan mermiydi ama ben de sende tutuklu kaldım.."]
        if choice == "BAM!!":
            await ctx.send(random.choice(dead_messages))

        else:
            await ctx.send(random.choice(survive_messages))

#8ball Command

    @commands.command(name="sor", help="Merak ettiğin şeyi sor.", pass_context=True)
    async def sor(self, ctx, *, question):
        responses = ["Bu kesin.",
                     "Kesinlikle öyle.",
                     "Şüphesiz",
                     "Şakasız",
                     "Evet, kesinlikle.",
                     "Gördüğüm kadarıyla, evet.",
                     "Büyük ihtimalle.",
                     "İyi görünüyor.",
                     "Evet.",
                     "İşaretler eveti gösteriyor.",
                     "Emin değilim tekrar dene.",
                     "Daha sonra tekrar sor.",
                     "Buna şimdi cevap vermesem daha iyi",
                     "Ben buna yorum yapamam..",
                     "Netttt",
                     "Benim cevabım hayır.",
                     "Kaynaklarıma göre hayır.",
                     "İçimden bi ses olmaz diyor.",
                     "Sonu çok iyi görünmüyor..",
                     "Şüpheli bi tık.."]

        await ctx.send(f'Soru: {question}\nCevap: {random.choice(responses)}')
        print("Soru cevaplandı!")
