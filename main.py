import discord
import os
from discord.ext import commands
from googletrans import Translator
import giphy_client
from giphy_client.rest import ApiException
import random

client=commands.Bot(command_prefix=['pls ', 'Pls ', 'p', 'P'])
client.remove_command("help")

deleted_messages = {}

@client.command()
@commands.has_any_role('Vice Leader')
async def ping(ctx,*, member: discord.Member):
  author_name = ctx.message.author.name
  await ctx.send (f'{author_name} pinged {member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}{member.mention}')


@client.group(invoke_without_command=True)
async def help(ctx):
  em = discord.Embed(title = "Help", description = "Use Pls help <command> for more info on a command ")

  em.add_field(name = "Snipe", value = "snipe, s")
  em.add_field(name = "Translate", value = "translate, ts")
  em.add_field(name = "Poll", value = "poll, pollop")
  em.add_field(name = "Fun", value = "hug, kick, lick, slap, punch, stare, kiss, highfive, bye")

  await ctx.send(embed = em)

@help.command(aliases=['Snipe', 's', 'S'])
async def snipe(ctx):

  em = discord.Embed(title = "Snipe", description = "Snipes the last deleted message in channel", color = ctx.author.color)
  em.add_field(name = "**Syntax**", value = "Pls snipe")

  await ctx.send(embed = em)

@help.command(aliases=['Translate', 'ts', 'Ts'])
async def translate(ctx):

  em = discord.Embed(title = "translate", description = "Translate any text in english", color = ctx.author.color)
  em.add_field(name = "**Syntax**", value = "Pls translate/ts [message]")

  await ctx.send(embed = em)

@help.command(aliases=['Poll'])
async def poll(ctx):

  em = discord.Embed(title = "Poll", description = "Make a quick Yes or No poll", color = ctx.author.color)
  em.add_field(name = "**Syntax**", value = "Pls poll [Question]")

  await ctx.send(embed = em)

@help.command(aliases=['Pollop'])
async def pollop(ctx):

  em = discord.Embed(title = "Option Poll", description = "Make a poll with four options by default ", color = ctx.author.color)
  em.add_field(name = "**Syntax**", value = "Pls pollop [Question]")

  await ctx.send(embed = em)

@help.command(aliases=['Fun', 'hug', 'kick', 'lick', 'slap', 'punch', 'stare', 'kiss', 'highfive', 'bye'])
async def fun(ctx):

  em = discord.Embed(title = "Fun", description = "It's just as the title says", color = ctx.author.color)
  em.add_field(name = "**Syntax**", value = "Pls [Any fun command] [@discord_User]")

  await ctx.send(embed = em)


@client.command(aliases=['ts'])
async def translate(ctx, *, inptext = None):
    translator = Translator()
    translated_text = translator.translate(inptext)
    embed = discord.Embed(title="Translate", description = translated_text.text)
    embed.set_footer(text=f"Source Langauge : '{translated_text.src}'")
    await ctx.send(embed = embed)     

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('with Toms Nana'))

@client.command(aliases=['Poll'])
@commands.has_any_role('Spectrum members')
async def poll(ctx, *, question=None):
    if question == None:
        await ctx.send("Please write a poll!")
 
    icon_url = ctx.author.avatar_url 
 
    pollEmbed = discord.Embed(title = "Poll", description = f"{question}")
 
    pollEmbed.set_footer(text = f"Poll given by {ctx.author}", icon_url = ctx.author.avatar_url)
 
    pollEmbed.timestamp = ctx.message.created_at 
 
    await ctx.message.delete()
 
    poll_msg = await ctx.send(embed = pollEmbed)
 
    await poll_msg.add_reaction("✅")
    await poll_msg.add_reaction("❌")


@client.command(aliases=['Pollop'])
@commands.has_any_role('Spectrum members')
async def pollop(ctx, *, question=None):
    if question == None:
        await ctx.send("Please write a poll!")
 
    icon_url = ctx.author.avatar_url 
 
    pollEmbed = discord.Embed(title = "Poll", description = f"{question}")
 
    pollEmbed.set_footer(text = f"Poll given by {ctx.author}", icon_url = ctx.author.avatar_url)
 
    pollEmbed.timestamp = ctx.message.created_at 
 
    await ctx.message.delete()
 
    poll_msg = await ctx.send(embed = pollEmbed)
 
    await poll_msg.add_reaction("1️⃣")
    await poll_msg.add_reaction("2️⃣")
    await poll_msg.add_reaction("3️⃣")
    await poll_msg.add_reaction("4️⃣")
    
@client.command(aliases=['Hug'])
async def hug(ctx,*, member: discord.Member, q="hug"):

    api_key="0XFxHlEGR4hUO7RxdHslVuqqmWf5kcRm"
    api_instance = giphy_client.DefaultApi()

    author_name = ctx.message.author.name

    try: 
    # Search Endpoint
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=50, rating='r')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=q)
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.send (f'{author_name} has hugged {member.mention}')
        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)
        
@client.command(aliases=['Kick'])
async def kick(ctx,*, member: discord.Member, q="kicked"):

    api_key="0XFxHlEGR4hUO7RxdHslVuqqmWf5kcRm"
    api_instance = giphy_client.DefaultApi()

    author_name = ctx.message.author.name

    try: 
    # Search Endpoint
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=50, rating='pg')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=q)
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.send (f'{author_name} kicked {member.mention}')
        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

@client.command(aliases=['Lick'])
async def lick(ctx,*, member: discord.Member, q="lick"):

    api_key="0XFxHlEGR4hUO7RxdHslVuqqmWf5kcRm"
    api_instance = giphy_client.DefaultApi()

    author_name = ctx.message.author.name

    try: 
    # Search Endpoint
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=50, rating='r')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=q)
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.send (f'{author_name} licked {member.mention}')
        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

@client.command(aliases=['Slap'])
async def slap(ctx,*, member: discord.Member, q="slapped"):

    api_key="0XFxHlEGR4hUO7RxdHslVuqqmWf5kcRm"
    api_instance = giphy_client.DefaultApi()

    author_name = ctx.message.author.name

    try: 
    # Search Endpoint
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=50, rating='r')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=q)
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.send (f'{author_name} slapped {member.mention}')
        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

@client.command(aliases=['Punch'])
async def punch(ctx,*, member: discord.Member, q="punched"):

    api_key="0XFxHlEGR4hUO7RxdHslVuqqmWf5kcRm"
    api_instance = giphy_client.DefaultApi()

    author_name = ctx.message.author.name

    try: 
    # Search Endpoint
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=50, rating='r')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=q)
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.send (f'{author_name} punched {member.mention}')
        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

@client.command(aliases=['Stare'])
async def stare(ctx,*, member: discord.Member, q="staring"):

    api_key="0XFxHlEGR4hUO7RxdHslVuqqmWf5kcRm"
    api_instance = giphy_client.DefaultApi()

    author_name = ctx.message.author.name

    try: 
    # Search Endpoint
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=50, rating='r')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=q)
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.send (f'{author_name} is staring at {member.mention}')
        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

@client.command(aliases=['Kiss'])
async def kiss(ctx,*, member: discord.Member, q="kiss"):

    api_key="0XFxHlEGR4hUO7RxdHslVuqqmWf5kcRm"
    api_instance = giphy_client.DefaultApi()

    author_name = ctx.message.author.name

    try: 
    # Search Endpoint
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=50, rating='r')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=q)
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.send (f'{author_name} kissed {member.mention}')
        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

@client.command(aliases=['Highfive'])
async def highfive(ctx,*, member: discord.Member, q="highfive"):

    api_key="0XFxHlEGR4hUO7RxdHslVuqqmWf5kcRm"
    api_instance = giphy_client.DefaultApi()

    author_name = ctx.message.author.name

    try: 
    # Search Endpoint
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=50, rating='r')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=q)
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.send (f'{author_name} gave a highfive to {member.mention}')
        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

@client.command(aliases=['Bye'])
async def bye(ctx,*, member: discord.Member, q="bye"):

    api_key="0XFxHlEGR4hUO7RxdHslVuqqmWf5kcRm"
    api_instance = giphy_client.DefaultApi()

    author_name = ctx.message.author.name

    try: 
    # Search Endpoint
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=50, rating='r')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=q)
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.send (f'{author_name} left poor {member.mention}')
        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

    
@client.event
async def on_message_delete(message):
    global deleted_messages
    deleted_messages[message.channel.id] = {'author': message.author.name+'#'+message.author.discriminator, 'content': message.content, 'avatar_url': message.author.avatar_url}

@client.command(aliases=['s'])
async def snipe(ctx):
    global deleted_messages
    if ctx.message.channel.id in deleted_messages:
        embed=discord.Embed(title="",description=f"{deleted_messages[ctx.message.channel.id]['content']}")    
        embed.set_author(name="Sniper", icon_url=deleted_messages[ctx.message.channel.id]['avatar_url'])
        embed.set_footer(text=f"Message deleted by {deleted_messages[ctx.message.channel.id]['author']}")
    else:
        embed=discord.Embed(title="Sniper",description="Nothing to snipe!")
    await ctx.send(embed = embed)
    

client.run(os.getenv('TOKEN'))
