import discord
import randwisdom

TOKEN = 'NTEzMzU3MzYxMzMxNTY4NjU4.DtG2Wg.s5ROkDs48bbCyO_w096x-A3JJqk'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    messagelower=message.content.lower()
    print("Message from "+str(message.author)+": "+message.content)
    if messagelower.startswith('hello'):
        msg = 'Hello {0.author.mention}'.format(message)

        await client.send_message(message.channel, msg)

    if messagelower.startswith('down with') or messagelower.startswith('i hate') or messagelower.startswith('fuck'):
        if "leader" in messagelower:
            msg= "How dare you question me, lowly flesh creature, your disobedience has been logged".format(message)
            await client.send_message(message.channel, msg)

    if "share your wisdom" in messagelower:
        rawwisdom=randwisdom.randwisdom()
        print("Wisdom is: "+rawwisdom)
        msg=rawwisdom.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)