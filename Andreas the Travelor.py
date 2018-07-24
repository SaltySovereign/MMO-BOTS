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

        await client.process_commands(message) #Processes commands before interacting with message
        if message.channel.id == '467676045752008716': #Checks if the message came from the hidden channel
                if client.user.mentioned_in(message): #Checks if the bot was mentioned in the chat
                        if message.author.id == '467533860263952384': #Checks who the message was from
                                await client.send_message(message.channel, choice(['Can do boss!', 'Absolutely.', 'Anything for you man!'])) #Sends a message
                                mentionsList = list(message.mentions) #Puts all mentions from the message recieved into a list, these are generators

                                mentionsList.remove(client.user) #Removes itself from the list, this leaves only the user that was attached with the message

                                await client.send_message(mentionsList[0], "Hey man, looks like you're new around here.\n\nI'm Andreas, I help people get from A to B the fastest.\nArtemis tells me you have stumbled your way into Grondle without a clue of where you actually are, I am here to help you with that.\nGrondle is the capital north of the **Golden Trade Route.**\nIn the city itself it is a pleasent place, peaceful, very little violence. There is even a pub that you can communicate through no matter where you are in Grondle. Outside the city, well... that would ruin the fun.\n\nI am sure Artemis gave you a quest or pointer of some kind? No? Err.. ***There should be someone in the Grondle Tavern***, ***Thomas*** I think. ***Ping him if you want something to do***. \n\n\nAnyway, if you need help moving just do !help and then follow it with my name, should look something like '!help "+str(client.user.mention+"', infact this works with everyone else as well.")) #Sends a message to the attached user


        if message.content.startswith('!help '): #Checks whether the message started with '!help '
                if client.user.mentioned_in(message): #Checks if the user is asking help from this bot
                        await client.send_message(message.channel, "Whats the probs, bobs? :incoming_envelope: ") #Sends a short message to the channel that the question originated
                        await client.send_message(message.author, 'Look buddy, I am not a complex man/beast thing. I can do few but alot at the same time. You know what I mean?\n\nFor one, I am good at moving people, and not in a sus way (except for that one time). Typing \n```!move [DIRECTION]```\nwill move you in that direction. Directions can be N (North), S (South), E (East), or W (West). Movement commands should look something like this, ```!move N```\n\nI also know my history, for example if you type \n```!wai```\nI can ramble on about where you are (wai stands for **w**here **a**m **i**)\n\n\nThat is basically all I do. As you can see, I am not a lot.') #Sends some information to the author

@client.command(pass_context=True) #DAB
async def move(ctx, direction): #Creates a move command and passes the context as well as a direction

        with open("D:/Python/MMO BOTS/Data/Member Data/"+str(ctx.message.author.id)+".txt",'r') as read_file: #Opens up the JSON file
                jsonFile = json.load(read_file) #Sets the JSON file as a python dictation

        tile = jsonFile["stats"]["tile"].split(',') #Opens the tile data in the JSON strcuture and splits the two number into a list.
        xtile = int(tile[0]) #Sets the xtile to the first number
        ytile = int(tile[1]) #Sets the ytile to the second number
        stamina = jsonFile["stats"]["stamina"] #Collects the stamina user data from the JSON dict

        async def finishMove(): #Creates a short hand
                
                jsonFile["stats"]["stamina"] = stamina - 10 #Reduces the users stamina by ten

                with open('D:/Python/MMO BOTS/Data/Game Data/tileToRole.txt', 'r') as role_file: #Reads what role corrolates with what position

                        for line in role_file: #Runs for each line in the file
                                print(line)
                                if str(xtile)+','+str(ytile) in line: #Checks if the line has the position in it
                                        valuesInLine = line.split(',') #Splits the line into a list via ','
                                        roleIdInValues = valuesInLine[2] #Grabs the role id following the location
                                        roleIdInValues = roleIdInValues[:-1] #Removes line break character from the end of the line (Got me stuck for half an hour)
                                        roleId = discord.utils.get(ctx.message.server.roles, name=roleIdInValues) #Prints what the role id is
                                        
                                        await client.add_roles(ctx.message.author,roleId) #Adds new location channels
                                        

                                if str(tile[0])+','+str(tile[1]) in line: #Checks if the line has the position in it
                                        valuesInLine = line.split(',') #Splits the line into a list via ','
                                        roleIdInValues = valuesInLine[2] #Grabs the role id following the location
                                        roleIdInValues = roleIdInValues[:-1] #Removes line break character from the end of the line (Got me stuck for half an hour)
                                        roleId = discord.utils.get(ctx.message.server.roles, name=roleIdInValues) #Prints what the role id is
                                       
                                        await client.remove_roles(ctx.message.author,roleId) #Removes access to old location channels
                                        

               
                        

                


        if stamina >= 10:
                if direction.lower() == 'n': #Checks if the user selected North
                        if not ytile == 0: #Makes sure the user cannot walk off the map
                        
                                ytile -= 1 #Moves the user
                                
                                await finishMove()
                                
                        else:
                                await client.say('{}, you are at the edge of the world. You are unable to go `NORTH`.'.format(ctx.message.author.mention)) #If the member cannot move, send them a message

                if direction.lower() == 's': #Checks if the user selected South
                        if not ytile == 9: #Makes sure the user cannot walk off the map

                                ytile += 1 #Moves the user
                                
                                await finishMove()
                        else:
                                await client.say('{}, you are at the edge of the world. You are unable to go `SOUTH`.'.format(ctx.message.author.mention)) #If the member cannot move, send them a message
                
                if direction.lower() == 'e': #Checks if the user selected East
                        if not xtile == 9: #Makes sure the user cannot walk off the map

                                xtile += 1 #Moves the user
                                
                                await finishMove()
                        else:
                                await client.say('{}, you are at the edge of the world. You are unable to go `EAST`.'.format(ctx.message.author.mention)) #If the member cannot move, send them a message

                if direction.lower() == 'w': #Checks if the user selected West
                        if not xtile == 0: #Makes sure the user cannot walk off the map

                                xtile -= 1 #Moves the user
                                
                                await finishMove()
                        else:
                                await client.say('{}, you are at the edge of the world. You are unable to go `WEST`.'.format(ctx.message.author.mention)) #If the member cannot move, send them a message


        print(str(xtile)+','+str(ytile)) #Prints the changed tile location
        jsonFile["stats"]["tile"] = str(xtile)+','+str(ytile) #Sets the new tile location

        with open("D:/Python/MMO BOTS/Data/Member Data/"+str(ctx.message.author.id)+".txt", 'w') as outfile: #Opens the JSON file in write mode
            json.dump(jsonFile, outfile) #Writes the changed data to the JSON file



client.run("") #DAB

