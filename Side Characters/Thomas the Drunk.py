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

occupied = False

@client.event #DAB
async def on_ready(): #Activates when the bot goes online 
        print("Bot Online")
        print("Name: {}".format(client.user.name))
        print("ID: {}".format(client.user.id))
        client.remove_command("help")
        await client.change_presence(game=discord.Game(name=' with coins', type=1))

@client.event
async def on_message(message): #Triggerss whenever a message is sent
    if message.channel.id == '467670236020342787': #Checks the message is in the right channel
                if client.user.mentioned_in(message): #Checks if the bot got mentions
                    global occupied #Import occupied with a global (eww)
                    await client.change_presence(game=discord.Game(name=' with coins', type=1))
                    with open("D:/Python/MMO BOTS/Data/Member Data/"+str(message.author.id)+".txt",'r') as read_file: #Opens up the JSON file
                        jsonFile = json.load(read_file)

                    if "Incomplete" in jsonFile['stats']['quests']["A Guessing Game."]["progress"]: #Makes sure the quest is incomplete
                    

                        def is_number(x): #Just a def to make sure the value is actually a number
                            try:
                                float(x)
                                return True
                            except ValueError:
                                return False


                        
                        if occupied == False: #Makes sure the bot is not talking to someone else
                            occupied = True #Checks occupied
                            deleteMessageList = [] #Creates the deleted messages list
                            deleteMessageList.append(message) #Appends the original message to the deleted messages list
                            msg = await client.send_message(message.channel, "...Wait.. What?..\n\nWho the hell are you? On second thought, I don't care, I want to have some fun.\n\nHeres an idea! I am going to pick a number between 1 and 10! Get it right, I give you 20 gems! Get it wrong though, and you give me 5 gems! Sound good?\n\nYou don't have any gems? Eh, lets play anyway. When your this bored am I right.\n\nWhenever your ready just send me a number.") #Sends a message and makes it a variable to reference later
                            deleteMessageList.append(msg) #Appends the message to the deleted messages list
                            maximumNumber = 10 #Sets the variable for the max number to be randomized
                            runThroughs = 0 #Sets the amount of times the user has run through the program
                            pickedNumber = randint(0,maximumNumber) #Picks a number between 0 and the max number
                            
                            while runThroughs < 3: #Repeats until the user has gone through more than 3 times
                                await client.change_presence(game=discord.Game(name=str(pickedNumber), type=1)) #Changes bot status to the number it picked
                                response = await client.wait_for_message(timeout=60,author=message.author) #Waits for a response from the user and labels their response as a variable
                                
                                if response == None: #Checks if the user did not respond
                                    print('The player left')
                                    await client.delete_messages(deleteMessageList) #Deletes all the messages in the list
                                    msg = await client.send_message(message.channel, "Are we even playing {}? God. Come back later so we can have this whole conversation again.".format(message.author.mention)) #Mentions the user in a message and sets the message to a variable
                                    occupied = False #Changes the bot to be un-occupied
                                    deleteMessageList.append(msg) #Appends the message to the deleted messages list
                                    runThroughs = 5
                                elif is_number(response.content):#Makes sure the response is a number
                                    if int(response.content) == pickedNumber: #Checks if the user got it right
                                        
                                        jsonFile["stats"]["currentCoins"] += 20 #Give the player 20 coins
                                        runThroughs += 1 #Applies the runThroughs
                                        maximumNumber *= 10 #Multiplys the maximum number by 10
                                        pickedNumber = randint(0,maximumNumber) #Re-picks the number
                                        if runThroughs < 3: #Checks to see if that was the last run through
                                            msg = await client.send_message(message.channel, choice(['Wow! You are a natural at this, lets make it a bit harder. How about a number between 0 and {}'.format(str(maximumNumber)), 'Oh my, that was fast. How about a number between 0 and {}'.format(str(maximumNumber)), 'Oi <@467533860263952384>, is this person cheating!? What ever, how about a number between 0 and {}'.format(str(maximumNumber))])) #Sends a message and sets it to a variable
                                            deleteMessageList.append(msg) #Appends message to the delete messages list
                                    else: #If the user did not send the right number
                                        msg = await client.send_message(message.channel, choice(['Guess again buddy.', 'Not even close.', 'Wow! That was almost the worst number you could pick!', 'Maybe you should look for some clues ***wink***'])) #Sends a message and makes it a variable
                                        deleteMessageList.append(msg) #Appends that variable to a list
                                
                                else: #If the user did not send the a number
                                    msg = await client.send_message(message.channel, 'I need a number, not a word.') #Sends a message and makes it a variable
                                    deleteMessageList.append(msg) #Appends the message to the deleted messages list

                                deleteMessageList.append(response) #Appends the users response to the deleted messages list
                            await client.delete_messages(deleteMessageList) #Deletes all the messages in the list
                            msg = await client.send_message(message.channel, 'Wow. I did not expect that...\n\nGuess Ill go home now, you just stole all my drinking money. \n\n*Thomas staggers towards the door, but flops onto a table and falls asleep before he ever makes it there.*\n\n\n\n ***You have earnt 60 xp and 60 gems***') #Sends a message and sets it to a variable
                            await client.change_presence(game=discord.Game(name=' with coins', type=1))
                             #Changes presence to nothing
                            jsonFile['stats']['xp'] += 60 #Adds 60 xp to the player
                            jsonFile['stats']['quests']["A Guessing Game."]["progress"] = 'Complete' #Changes the quest to complete

                            await client.send_message(client.get_channel('467676045752008716'), '<@468216147423002636>, {} just beat me at the guessing game, wanna give him the talk?'.format(message.author.mention)) #Sends a message through a hidden channel to tell another bot to do something.
                            occupied = False #Sets occupied to false
                            with open("D:/Python/MMO BOTS/Data/Member Data/"+str(message.author.id)+".txt", 'w') as outfile: #Opens the JSON file in write mode
                                json.dump(jsonFile, outfile) #Writes the changed data to the JSON file

                            await asyncio.sleep(20) #Pauses code for 20 seconds
                            await client.delete_message(msg) #Deletes the previous message sent
                        else: #If the bot is already occupied
                            await client.send_message(message.channel, '{} can you shut up. I am having a conversation here.'.format(message.author.mention)) #Sends a message
                    else: #If you have already completed the quest
                        await client.send_message(message.channel, '*Thomas sleeps on the table quietly... too quietly...*') #Sends a message
                
                        

                                
client.run('') #Dab
