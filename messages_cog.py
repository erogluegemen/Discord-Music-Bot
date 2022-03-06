from discord.ext import commands
import discord
import random
import pandas as pd

class messages_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

#Günün Sözü

    @commands.command(name="soz", help="Günün sözünü verir.", pass_context=True)
    async def soz(self, ctx):
        daily_messages = ["Hayatı torpilli yaşayanlardan değilim. Sadece her şeye rağmen gülmesini biliyorum.","Dümende iyisin anladık da, asfaltta gemi yürümez.","Bir insanı ancak zamanla tanırsınız. Sırtınızdan vuranı da, sözünün arkasında duranı da…","Ağzında bal olan arının bile g.tünde iğnesi var. Güvenme öyle herkese!","Sana söz veriyorum. Selektör yapıp geçtiğin bu kalbi, ilerde dörtlüleri yakıp, otostop yapıp bekleyeceksin.","Yarım kalmış bir film yoktur. O film o kadardır.","Fazla uzatmayacağım, yerime koyduklarının sana koyması dileğiyle.","Senin için savaşırdım ama verimsiz toprakları fethetmeye gerek yok!","Bana attığın kazıkları saklıyorum, döndüğünde oturacak yerin olsun diye.","Hakim dedi “Arabada kim vardı?” Ben vardım bir de içimde büyüyen kin vardı…","Kaderimizde varsa genç yaşta kefen giymek; geri vites nedir bilmez bu deli yürek.","Benim yokluğumda gülemezsin demişsin, en çok da ona güldüm ;)","Yanımda bir kişilik yer var.Ama ne yazık ki o kişilik sende yok.","Asla arkana bakma! Cindirella ayakkabısını almak için dönseydi asla prenses olmazdı..","Nefes almak için pencereyi değil de fotoğrafını açtığım an anladım sana yenildiğimi..","Hayat bana hiçbir zaman yeşil ışık yakmadı, sorun değil ben zaten hiç kırmızıda durmadım","Ölüme gidelim dedin de mazot mu yok dedik…","İleride güzel günler göreceğiz demişlerdi. Daha ne kadar gideceğiz?","Adımı avucuna yaz. Beni hatırladıkça avucunu yalarsın.","Otopsi istiyorum! Hayallerim kendi eceliyle ölmüş olamaz.","Mevzu atlı karıncalar değil. Dönen dolaplar!","Gönlünde yer yoksa güzelim, Fark etmez ben ayakta da giderim.","Kalp dediğin atıyor zaten. Marifet ritmi değiştirmekte.","Her şeyi bilmene gerek yok. Haddini bil yeter.","Ahlarla kaybettiğini keşkelerle arayacaksın…!","Azrail Blöf Yapmaz.","Dar geliyorsun artık dar… BAŞKENT olsan neye yarar.", "Şoförün hatasını Toprak örter.","Kasko yok muska var!","Biz kimseyi yarı yolda bırakmadık onlar müsait bir yerde indiler…","Güvendiğim dağlara kar yağdıranlar, hazırlanın! Kaymaya geliyorum.","Aşk tahterevalliye benzer birinin sevgisi ağır bastı mı diğerinin götü kalkar","Giden mi suçluydu hep? Suçu yok muydu itenin?","Beni bir sen anladın;sen de yanlış anladın","Göte geldi aşkımız,ikimiz de şaşkınız","Balıkesir bandırma sik anasını aldırma.","Tay sikildiği çayırı özlermiş."]

        await ctx.send(random.choice(daily_messages))

#Şiirler

    @commands.command(name="siir", help="Şiir verir.", pass_context=True)
    async def siir(self, ctx):
        poem_messages = ["Şu an yanımda olmanı isterdim. Ama değilsin. Sen ordasın; ve orası ne kadar şanslı olduğunu bilmiyor... \n-Nazım Hikmet","Türk milleti gariptir her bi lafı kaldıramaz. İbne dersin kızar da sikersin aldırmaz""Bir kendisi var her şeyi bilen\nBaşka bilen yok sanıyor\nHerkes kendini bir bok sanır\nBu herif 2 bok sanıyor","Ne ararsin Tanri ile aramda\nSen kimsin ki orucumu sorarsin?\nHakikaten gözün yoksa haramda\nBasi açiga neden türban sorarsin?\n\nRaki, sarap içiyorsam sana ne\nYoksa sana bir zarari, içerim\nIkimiz de gelsek kildan köprüye\nBen dürüstsem sarhosken de geçerim.\n\nEsir iken mümkün müdür ibadet\nYatip kalkip Atatürke dua et...\nSenin gibi dürzülerin yüzünden\nDininden de soguyacak bu millet.\n\nIsgaldeki hali sakin unutma\nAtatürke dil uzatma sebepsiz\nSen anandan yine çikardin amma\nBaban kimdi bilemezdin serefsiz.","Ben sana bok diyemem boklar duyar ar eyler\nBir zerren düşse boka onu da mundar eder\nTanrı senin hamurunu necasetle yoğurmuş\nAnan seni sıçar iken yanlışlıkla doğurmuş","Bekaretinle kapatmaya çalışsan da bedenin gizlemiyor ruhundaki fahişeyi\nZaten bacak arasından ibaret olsaymış namus\nYaradan da kapatırdı inekteki memeyi","Kalkın ey ehli vatan dediler kalktık\nPuştlar oturdu biz ayakta kaldık","Senden kaçtı, çünkü seni ne kadar çok sevdiğinin farkına vardı. Senin yanında olmaya gücü yetmedi. -Dostoyevski(Budala)","Şerefe kalkan bardaklar şeref vermez şerefsize\nUlan ayyaş dangalaklar,lazım değil şeref size!","yürü bre ehli deve endamını göreyim\nsensiz geçen gecelerin ecdadını sikeyim\nmecnun gibi top muyum bir am için öleyim?\nleyla'yı da sikeyim mecnun'u da sikeyim.\nbana yar olmayan karının izzetini itibarini sikeyim...\nyansın karıların alayı, su veren itfaiyenin hortumunu sikeyim.\n\ndüşmüşüz bir orospunun belasına,\nkoymadık diye taaa amının ortasına, kader böyle yazmış hatırasına...\nben böyle hatıranın hikayesini sikeyim!\n\nkerem dağları deler bir amcık uğruna, aslı gitsin de ona buna vurdura...\nbir karı için değer mi hiç bütün bunlara, her taraf amcık dolu mala iyi vurana.\nfuzuli am peşine düştün gurbete, am serindir am derindir şifa verir millete,\nye kebabı iç şarabı vur karpuz göte, bu gidişle yarrağımı gidersin cennete.\n-Neyzen Tevfik"]

        await ctx.send(random.choice(poem_messages))

    @commands.command(name="recommend", help="Yazdığınız filme göre film önerir", pass_context=True)
    async def recommend(self, ctx, *, get_recommend):
        df1 = pd.read_csv('u.data', sep='\t')
        df1.columns = ['user_id', 'item_id', 'rating', 'timestamp']

        df2 = pd.read_csv('Movie_Id_Titles')
        df = pd.merge(df1, df2, on='item_id')

        rating_and_no_of_rating = pd.DataFrame(df.groupby('title')['rating'].mean().sort_values(ascending=False))
        rating_and_no_of_rating['no_of_ratings'] = df.groupby('title')['rating'].count()
        rating_and_no_of_rating = rating_and_no_of_rating.sort_values('no_of_ratings', ascending=False)

        pt = df.pivot_table(index='user_id', columns='title', values='rating')

        movie_vector = pt[get_recommend].dropna()
        similar_movies = pt.corrwith(movie_vector)

        corr_df = pd.DataFrame(similar_movies, columns=['Correlation'])
        corr_df = corr_df.join(rating_and_no_of_rating['no_of_ratings'])

        corr_df = corr_df[corr_df['no_of_ratings'] > 100].sort_values('Correlation', ascending=False).dropna()

        print("{} filmine göre şu 10 filmi önerebilirim: ".format(get_recommend))
        print(corr_df.head(10))

        await ctx.send("{} filmine göre şu 10 filmi önerebilirim: ".format(get_recommend))
        await ctx.send(corr_df.head(10))

        print("Film önerildi..")
