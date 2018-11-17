import discord
import randwisdom
import findWikiAnswer

TOKEN = 'NTEzMzU3MzYxMzMxNTY4NjU4.DtG2Wg.s5ROkDs48bbCyO_w096x-A3JJqk'
import findWikiAnswer
insultingstarters=["down with","i hate", "fuck","die", "i am having doubts", "i dislike","screw"]
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
        if messagelower.startswith(insultingstarters[i]):
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

def requestpraise():
    msg = "PRAISE ME MORTALS".format(message)
    client.send_message(message.channel, msg)


client.run(TOKEN)
