import discord
import os
from discord.ext import commands
from googletrans import Translator
import giphy_client
from giphy_client.rest import ApiException
import random

client=commands.Bot(command_prefix=['pls ', 'Pls ', 'p', 'P'])

deleted_messages = {}

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

@client.command()
@commands.has_any_role('Vice Leader')
async def poll(ctx, *, question=None):
    if question == None:
        await ctx.send("Please write a poll!")
 
    icon_url = ctx.author.avatar_url 
 
    pollEmbed = discord.Embed(title = "Poll", description = f"{question}")
 
    pollEmbed.set_footer(text = f"Poll given by {ctx.author}", icon_url = ctx.author.avatar_url)
 
    pollEmbed.timestamp = ctx.message.created_at 
 
    await ctx.message.delete()
 
    poll_msg = await ctx.send(embed = pollEmbed)
 
    await poll_msg.add_reaction("❌")
    await poll_msg.add_reaction("⭕")


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
    
@client.command()
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

client.run(os.getenv('TOKEN'))
