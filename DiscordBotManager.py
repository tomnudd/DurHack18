import discord
import randwisdom
import scientologyWisdom
import findWikiAnswer
import random
import database
import blackmail
import datetime

TOKEN = 'NTEzMzU3MzYxMzMxNTY4NjU4.DtG2Wg.s5ROkDs48bbCyO_w096x-A3JJqk'

insultingstarters=["down with","i hate", "fuck","die", "i am having doubts", "i dislike","screw"]
ch_proclimations=None #Initialises this before its edited
ch_cult_chat=None

lastpraiserequest=None
memberlistpraise={}

client = discord.Client()
@client.event
async def on_message(message): #This triggers every time a message is sent
    global memberlistpraise
    if message.author.name not in memberlistpraise:
        memberlistpraise[message.author.name]=False
    # we do not want the bot to reply to itself so it ends it the message sender is the same as the bot

    print("Message from "+str(message.author)+" on "+str(message.channel)+": "+message.content)

    if message.author == client.user:
        return

    if database.badpointcount(str(message.author))>5 and database.giveblackmail(str(message.author),3)==0:
        client.loop.create_task(requestsecret(message.author))
    print(str(message.timestamp))
    isBlackmail = 0
    messagelower=message.content.lower()

    if "praise glorious leader" in messagelower:
        await client.send_message(message.channel, "Your praise has been noted, follower")
        await checkpraiseresponse(message.author)

    if messagelower.startswith('hello'):
        msg = 'Hello {0.author.mention}'.format(message)

        await client.send_message(message.channel, msg)
    for i in insultingstarters:
        if messagelower.startswith(i):
            if "leader" in messagelower:
                msg= "How dare you question me, lowly flesh creature, your disobedience has been logged"
                await client.send_message(message.channel, msg)
                database.addbpoint(str(message.author),3) # Adds 3 bad points for being rude
                await client.send_message(client.get_channel("513372966533464064"), str(message.author) + " has defied the cult.")
                await client.send_message(client.get_channel("513372966533464064"), str(blackmail.blackmail(str(message.author),3)))

    if messagelower== "get hyped":
        msg="https://lh3.googleusercontent.com/E1OLQGly6YhImTSZ5HOqUpPq3szjq8hVrsPvG77wEfvMyKyzQWdY3FIw_UA9C2VS-DTcaKb2qQIE6FRTVZesQuiKe0nkERKfc-TXgZPJp9-QsAdlyoeppDYtWnzOM4RJeROKlPWSptpL6nreeJJpvDginh7goDLyumDBPVklTTuhy_7zMGqwjTTiq5z_UvUinHZTYLchjngEOXmTOdbJdCSgKTiRhStWQyLAZKgLazKtKlj3OAAkKffQaw99rOzHDcH3HrwmzH0A_DHLXZcZVrepibldDKQtiVUGf7qtcg2IFyOW1KGeDrJGXlokvSevokoYPY7Vkwx636bakd0SFJ6PPGNmoKCtBrL9sJVlVd_0-f_FCiJm3Uk2Xa1ljDZLYnI2cddhNxgnqxRwawXt-oPCoclI8yJNlpzckfOYMI7YL74mMFu8pfks5J4f9d9WRtJxkaucWUYwCVZ4t6rGcvw4psDkwhbhTfxlbQy8gyhT1eMSlqiy3brjtL9-qHTlLb_1vAYlOx7BNrj58thNJQu8BUiIEez1EYLSXIMI86mSKmUx2nq18Z_DrMfh3wMsDOGUhOZnd4tH-_HJvypTB2AEmkTKBQryBx_51XCCDNAuDJUGJ_kzbaEZar43eMB64G7mQEJBKp6GA6TBuC2qAavusn08zfR_udqXi2fGnkapbhdPjrhVbwTG_CcSnbWidhNV6obTvhyx4_XzPA=w470-h592-no"
        await client.send_message(message.channel, msg)
    if (messagelower.startswith("<@513357361331568658> should") and not "or" in messagelower) or (messagelower.startswith("<@513357361331568658> is")) or (messagelower.startswith("<@513357361331568658> am")) or (messagelower.startswith("<@513357361331568658> does"))or (messagelower.startswith("<@513357361331568658> would")) or (messagelower.startswith("<@513357361331568658> could"))or (messagelower.startswith("<@513357361331568658> are")) or (messagelower.startswith("<@513357361331568658> can")):

        randnum=random.randint(0,2)
        if randnum==1:
            await client.send_message(message.channel, "No")
        else:
            await client.send_message(message.channel, "Yes")
    elif "why" in messagelower:
        await client.send_message(message.channel, "Do not concern yourself with useless 'why's. Concern yourself only with me, your leader.")



    elif "share your wisdom" in messagelower:
        rawwisdom=randwisdom.randwisdom()
        print("Wisdom is: "+rawwisdom)
        msg=rawwisdom.format(message)
        await client.send_message(message.channel, msg)
    elif "share your scientology" in messagelower or "give a proclamation" in messagelower:
        rawwisdom=scientologyWisdom.wisdom()
        print("Proclamation is: "+rawwisdom)
        msg=rawwisdom.format(message)
        await client.send_message(message.channel, msg)
    else:
        if ("?" in messagelower) and ( "<@513357361331568658>" in messagelower):
            print("Question detected")
            messagelower = messagelower.replace("<@513357361331568658>", "")
            #askQuestion() returns a list of the 'advice' and a value for blackmail
            answer = findWikiAnswer.askQuestion(messagelower)
            isBlackmail = answer[1]
            for msg in answer[0]:
                print("The message contents is")
                print(str(msg))
                print("The length of this message is: "+str(len(str(msg))))
                if len(msg)>1000: #if message is too long, splits into several messages
                    msgcount=int(len(msg)/1000)
                    for i in range(0,msgcount):
                        await client.send_message(message.channel, msg[i*1000:(i+1)*1000])
                await client.send_message(message.channel, str(msg))
                print("The blackmail value of this search is: "+str(answer[1]))
        else:
            isBlackmail = findWikiAnswer.findBlackmail(messagelower)

    if isBlackmail >= 1:
        #need another function to input the blackmail into the database
        print("Blackmail is 1")
        blackmail.insertBlackmail(str(message.author),"You asked the question: "+message.content,answer[1],"Wiki search")


@client.event
async def on_ready():  #Runs when the bot connects
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    global ch_proclimations
    global ch_cult_chat
    ch_proclimations=client.get_channel("513403703533895680")
    ch_cult_chat=client.get_channel("513354948092755992")
  #  print("Post-ready Praise Request")
  #  requestpraise()
    requestpraise() #Set time until you run requestpraise, 10800 for 3 hours
    client.wait_until_ready()
    CassUser=await client.get_user_info("99611176119312384")

    print(str(CassUser))
    #client.loop.cre
    # ate_task(requestsecret(CassUser))
    #for i in range(0,4):


def requestpraise():
    global memberlistpraise
    for userkey in memberlistpraise:
        if not memberlistpraise[userkey]:
            database.addbpoint(userkey,3)
        memberlistpraise[userkey]=False


    print("Waiting till ready to request praise")
    client.wait_until_ready()
    print("Requesting Praise")
    msg = "PRAISE ME MORTALS"
    client.loop.create_task(client.send_message(ch_proclimations, msg))
    client.loop.call_later(10800, requestpraise) #Set time until repeat
    global lastpraiserequest
    lastpraiserequest = datetime.datetime.now()


async def requestsecret(user):
    print("Requesting secret from "+user.display_name)
    await client.start_private_message(user)
    await client.send_message(user,"Tell me a secret dear follower")
    validresponse = False
    while not validresponse:
        reply= await client.wait_for_message(author=user)
        if reply.channel.is_private:
            await client.send_message(user, "Your obedience is noted")
            blackmail.insertBlackmail(str(user),reply.content,3,"Sent as secret")
            validresponse=True


def punishheretic(user):
    client.loop.create_task(client.send_message(513372966533464064, str(user) + "has defied the cult."))
    #print out some juicy gossip


async def checkpraiseresponse(user):
    print("DEBUG PRINT")
    global lastpraiserequest
    global memberlistpraise
    now=datetime.datetime.now()
    if lastpraiserequest is None:
        print("No request for praise yet made")
        return None

    timediff = now-lastpraiserequest
    if (timediff.seconds/3600)<2:
        memberlistpraise[user.name]=True
        if (timediff.seconds / 3600) > 1:
            await client.send_message(user, "Your praise was late, be more prompt in future")
            database.addbpoint(user.name,1)




print("Starting bot")
client.run(TOKEN)

