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
    if message.channel.id == '467519829755166720':
        if not message.author.id == client.user.id: #Check to make sure the bot is not hearing itself
            await client.process_commands(message) #Processes commands
            await client.delete_message(message) #Deletes the message that was sent, prevents users from spamming the-gate channel

@client.command(pass_context=True)
async def joinmessage(ctx): #Creates command joinmessage
        if ctx.message.author.server_permissions.administrator: #Checks if the author is an admin
            await client.say('*You stand in a large hallway, a great door stands before you. A giant stands to its left.*\n\n\n***Welcome Travelor!*** \n\nYou are now entering the province of Cinderfall. This land is littered with what filth is left of the human race.\n\nAfter the water supply ran out, total chaos spread across the land.\n\nBurgarlarry, Muggings, Murder, the new norm.\n\nWithout end in site, the rich fortifide themselves behind a great wall the covered the western end of the **Golden Thread Trade Route.**\n\nThe rich, the poor, the violent. They all gather here to sell their merchandise. \nYour story will begin in the city of ***Grondle***, home of the rich.\nWhat you do from there is up to you.\n\n\n\n\n*Type !enter to open the door.*')



@client.command(pass_context=True)
async def enter(ctx):
        my_file = Path("./Data/Member Data/"+str(ctx.message.author.id)+".txt") #Sets user file path as a variable
        if not my_file.is_file(): #Checks to make sure the user does not have a file

                today = datetime.date.today() #Gets the current date
                timeYearAgo = str(datetime.datetime.strftime(datetime.date(today.year-1,today.month,today.day),'%x'))
                f = open("D:/Python/MMO BOTS/Data/Member Data/"+str(ctx.message.author.id)+".txt",'w') #Opens the users file
                f.write('{"stats": {"health": 100, "maxHealth": 100, "inventory": "", "lastCheckIn": "'+timeYearAgo+'", "quests": {"A Guessing Game.":{"taskDescript": "Speak to Thomas in the Grondle Tavern.", "progress": "Incomplete"}}, "tile": "0,0", "role": "Township", "level": 0, "xp": 0, "upgradePoints": 0, "currentCoins": 15, "damage": 2, "stamina": 15, "speed": 2}}') #Inserts all user default data
                f.close() #Closes user file
        
        else: #If the file does exist... 

                print('Member '+ctx.message.author.name+' has returned!') #Prints 'Member [THEIR NAME] has returned

        roleId = discord.utils.get(ctx.message.server.roles, name='Player') #Prints what the role id is
        await client.add_roles(ctx.message.author,roleId) #Adds new location channels
        roleId = discord.utils.get(ctx.message.server.roles, name='grondle-city-center') #Prints what the role id is
        await client.add_roles(ctx.message.author,roleId) #Adds new location channels
        await client.send_message(client.get_channel('467676045752008716'), '<@467685141805006858> Hey man can you send '+str(ctx.message.author.mention)+' some backstory for grondle-city-center?')



client.run('')
