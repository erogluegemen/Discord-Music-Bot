import discord
from discord.ext import commands

class main_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```
Genel Komutlar:
-help -> Bütün komutları gösterir
-disconnect -> Botu geldiği yere geri gönderir.

Müzik Komutları:
-p <şarkı adı / link> -> Youtubeda bulduğu şarkıyı açar
-list -> Mevcut müzik sırasını görüntüler
-skip -> Çalınmakta olan şarkıyı atlar
```
"""
        self.text_channel_list = []

    #Botun bağlandığında çalışacak bölüm
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_list.append(channel)



    @commands.command(name="help", help="Bütün komutları gösterir", pass_context=True)
    async def help(self, ctx):
        await ctx.send(self.help_message)

    async def send_to_all(self, msg):
        if text_channel in self.text_channel_list:
            self.channel = commands.get_channel(891700345997262919)
            #ÖNEMLİ !!!!! yukarıdaki metin kanalı benim serverimdeki metin kanalının idsi siz de kendinizinkini yapmanız lazım.
            #get_channel kısmında mesajın yazılmasını istediğiniz kanalın id sini kopyalayın
            await self.channel.send(self.help_message)


    #EĞER HER KANAL IDSINI ALAMADIYSANIZ YA DA MESAJIN HER METIN KANALINA GİTMESİNİ İSTİYORSANIZ:
    #YUKARIDAKİ KOD BLOĞUNU SİLİP AŞAĞIDAKİ KOD BLOĞUNU AKTİVE EDİN

    # @commands.command(name="help", help="Bütün komutları gösterir")
    # async def help(self, ctx):
    #     await ctx.send(self.help_message)
    #
    # async def send_to_all(self, msg):
    #     for text_channel in self.text_channel_list:
    #         await text_channel.send(msg)


    @commands.command(name="disconnect", help="Serverdan ayrılır", pass_context=True)
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()





