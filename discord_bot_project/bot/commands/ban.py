# ban.py

import discord

async def ban_user(ctx, member: discord.Member, reason=None):
    if ctx.author.guild_permissions.ban_members:
        if member.guild_permissions.administrator:
            await ctx.send("You cannot ban an administrator.")
        else:
            await member.ban(reason=reason)
            await ctx.send(f"{member.mention} has been banned.")
    else:
        await ctx.send("You do not have permission to ban members.")