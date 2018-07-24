#####################################################################
#### If something has DAB next to it, it means 'Discord API Bit' ####
#####################################################################

import discord #Required for Discord API
from discord.ext.commands import Bot #Required for Discord API
from discord.ext import commands #Required for Discord API
from discord.ext import commands #Required for Discord API
import asyncio #Required for Discord API
import simplejson as json #Required for accessing JSON documents
from random import choice
from random import randint

import datetime #Required for accessing time


from pathlib import Path #Required for checking files

bot_prefix = "!" #Sets bot prefix
client = commands.Bot(command_prefix=bot_prefix) #DAB



@client.event #DAB
async def on_ready(): #Activates when the bot goes online 
        print("Bot Online")
        print("Name: {}".format(client.user.name))
        print("ID: {}".format(client.user.id))
        client.remove_command("help")

@client.event
async def on_message(message):
    await client.process_commands(message) #Processes commands
    if message.channel.id == '467676045752008716': #Checks if the message came from the hidden channel
        if client.user.mentioned_in(message): #Checks if the bot was mentioned
            if message.author.id == '467961194175791114': #Checks who the message came from
                mentionsList = list(message.mentions) #Comprises the mentions into a list
                
                mentionsList.remove(client.user) #Removes himself from the list, leaving only the user in question
                
                await client.send_message(message.channel, 'You make that sound very nasty.') #Sends a message to the hidden channel
                

                with open("D:/Python/MMO BOTS/Data/Member Data/"+str(mentionsList[0].id)+".txt",'r') as read_file: #Opens up the JSON file
                    jsonFile = json.load(read_file)
                
                jsonFile["stats"]["quests"]["The wild wild east."] = {"taskDescript": "Head East and talk to the weapons smith.", "progress": "Incomplete"} #Adds a new quest to the users data
                await client.send_message(mentionsList[0], "Looks like you just completed your first quest. Very good.\n\nAs a reward you would have been given some xp and gems, these will help you throughout your adventure.\n\nThe gems, of course, you can purchase items with. The xp is much more interesting.\n\nXp will allow you to gain more perk points. This means you become faster, stronger, have more endurence that sort of thing.\n\nTo find your other quests, simple type '!quests' in any channel of which I reside.\n\nI just added a new quest for you to do as well. If you head east you will find a man there who is able to give you some weapons. \nYou might want to ask for some help from <@467685141805006858> on how to get there, that's his kind of thing.\n\nWell that's my spiel. You may continue on your way.") #Sends a message to the user

                with open("D:/Python/MMO BOTS/Data/Member Data/"+str(mentionsList[0].id)+".txt", 'w') as outfile: #Opens the JSON file in write mode
                    json.dump(jsonFile, outfile) #Writes the changed data to the JSON file

    if message.content.startswith('!help '): #Checks if the message started with '!help '
                if client.user.mentioned_in(message): #Checks if the bot is needed for help
                    await client.send_message(message.channel, 'Figure it out yourself.') #Sends a helpful message

@client.command(pass_context=True)
async def quests(ctx):
    with open("D:/Python/MMO BOTS/Data/Member Data/"+str(ctx.message.author.id)+".txt",'r') as read_file: #Opens up the JSON file
        jsonFile = json.load(read_file)

    embed = discord.Embed(title='Active Quests', description="All {}'s active quests".format(ctx.message.author.mention), color=0x7ce2ff) #DAB #But basically it makes a fancy message with the title and description

    for value in jsonFile["stats"]["quests"]: #For each of the quests the user has 
        if jsonFile["stats"]["quests"][value]["progress"] != 'Complete': #If the quest in question is Incomplete
            embed.add_field(name=value,value=jsonFile["stats"]["quests"][value]['taskDescript'], inline=True) #Add to the fancy message with somefancy name and description

    await client.say(embed=embed) #Sends the fancy message



client.run('') #DAB
