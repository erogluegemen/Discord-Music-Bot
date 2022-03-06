
import discord
from discord.ext import commands
from random import choice


class main_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```

## Genel Komutlar ##
-help -> Bütün komutları gösterir.
-disconnect / dc -> Botu geldiği yere geri gönderir.
-ping -> pingi kontrol eder.
-clear -> belirtilen kadar mesajı siler.

## Müzik Komutları ##
-p {şarkı adı / link} -> Youtubeda bulduğu şarkıyı açar.
-l / list -> Mevcut müzik sırasını görüntüler.
-s / skip -> Çalan şarkıyı atlar.
-lyrics {şarkıcı - şarkı adı}-> Şarkının sözlerinin gösterir.

## Mesaj Komutları ##
-siir -> Rastgele bir şiir verir.(Büyük ihtimal küfürlü)
-soz -> Panky şekli şemali misali günün sözünü verir.(Küfürlü olma olasılığı var)
-recommend ->Söylenilen filme benzer 10 film önerir.

## Şans Komutları ##
-coinflip -> Yazı tura atar.
-dice -> Zar atar.
-rps -> Taş-Kağıt-Makas yapar.
-rr -> Rus ruleti.
-sor -> Merak ettiğin şeyi sor cevaplasın.

```
"""
        self.text_channel_list = [""] #kendi channel_id'niz.

#Connect

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Yine Geldik Mekana {self.bot.user} ({self.bot.user.id})')
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_list.append(channel)

#Reconnect

    @commands.Cog.listener()
    async def on_resumed(self):
        print('Arap Şükrü Tekrar Bağlandı!')

#Error Handling

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        error_messages = ["Biz böyle bir talimat vermedik!","Sen ne diyon??","Kardeşimsin bu ne demek","Bir daha yaz anlamadım"]

        if isinstance(error, commands.CommandNotFound):
            await ctx.send(choice(error_messages))

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('Sana böyle bi yetki verdiğimi hatırlamıyorum!')

#Help

    @commands.command(name="help", help="Bütün komutları gösterir.", pass_context=True)
    async def help(self, ctx):
        await ctx.send(self.help_message)

#Disconnect

    @commands.command(name="disconnect", help="Serverdan ayrılır.", pass_context=True)
    async def disconnect(self, ctx):
        disconnect_messages = ["Hoççağalın..","Ben Kaçar","Gittim o zaman","İstenmediğim yerde durmam"]
        await ctx.send(choice(disconnect_messages))
        await ctx.voice_client.disconnect()


    @commands.command(name="dc", help="Serverdan ayrılır.", pass_context=True)
    async def dc(self, ctx):
        disconnect_messages = ["Hoççağalın..", "Ben Kaçar", "Gittim o zaman", "İstenmediğim yerde durmam"]
        await ctx.send(choice(disconnect_messages))
        await ctx.voice_client.disconnect()






