import time
import discord
from discord.ext import commands
import ffmpeg
from youtube_dl import YoutubeDL
from lyricsgenius import Genius


class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.is_playing = False
        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                               'options': '-vn'}
        self.vc = ""

#Get Song

    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
            except Exception:
                return False

        return {'source': info['formats'][0]['url'], 'title': info['title']}

#Skip Function

    def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']
            self.music_queue.pop(0)
            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS, executable="ffmpeg.exe"),
                         after=lambda e: self.play_next())

        else:
            self.is_playing = False

#Play Function

    async def play_music(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']

            if self.vc == "" or not self.vc.is_connected() or self.vc == None:
                self.vc = await self.music_queue[0][1].connect()

            else:
                await self.vc.move_to(self.music_queue[0][1])

            print(self.music_queue)
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS, executable="ffmpeg.exe"),
                         after=lambda e: self.play_next())

        else:
            self.is_playing = False

#Play Command

    @commands.command(aliases=["p"],name="play", help="Youtubeda bulduğu şarkıyı açar")
    async def p (self, ctx, *args):
        query = " ".join(args)

        voice_channel = ctx.author.voice.channel
        #await voice_channel.connect()

        if voice_channel is None:
            await ctx.send("Bir ses kanalına bağlanın!")
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send("Sıkıntılar yaşadım. Bir daha denesene bi")

            else:
                self.music_queue.append([song, voice_channel])
                await ctx.send("{} sıraya eklendi!".format(song['title']))
                if self.is_playing == False:
                    await self.play_music()

#Pause Command
    @commands.command(name="pause", help="Mevcut çalan şarkıyı durdurur.")
    async def pause(self, ctx):
        voice = discord.utils.get(self.vc, guild=ctx.guild)
        if voice.is_connected():
            await voice.pause()
            await ctx.send("Şarkı durduruldu.")

        else:
            await ctx.send("Şu anda oynatılan bir şarkı yok")

#Resume Command
    @commands.command(name="resume", help="Durdurulan şarkıyı devam ettirir.")
    async def resume(self,ctx):
        voice = discord.utils.get(self.vc, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
            await ctx.send("Şarkı devam ediyor.")

        else:
            await ctx.send("Durdurulanan bir şarkı yok.")


#List Command

    @commands.command(aliases=["l"],name="list", help="Mevcut müzik sırasını görüntüler")
    async def l(self, ctx):
        retval = ""
        for i in range(0, len(self.music_queue)):
            retval += self.music_queue[i][0]['title'] + "\n"

        print(retval)
        if retval != "":
            await ctx.send(retval)
        else:
            await ctx.send("Sırada hiç müzik yok!")
    # *****************************************************
    async def list(self, ctx):
        retval = ""
        for i in range(0, len(self.music_queue)):
            retval += self.music_queue[i][0]['title'] + "\n"

        print(retval)
        if retval != "":
            await ctx.send(retval)
        else:
            await ctx.send("Sırada hiç müzik yok!")

#Skip Command

    @commands.command(aliases=["s"], name="skip", help= "Müziği geçer")
    async def s(self, ctx):
        if self.vc != "" and self.vc:
            try:
                self.vc.stop()
                await ctx.play_music()
            except:
                pass
    # *****************************************************
    async def skip(self, ctx):
        if self.vc != "" and self.vc:
            try:
                self.vc.stop()
                await ctx.play_music()
            except:
                pass

#Show Lyrics Command

    @commands.command(name="lyrics", help="Şarkı sözlerini gösterir", pass_context=True)
    async def lyrics(self, ctx,*, artist_song):
        genius_key = 'z0QcIpr0qEMVX9TrGhTB3zemYr9lxa3QyUvcY06UkFt0TmqWzYyvXIld1azo04C1'
        genius = Genius(genius_key)
        artist1, song1 = artist_song.split("-")
        print("Şarkıcı: {}\nŞarkı: {}".format(artist1,song1)) #terminalde görmem için test amaçlı
        song = genius.search_song(song1, artist1)
        lyrics_first_part = song.lyrics[0:len(song.lyrics) // 2]
        lyrics_second_part = song.lyrics[len(song.lyrics) // 2 if len(song.lyrics) % 2 == 0 else ((len(song.lyrics) // 2) + 1):]
        emb = discord.Embed(title="{} - {}".format(artist1,song1),color=0xa3a3ff)
        emb.add_field(name="Field 2 Title", value=f"{lyrics_first_part}", inline=True)
        emb.add_field(name="Field 3 Title", value=f"{lyrics_second_part}", inline=True)
        await ctx.send(embed=emb)
        #description=f"{song.lyrics}"

