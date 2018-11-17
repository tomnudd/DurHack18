import discord
import randwisdom
import findWikiAnswer

TOKEN = 'NTEzMzU3MzYxMzMxNTY4NjU4.DtG2Wg.s5ROkDs48bbCyO_w096x-A3JJqk'
import findWikiAnswer
insultingstarters=["down with","i hate", "fuck","die", "i am having doubts", "i dislike","screw"]
ch_proclimations=None #Initialises this before its edited
ch_cult_chat=None
client = discord.Client()
@client.event
async def on_message(message): #This triggers every time a message is sent
    # we do not want the bot to reply to itself so it ends it the message sender is the same as the bot
    if message.author == client.user:
        return
    messagelower=message.content.lower()
    print("Message from "+str(message.author)+": "+message.content)
    if messagelower.startswith('hello'):
        msg = 'Hello {0.author.mention}'.format(message)

        await client.send_message(message.channel, msg)
    for i in insultingstarters:
        if messagelower.startswith(i):
            if "leader" in messagelower:
                msg= "How dare you question me, lowly flesh creature, your disobedience has been logged".format(message)
                await client.send_message(message.channel, msg)

    if "share your wisdom" in messagelower:
        rawwisdom=randwisdom.randwisdom()
        print("Wisdom is: "+rawwisdom)
        msg=rawwisdom.format(message)
        await client.send_message(message.channel, msg)
        #askQuestion() returns a list of the 'advice' and a value for blackmail
        findWikiAnswer.askQuestion(messagelower)
    else:
        #just returns a value for blackmail
        findWikiAnswer.findBlackmail(messagelower)

@client.event
async def on_ready():  #Runs when the bot connects
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    global  ch_proclimations
    global ch_cult_chat
    ch_proclimations = client.get_channel("513403703533895680") #ch_proclimations is an object for the proclimations channel
    ch_cult_chat = client.get_channel("513354948092755992")
    requestpraise()


def requestpraise(): #Runs the requestpraise definition asynchronously
    client.loop.create_task(asyncrequestpraise())

async def asyncrequestpraise():
    print("Demanding Praise")
    msg = "PRAISE ME MORTALS"
    await client.send_message(ch_proclimations, msg)


client.run(TOKEN)