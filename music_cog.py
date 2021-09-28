import discord
from discord.ext import commands
import ffmpeg
from youtube_dl import YoutubeDL


class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.is_playing = False
        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                               'options': '-vn'}
        self.vc = ""

    # Youtube sorgusu
    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
            except Exception:
                return False

        return {'source': info['formats'][0]['url'], 'title': info['title']}

    def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            # Parçanı URL sini alıyoruz
            m_url = self.music_queue[0][0]['source']

            # Çalan şarkıyı remove etmek
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS, executable="ffmpeg.exe"),
                         after=lambda e: self.play_next())
        else:
            self.is_playing = False


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

    @commands.command(aliases=["p"],name="play", help="Youtubeda bulduğu şarkıyı açar")
    async def p (self, ctx, *args):
        query = " ".join(args)

        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            await ctx.send("Bir ses kanalına bağlanın!")
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send("Şarkı sıraya eklendi!")

            else:
                #bunda bir bozukluk var gerek de yok pek ctx send atmaya.
                # await ctx.send("Şarkı indirilemedi. Yanlış biçim başka bir anahtar kelime deneyin. Bunun nedeni oynatma listesi veya canlı yayın biçimi olabilir.")
                self.music_queue.append([song, voice_channel])

                if self.is_playing == False:
                    await self.play_music()

    @commands.command(name="list", help="Mevcut müzik sırasını görüntüler")
    async def list(self, ctx):
        retval = ""
        for i in range(0, len(self.music_queue)):
            retval += self.music_queue[i][0]['title'] + "\n"

        print(retval)
        if retval != "":
            await ctx.send(retval)
        else:
            await ctx.send("Sırada hiç müzik yok!")

    @commands.command(name="skip", help="Çalınmakta olan şarkıyı atlar")
    async def skip(self,ctx):
        if self.vc != "" and self.vc:
            self.vc.stop()
            # varsa sıradaki oynamaya çalışsın
            await self.play_music()
