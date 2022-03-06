from discord.ext import commands
import discord
import asyncio

class admin_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def is_it_admin(self,ctx):
        # authors = [267952513372782602, 262510424551849985, 740360134806470740, 389443725140557826, 691628125960011837]
        # for i in authors:
        #     if author in authors:
        #         return ctx.author.id == author
        return ctx.author.id == 267952513372782602


    @commands.command(name="clear", help="belirtilen kadar mesajı siler.", pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit = amount)

    @commands.command(name="kick", help="belirtilen kişiyi serverdan kickler.", pass_context=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)

    @commands.command(name="ban", help="belirtilen kişiyi serverdan banlar.", pass_context=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banlanan şahıs: {member.mention}')

    @commands.command(name="unban", help="belirtilen kişinin serverdan banını kaldırır.", pass_context=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Banı kalkan şahıs: {user.mention}')
                return


class DurationConverter(commands.Converter):
    async def convert(self, ctx, argument):
        amount = argument[:-1]
        unit = argument[-1]
        if amount.isdigit() and unit in ['s', 'm']:
            return (int(amount), unit)
        raise commands.BadArgument(message='Geçerli olmayan bir zaman dilimi')


@commands.command()
async def tempban(ctx, member: commands.MemberConverter, duration: DurationConverter):

    multiplier = {'s':1, 'm':60}
    amount, unit = duration

    await ctx.guild.ban(member)
    await ctx.send(f'{member} kullanıcısı {amount}{unit} süre boyunca banlandı.')
    await asyncio.sleep(amount * multiplier[unit])
    await ctx.guild.unban(member)
