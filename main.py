import discord
from discord.ext import commands
from main_cog import main_cog
from music_cog import music_cog


bot = commands.Bot(command_prefix='-') #Komut işaretini seçiyoruz
bot.remove_command('help') #Discordun kendi help komutunu atıyoruz ki kendi help komutumuzu yaratalım.
bot.add_cog(main_cog(bot))
bot.add_cog(music_cog(bot))

def read_token():
    with open("token.txt","r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()
bot.run(token)

"""
1-)
read_token kısmı biraz işin şovu.Herkesin discord bot tokenı kendine özel olduğu için bu kodları gizlememiz gerekiyor.
Yoksa herkes erişebilir.

token.txt diye bi dosya oluşturup içine tokenımızı yazıyoruz.Dosya okuma metodu ile ordan da çekiyoruz tokenımızı

2-)
.env diye bi dosya oluşturup içine tokenı atabilirsiniz.Daha sonra os modülünü import edip 
token = os.getenv() ile de getirtebilirsiniz.

3-)
Privacy is overrated diyosanız ya da projenizi sadece localde çalıştırıcaksanız,paylaşmayacaksanız direkt
bot.run(416541616156516) diye ya da daha temiz olması için

token = 416541616156516
bot.run(token) yapabilirsiniz.
"""


