import discord #Required for Discord API
from discord.ext.commands import Bot #Required for Discord API
from discord.ext import commands #Required for Discord API
from discord.ext import commands #Required for Discord API
import asyncio #Required for Discord API
import simplejson as json #Required for accessing JSON documents


import datetime #Required for accessing time


from pathlib import Path #Required for checking files

bot_prefix = "!" #Sets bot prefix
client = commands.Bot(command_prefix=bot_prefix) #DAB


@client.event #DAB
async def on_ready(): #Activates when the bot goes online 
    print("Bot Online")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))

@client.event
async def on_message(message):

    if message.content.startswith('!help '):
        
        with open("D:/Python/MMO BOTS/Data/Member Data/"+str(message.author.id)+".txt",'r') as read_file: #Opens up the JSON file
                        jsonFile = json.load(read_file)

        if "The wild wild east." in jsonFile['stats']['quests']:
            if not "Complete" in jsonFile['stats']['quests']["The wild wild east."]["progress"]: #Makes sure the quest is incomplete
                if not 'Gather 5 bits of wheat and bring them back to Kalderon' in jsonFile['stats']['quests']["The wild wild east."]["taskDescript"]:
                    await client.send_message(message.channel, "Who the hell are you? :incoming_envelope: ")
                    await client.send_message(message.author, "Hey buddy.\n\nI am the weapon forger around these parts. I supply weapons for the Grondle Garrison, the rebels, and even adventurues like yourself on occation.\n\nKadin sent you did he? Shit, you have got a tough time ahead of you if you are talking to someone with balls that big.\n\nHeres what I'll do for yah. I will give you an absolutely garbage sword, in return you need to go and get **5 bits of wheat** for me. If you head E you will find them in the grondle-farmland. Come back to me ones you have them.")

                    jsonFile['stats']['quests']["The wild wild east."]["progress"] = 0
                    jsonFile['stats']['quests']["The wild wild east."]["taskDescript"] = 'Gather 5 bits of wheat and bring them back to Kalderon'

                    with open("D:/Python/MMO BOTS/Data/Member Data/"+str(message.author.id)+".txt", 'w') as outfile: #Opens the JSON file in write mode
                        json.dump(jsonFile, outfile) #Writes the changed data to the JSON file
                else:
                    await client.send_message(message.channel, 'What? I thought I told you to go get 5 bits of wheat from <#467499738959314954>.')
            else:
                await client.send_message(message.channel, "Work it out yourself.")
        else:
            await client.send_message(message.channel, "{}, leave me alone.".format(message.author.mention))




client.run('')
