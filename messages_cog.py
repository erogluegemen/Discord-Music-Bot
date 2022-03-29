from discord.ext import commands
import discord
import random
import pandas as pd

class messages_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# Günün Sözü

    @commands.command(name="soz", help="Günün sözünü verir.", pass_context=True)
    async def soz(self, ctx):
        daily_messages = [""]

        await ctx.send(random.choice(daily_messages))

# Şiirler

    @commands.command(name="siir", help="Şiir verir.", pass_context=True)
    async def siir(self, ctx):
        poem_messages = [""]

        await ctx.send(random.choice(poem_messages))
# Film Öner
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

    # Hatırlatıcı
    @commands.command(name="hatirlat", help="hatırlatır.", pass_context=True)
    async def hatirlat(self, ctx, time: int, *, msg):
        await s(time * 60)  # (saniye * 60)
        for i in range(5):
            await (ctx.send("{}, {} !!!".format(msg, ctx.author.mention)))
            i += 1
