import discord  # uses Pycord
import wikipedia
from discord import Option

bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"We've logged in as {bot.user}.")


testing = [969767375048175686]  # list of guild ids


@bot.slash_command(guild_ids=testing, name='summary', description='Returns a Wikipedia summary')
async def summary(ctx, search: Option(str, description="What do you want to get a summary for?", required=True)):
    await ctx.channel.trigger_typing()  # shows that the bot is typing
    try:  # tries to get a summary
        thesummary = wikipedia.summary(search,
                                       chars=1950)  # limits the summary to a maximum of 1950 characters, discord's
        # limit is 2,000 per message
        try:
            await ctx.respond(thesummary)  # responds to the slash command (bot must respond within 3 seconds)
        except:
            await ctx.send(thesummary)  # sends as a regular message, if it cannot send as a slash command
    except:
        searchsummary = str(wikipedia.search(search, suggestion=True)).replace('(', '').replace(')', '').replace("'",
                                                                                                                 "").replace(
            '[', '').replace(']',
                             '')  # usually returns a list, so we turn it into a string, suggestion = true includes suggestions
        try:
            await ctx.respond(f"I can't seem to find a summary for that.. Did you mean: {searchsummary}")
        except:
            await ctx.send(f"I can't seem to find a summary for that.. Did you mean: {searchsummary}")


@bot.slash_command(guild_ids=testing, name='search', description="Search Wikipedia")
async def search(ctx, search: Option(str, description="What do you want to search for?", required=True)):
    await ctx.channel.trigger_typing()  # shows that the bot is typing
    searchsearch = str(wikipedia.search(search, suggestion=True)).replace('(', '').replace(')', '').replace("'",
                                                                                                            "").replace(
        '[', '').replace(']',
                         '')  # usually returns a list, so we turn it into a string, suggestion = true includes suggestions
    try:
        await ctx.respond(searchsearch)
    except:
        await ctx.send(searchsearch)


@bot.slash_command(guild_ids=testing, name="url", description="Get a URL to a page on Wikipedia")
async def url(ctx, search: Option(str, description="What do you want to get a URL for?", required=True)):
    await ctx.channel.trigger_typing()
    try:  # tries to get a summary to see if we can get a link
        urlsummary = wikipedia.summary(search, auto_suggest=False)  # i think auto suggest is on by default
        search = search.lower().replace(' ', '_').replace('  ', '_')
        try:
            await ctx.respond(f'https://en.wikipedia.org/wiki/{search}')
        except:
            await ctx.send(f'https://en.wikipedia.org/wiki/{search}')
    except:
        urlsearch = str(wikipedia.search(search, suggestion=True)).replace('(', '').replace(')', '').replace("'",
                                                                                                             "").replace(
            '[', '').replace(']', '')
        try:
            await ctx.respond(f"I can't find what you're talking about, did you mean: {urlsearch}")
        except:
            await ctx.send(f"I can't find what you're talking about, did you mean: {urlsearch}")


@bot.slash_command(guild_ids=testing, name="random", description="Returns a random Wikipedia article")
async def random(ctx):
    await ctx.channel.trigger_typing()
    randomtitle = wikipedia.random()  # returns a title
    randomsummary = wikipedia.summary(randomtitle, chars=1950)
    link = randomtitle.replace(' ', '_')
    try:
        await ctx.respond(f"**{randomtitle}** \n\n{randomsummary}\n\nhttps://en.wikipedia.org/wiki/{link}")
    except:
        await ctx.send(f"**{randomtitle}** \n\n{randomsummary}\n\nhttps://en.wikipedia.org/wiki/{link}")


bot.run('MTA1MTE4ODYzODI3MDEwNzc4OA.GCTwHL.ez117Q1mwcaM9DfKhtFAzTfLJMaE2wvBkcP02c')
