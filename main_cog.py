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
        #Her kanala help mesajı basmaması için yanlışlıkla bulduğum çözüm.Nasıl çalışıyor anlamadım ama YOLO.
        self.channel = commands.get_channel(782236647239450644)
        await self.channel.send(self.help_message)


    @commands.command(name="disconnect", help="Serverdan ayrılır", pass_context=True)
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()



