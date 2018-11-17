import database

def insertBlackmail(username, blackmail, rating, action):
    database.insertblackmail(username, blackmail, rating)

def blackmail(username, level):
    return username + " " + database.giveblackmail(username,level)

print(blackmail("karina",2))
