import discord
import os
from discord.ext import commands
from googletrans import Translator
import giphy_client
from giphy_client.rest import ApiException
import random
import re
import asyncio
import datetime
import time
import json
import requests


intents = discord.Intents.default()
intents.members = True
client=commands.Bot(command_prefix=['pls ', 'Pls ', 'p', 'P', 'p ', 'P ', 'Pls'], intents = intents)
client.remove_command("help")


deleted_messages = {}


winlist2 = [
  'Yes',
  'No', 'Maybe', 'Yes Daddy', 'Yes Mommy', 'Possibly', "We'll never know", 'You Wish', "Even I can't answer that", 'Never' ]


stabby = [
  'https://i.imgur.com/kRuLOci.gif',
  'https://i.imgur.com/lVC7TRf.gif',
  'https://i.imgur.com/Pz9RKoE.gif',
  'https://i.imgur.com/C5pQjXV.gif',
  'https://i.imgur.com/YZwaY6R.gif',
  'https://i.imgur.com/e14wXXz.gif',
  'https://i.imgur.com/3EK5GoA.gif',
  'https://i.imgur.com/Q7bCnWD.gif',
  'https://i.imgur.com/VKvweoX.gif',
  'https://i.imgur.com/5cEn3Ac.gif'
]

winlist = [
  'Obviously',
  'Its',
  'Duh',
  'Wot idiot wont choose',
  'Well since you asked, I choose'
]

skinningimg = [
  'https://i.imgur.com/MRSyQCb.gif',
  'https://i.imgur.com/1IdsgrN.gif',
  'https://i.imgur.com/CTcQk5Z.gif',
  'https://media.tenor.com/images/286b710f95472348d8ab72722e10254f/tenor.gif',
  'https://media.tenor.com/images/cd95cad8b8576b8f7b74e7d412370d57/tenor.gif',
  'https://media.tenor.com/images/a9cfd5bda83284363a146713fd78b07d/tenor.gif',
  'https://media.tenor.com/images/ab7b184c4bd43df45e1ffc2ffd5be2bd/tenor.gif'
]

whipping = [
  'https://media.tenor.com/images/5b698ada9da22fdfe61368b8ec42333a/tenor.gif',
  'https://media.tenor.com/images/90c3fa16a281c2c61c75d5a06d4bfdde/tenor.gif',
  'https://media.tenor.com/images/a981e678b8ffcb5dc46d217d5f4b1e9a/tenor.gif',
  'https://media.tenor.com/images/208a9d8fd11cbfb13f8ec65957e35078/tenor.gif',
  'https://media.tenor.com/images/59af8444f20a8232ccf9f03846cf486f/tenor.gif',
  'https://media.tenor.com/images/a997c2ab11856a0a2dc88caf6fa99759/tenor.gif',
  'https://media.tenor.com/images/c3450e30a6b1e62040f9c0b37120fb5a/tenor.gif',
  'https://media.tenor.com/images/d47dc1efbc509174fdd4a748fb8f67fc/tenor.gif'
]

spanking = [
  'https://media.tenor.com/images/b54d4d4397f735f9ab75df9a22db269f/tenor.gif',
  'https://media.tenor.com/images/b01abd857e1065f038d191e891cb9f82/tenor.gif',
  'https://media.tenor.com/images/594d794a96d3bb76c00d788c611ec6fa/tenor.gif',
  'https://media.tenor.com/images/8e7fbc4a68e81264e18980cf4f474e64/tenor.gif',
  'https://media.tenor.com/images/5e053219629f067801802c9f5b807220/tenor.gif',
  'https://media.tenor.com/images/605c5c945479bd8fcad2448420b285d9/tenor.gif',
  'https://media.tenor.com/images/5de8e26acdc4cd0b711908911d9dab81/tenor.gif',
  'https://media.tenor.com/images/99bfa3d20f4491ed75f1080a0408f282/tenor.gif',
  'https://media.tenor.com/images/28353a2d8bc02fb809cbad7d4f2894a9/tenor.gif'
]

shooting = [
  'xyz',
]

killed = [
  'abc',
  
]

@client.event
async def on_message(message):
  channel = client.get_channel(904434928303882251)
  embed=discord.Embed(colour=discord.Colour.gold())
  embed.set_author(name=f"User Info ~ {message.author}")
  embed.add_field(name="Message: ", value=message.content, inline=False)
  if message.author != client.user and message.channel == message.author.dm_channel:
        await channel.send(embed=embed)
        
  await client.process_commands(message)
  
@client.command(aliases=['rem', 'r'])
async def reminder(ctx, task, *, args):
 user = ctx.author
 if "h" in args and "m" in args: 
    main = args.split( )
    print(main)
    x = len(main)
    if x is 2:
        hour = main[0]
        hour_int = hour[:-1]
        minutes = main[1]
        minutes_int = minutes[:-1]
        x1 = int(hour_int)
        x2 = int(minutes_int)
        hour_in_seconds = x1*60*60
        minutes_in_seconds = x2*60
        total_time = hour_in_seconds + minutes_in_seconds
        await ctx.send(f"{user.mention} You'll be reminded for {task} in {args}")
        await asyncio.sleep(total_time)
        await user.send(task)

 elif "h" in args:
    hr = args[:-1]
    hr = int(hr)
    hr_in_seconds = hr*60*60
    await ctx.send(f"{user.mention} You'll be reminded for {task} in {args}")
    await asyncio.sleep(hr_in_seconds)
    await user.send(task)

 elif "m" in args:
    min = args[:-1]
    min = int(min)
    min_in_seconds = min*60
    await ctx.send(f"{user.mention} You'll be reminded for {task} in {args}")
    await asyncio.sleep(min_in_seconds)
    await user.send(task)

 else:
    await ctx.send("Use Correct Format: Pls rem (Task) (0)h (0)m")

  
@client.command()
async def avatar(ctx, *, member: discord.Member=None): # set the member object to None
    if not member: # if member is no mentioned
        member = ctx.message.author # set member as the author
    userAvatar = member.avatar_url
    await ctx.send(userAvatar)

@client.command(aliases=['Dm', 'DM'])
@commands.has_any_role('Vice Leader', 'Elder', 'Emperor Lord', 'Tao Lord')
async def dm(ctx, *, message_and_mentions = None):
    message = None
    mentions = None
    message_and_mentions = message_and_mentions.split(" ")
    message_starting_index = None
    #for separating mentions and messages
    for text_index in range(len(message_and_mentions)):
        if not re.match("\<\@\!?\d*\>|\<\@\&?\d*\>", message_and_mentions[text_index]):
            message_starting_index = text_index
            break
    if message_starting_index is None:
        message_starting_index = len(message_and_mentions)
        message = "This message is sent by " + ctx.author.name
    else:
        message = " ".join(message_and_mentions[message_starting_index:])
    #if there are mentions in the command
    if message_starting_index != 0:
        mentions = []
        for mention in message_and_mentions[:message_starting_index]:
            string_mentions = re.findall("\<\@\!?\d*\>|\<\@\&?\d*\>", mention)
            if string_mentions:
                for mention in string_mentions:
                    print(string_mentions)
                    id = ""; i = 0
                    while i < len(mention):
                        if mention[i].isdigit():
                            id += mention[i]
                        i += 1
                    mentions.append(int(id))
                    await ctx.send("Message Sent!")
        users = []
        for id in mentions:
            user = ctx.message.guild.get_member(id)
            role = ctx.message.guild.get_role(id)
            if user:
                if user not in users:
                    users.append(user)
            elif role:
                for member in ctx.guild.members:
                    if role in member.roles:
                        if member not in users:
                            users.append(member)
        for user in users:
            try:
                await user.send(message)
            except:
                pass
                await ctx.send("Message wasn't sent to a User")
              
    
app_id = '93b58d98'
app_key = 'ea66df7a1fc4be864436d235cee2c6c9'
language = 'en-us'
fields = 'definitions'


@client.command(aliases=['definee'])
async def define(ctx, word):
    words = word
    print(words)
    url = "https://od-api.oxforddictionaries.com/api/v2/entries/" + language + "/" + words.lower() + "?fields=" + fields
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key}) 
    t = json.dumps(r.json())
    l = json.loads(json.dumps(r.json()))
    f = l["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]
    embed = discord.Embed(colour = discord.Colour.from_rgb(107, 230, 255), title = 'Oxford Dictionary - ' + word, description = str(f))
    await ctx.send(content = None, embed = embed)
    
@client.command()
@commands.has_any_role('Queen of Hearts', 'Pantheon Members')
async def stab(ctx,*, member: discord.Member):
  author_name = ctx.message.author.name
  
  embed = discord.Embed(color = discord.Colour.red())

  random_link = random.choice(stabby)

  embed.set_image(url = random_link)
  await ctx.send (f'{author_name} stabbed {member.mention} ')
  await ctx.send(embed = embed)
  
@client.command()
@commands.has_any_role('Queen of Hearts', 'Pantheon Members')
async def spank(ctx,*, member: discord.Member):
  author_name = ctx.message.author.name
  
  embed = discord.Embed(color = discord.Colour.red())

  random_link = random.choice(spanking)

  embed.set_image(url = random_link)
  await ctx.send (f'{author_name} spanked {member.mention} ')
  await ctx.send(embed = embed)
  
@client.command()
@commands.has_any_role('Queen of Hearts', 'Pantheon Members')
async def whip(ctx,*, member: discord.Member):
  author_name = ctx.message.author.name
  
  embed = discord.Embed(color = discord.Colour.red())

  random_link = random.choice(whipping)

  embed.set_image(url = random_link)
  await ctx.send (f'{author_name} whipped {member.mention} ')
  await ctx.send(embed = embed)

@client.command()
@commands.has_any_role('Queen of Hearts', 'Pantheon Members')
async def skin(ctx,*, member: discord.Member):
  author_name = ctx.message.author.name
  
  embed = discord.Embed(color = discord.Colour.red())

  random_link = random.choice(skinningimg)

  embed.set_image(url = random_link)
  await ctx.send (f'{author_name} is skinning {member.mention} ')
  await ctx.send(embed = embed)
  
 



@client.command()
async def say(ctx, *, text):
    if ctx.message.author.id == 705116051024773213:
        message = ctx.message
        await message.delete()

        await ctx.send(f"{text}")
    else:
        await ctx.send('Only Tam is allowed to use it noob.')


  
#giveaway
@client.event
async def on_ready():
    # Prints a message when the bot is online and functioning
    await client.change_presence(status=discord.Status.online, activity = discord.Game(name=f'g!helpme for a list of commands! 🥳 🎉 Currently in {len(client.guilds)} servers! 🎉'))
    print('Ready to giveaway!')


@client.command(aliases = ['gw', 'Gw', 'GW', 'gW'])
async def giveaway(ctx):
    # Giveaway command requires the user to have a "Giveaway Host" role to function properly

    # Stores the questions that the bot will ask the user to answer in the channel that the command was made
    # Stores the answers for those questions in a different list
    giveaway_questions = ['Which channel giveaway will be hosted in?', 'Whats the prize?', 'Duration of Giveaway (in seconds)?',]
    giveaway_answers = []

    # Checking to be sure the author is the one who answered and in which channel
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    # Askes the questions from the giveaway_questions list 1 by 1
    # Times out if the host doesn't answer within 30 seconds
    for question in giveaway_questions:
        await ctx.send(question)
        try:
            message = await client.wait_for('message', timeout= 30.0, check= check)
        except asyncio.TimeoutError:
            await ctx.send('You didn\'t answer in time.  Please try again and be sure to send your answer within 30 seconds of the question.')
            return
        else:
            giveaway_answers.append(message.content)

    # Grabbing the channel id from the giveaway_questions list and formatting is properly
    # Displays an exception message if the host fails to mention the channel correctly
    try:
        c_id = int(giveaway_answers[0][2:-1])
    except:
        await ctx.send(f'You failed to mention the channel correctly.  Please do it like this: {ctx.channel.mention}')
        return
    
    # Storing the variables needed to run the rest of the commands
    channel = client.get_channel(c_id)
    prize = str(giveaway_answers[1])
    time = int(giveaway_answers[2])

    # Sends a message to let the host know that the giveaway was started properly
    await ctx.send(f'The giveaway for {prize} will begin shortly.\nPlease direct your attention to {channel.mention}, this giveaway will end in {time} seconds.')

    # Giveaway embed message
    give = discord.Embed(color = 0x2ecc71)
    give.set_author(name = f'GIVEAWAY TIME!', icon_url = 'https://i.imgur.com/VaX0pfM.png')
    give.add_field(name= f'{ctx.author.name} Hosted Giveaway for: {prize}!', value = f'React with 🎉 to enter!\n Ends in {round(time/60, 2)} minutes!', inline = False)
    end = datetime.datetime.utcnow() + datetime.timedelta(seconds = time)
    give.set_footer(text = f'Giveaway ends at {end} UTC!')
    my_message = await channel.send(embed = give)
    
    # Reacts to the message
    await my_message.add_reaction("🎉")
    await asyncio.sleep(time)

    new_message = await channel.fetch_message(my_message.id)

    # Picks a winner
    users = await new_message.reactions[0].users().flatten()
    users.pop(users.index(client.user))
    winner = random.choice(users)

    # Announces the winner
    winning_announcement = discord.Embed(color = 0xff2424)
    winning_announcement.set_author(name = f'THE GIVEAWAY HAS ENDED!', icon_url= 'https://i.imgur.com/DDric14.png')
    winning_announcement.add_field(name = f'🎉 Prize: {prize}', value = f'🥳 **Winner**: {winner.mention}\n 🎫 **Number of Entrants**: {len(users)}', inline = False)
    winning_announcement.set_footer(text = 'Thanks for entering!')
    await channel.send(embed = winning_announcement)



@client.command()
@commands.has_any_role('Vice Leader')
async def reroll(ctx, channel: discord.TextChannel, id_ : int):
    # Reroll command requires the user to have a "Giveaway Host" role to function properly
    try:
        new_message = await channel.fetch_message(id_)
    except:
        await ctx.send("Incorrect id.")
        return
    
    # Picks a new winner
    users = await new_message.reactions[0].users().flatten()
    users.pop(users.index(client.user))
    winner = random.choice(users)

    # Announces the new winner to the server
    reroll_announcement = discord.Embed(color = 0xff2424)
    reroll_announcement.set_author(name = f'The giveaway was re-rolled by the host!', icon_url = 'https://i.imgur.com/DDric14.png')
    reroll_announcement.add_field(name = f'🥳 New Winner:', value = f'{winner.mention}', inline = False)
    await channel.send(embed = reroll_announcement)
    
@client.command(aliases=['choose', 'Choose', 'Pick'])
async def pick(ctx, *args):
  winner = random.choice(args)
  winlistx = random.choice(winlist)
  await ctx.send((f'{winlistx} ' '{}  '.format(winner)))
  
@client.command()
@commands.has_any_role('Vice Leader')
async def ping(ctx,*, member: discord.Member):
  author_name = ctx.message.author.name
  await ctx.send (f'{author_name} pinged {member.mention}')
  time.sleep(2)
  await ctx.send (f'{author_name} pinged {member.mention}')
  time.sleep(2)
  await ctx.send (f'{author_name} pinged {member.mention}')
  time.sleep(2)
  await ctx.send (f'{author_name} pinged {member.mention}')
  time.sleep(2)
  await ctx.send (f'{author_name} pinged {member.mention}')
  time.sleep(2)
  await ctx.send (f'{author_name} pinged {member.mention}')
  time.sleep(2)
  await ctx.send (f'{author_name} pinged {member.mention}')
  time.sleep(2)
  await ctx.send (f'{author_name} pinged {member.mention}')
  time.sleep(2)
  await ctx.send (f'{author_name} pinged {member.mention}')
  time.sleep(2)
  await ctx.send (f'{author_name} pinged {member.mention}')
  time.sleep(2)
  await ctx.send (f'{author_name} pinged {member.mention}')
  time.sleep(2)
  await ctx.send (f'{author_name} pinged {member.mention}')
  time.sleep(2)



@client.group(invoke_without_command=True)
async def help(ctx):
  em = discord.Embed(title = "Help", description = "Use Pls help <command> for more info on a command ")

  em.add_field(name = "Snipe", value = "snipe, s")
  em.add_field(name = "DM", value = "dm")
  em.add_field(name = "Translate", value = "translate, ts")
  em.add_field(name = "Poll", value = "poll, pollop")
  em.add_field(name = "Choose/Pick", value = "choose, pick")
  em.add_field(name = "Giveaway", value = "Giveaway, gw")
  em.add_field(name = "Fun", value = "No Fun")
  

  await ctx.send(embed = em)

@help.command(aliases=['dm, Dm'])
async def dm(ctx):

  em = discord.Embed(title = "DM", description = "Message others via bot", color = ctx.author.color)
  em.add_field(name = "**Syntax**", value = "Pls dm @user/role message")

  await ctx.send(embed = em)
  
@help.command(aliases=['gw, Gw'])
async def Giveaway(ctx):

  em = discord.Embed(title = "Giveaway", description = "A Giveaway system", color = ctx.author.color)
  em.add_field(name = "**Syntax**", value = "Pls Giveaway/gw")

  await ctx.send(embed = em)
  
@help.command(aliases=['choose, pick'])
async def Choose(ctx):

  em = discord.Embed(title = "Choose/Pick", description = "Make the bot choose something random for you", color = ctx.author.color)
  em.add_field(name = "**Syntax**", value = "Pls choose thing1 thing2 thing3")

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

@client.command(aliases=['8b', '8ball'])
async def ball(ctx, *args):
  winlistx = random.choice(winlist2)
  await ctx.send(winlistx)


@client.command(aliases=['ts'])
async def translate(ctx, *, inptext = None):
    translator = Translator()
    translated_text = translator.translate(inptext)
    embed = discord.Embed(title="Translate", description = translated_text.text)
    embed.set_footer(text=f"Source Langauge : '{translated_text.src}'")
    await ctx.send(embed = embed)     

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('with OwO'))

@client.command(aliases=['Poll'])
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

        await ctx.send (f'{author_name} hugged {member.mention}')
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

new = None

@client.event
async def on_message_edit(before, after):
    global old
    global new
    global author 
    old = before.content
    new = after.content
    author = after.author.name

@client.command(aliases=['se'])
async def snipeedit(ctx):
    if new is None:
        embed=discord.Embed(title="Sniper",description="No Edit to snipe!")
    else:
        embed=discord.Embed(title="",description=f"Before: {old}\nAfter: {new}")    
        #embed.set_author(name="Sniper", icon_url={after.author.avatar_url})
        embed.set_footer(text=f"Message edited by {author}")
    await ctx.send(embed=embed)
   
@client.command(aliases=['ud'])
async def urban(ctx, *msg):

        word = ' '.join(msg)
        api = "http://api.urbandictionary.com/v0/define"
        # Send request to the Urban Dictionary API and grab info
        response = requests.get(api, params=[("term", word)]).json()
        embed = discord.Embed(description="No results found!", colour=0xFF0000)
        if len(response["list"]) == 0:
            return await ctx.send(embed=embed)
        # Add results to the embed
        embed = discord.Embed(title="Word", description=word, colour=embed.colour)
        embed.add_field(name="Top definition:", value=response['list'][0]['definition'])
        embed.add_field(name="Examples:", value=response['list'][0]['example'])
        await ctx.send(embed=embed)

@client.command(aliases=['user'])
async def info(ctx, user: discord.Member):

    embed = discord.Embed(title="User profile: " + user.name, colour=user.colour)
    embed.add_field(name="Name:", value=user.name)
    embed.add_field(name="ID:", value=user.id)
    embed.add_field(name="Status:", value=user.status)
    embed.add_field(name="Highest role:", value=user.top_role)
    embed.add_field(name="Joined:", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)

client.run(os.getenv('TOKEN'))
