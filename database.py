import mysql.connector
# This works well
def insertblackmail(uname,blackmails,ratings):
    mydb = mysql.connector.connect(
      host="cult.cv27lm8h5axy.eu-west-1.rds.amazonaws.com",
      user="samrobbins",
      passwd="durhackcult",
      database="testDB"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO blackmail (discorduname, blackmail, rating, used) VALUES (%s, %s, %s, 0)"
    val = (uname, blackmails, ratings)
    mycursor.execute(sql, val)

    mydb.commit()

def insertusrinfo(datatype,data,uname):
    mydb = mysql.connector.connect(
        host="cult.cv27lm8h5axy.eu-west-1.rds.amazonaws.com",
        user="samrobbins",
        passwd="durhackcult",
        database="testDB"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT discorduname FROM users WHERE discorduname= \"{}\"".format(uname))
    myresult = mycursor.fetchone()
    if (myresult == None):
        adduser(uname)
        return 0

    mycursor.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'users' AND TABLE_SCHEMA = 'testDB'")
    myresult = mycursor.fetchall()
    for x in myresult:
        list=[]
        list.append(x)
    if datatype not in list:
        return


    mycursor.execute("SELECT discorduname FROM users WHERE discorduname= \"{}\"".format(uname))
    myresult = mycursor.fetchone()
    if (myresult == None):
        adduser(uname)


    sql = "UPDATE users SET {} = \"{}\" WHERE discorduname = \"{}\"".format(datatype, data, uname)
    print(sql)
    mycursor.execute(sql)

    mydb.commit()

def addbpoint(uname,number):
    mydb = mysql.connector.connect(
        host="cult.cv27lm8h5axy.eu-west-1.rds.amazonaws.com",
        user="samrobbins",
        passwd="durhackcult",
        database="testDB"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT discorduname FROM users WHERE discorduname= \"{}\"".format(uname))
    myresult = mycursor.fetchone()
    if (myresult == None):
        adduser(uname)
        return 0

    mycursor.execute("SELECT badpoints FROM users WHERE discorduname= \"{}\"".format(uname))
    myresult=mycursor.fetchone()
    for x in myresult:
        x=x+number
        sql = "UPDATE users SET badpoints = \"{}\" WHERE discorduname = \"{}\"".format(x,uname)
        print(sql)
        mycursor.execute(sql)
        mydb.commit()

def adduser(uname):
    mydb = mysql.connector.connect(
        host="cult.cv27lm8h5axy.eu-west-1.rds.amazonaws.com",
        user="samrobbins",
        passwd="durhackcult",
        database="testDB"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT discorduname FROM users WHERE discorduname= \"{}\"".format(uname))
    myresult = mycursor.fetchone()
    if (myresult != None):
        return

    sql = "INSERT INTO users (discorduname,badpoints) VALUES (\"{}\",0)".format(uname)
    mycursor.execute(sql)

    mydb.commit()


def giveblackmail(uname,rating):
    mydb = mysql.connector.connect(
        host="cult.cv27lm8h5axy.eu-west-1.rds.amazonaws.com",
        user="samrobbins",
        passwd="durhackcult",
        database="testDB"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT discorduname FROM users WHERE discorduname= \"{}\"".format(uname))
    myresult=mycursor.fetchone()
    if(myresult==None):
        adduser(uname)



    mycursor.execute("SELECT blackmail FROM blackmail WHERE discorduname= \"{}\" AND rating= \"{}\" AND used=0 ORDER BY RAND()".format(uname,rating))

    myresult = mycursor.fetchone()
    if(myresult==None):
        mycursor.execute(
            "SELECT blackmail FROM blackmail WHERE discorduname= \"{}\" AND used=0 ORDER BY RAND()".format(uname))
        myresult = mycursor.fetchone()

        if(myresult==None):
            mycursor.execute(
                "SELECT blackmail FROM blackmail WHERE discorduname= \"{}\" ORDER BY RAND()".format(uname))
            myresult = mycursor.fetchone()
            if(myresult==None):
                return 0


    for i in myresult:
        return i


    mycursor = mydb.cursor()

    sql = "UPDATE blackmail SET used = 1 WHERE address =" + myresult

    mycursor.execute(sql)

    mydb.commit()


def badpointcount(user):
    mydb = mysql.connector.connect(
        host="cult.cv27lm8h5axy.eu-west-1.rds.amazonaws.com",
        user="samrobbins",
        passwd="durhackcult",
        database="testDB"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT discorduname FROM users WHERE discorduname= \"{}\"".format(uname))
    myresult = mycursor.fetchone()
    if (myresult == None):
        adduser(uname)
        return 0
    mycursor.execute("SELECT badpoints FROM users WHERE discorduname= \"{}\"".format(uname))
    myresult = mycursor.fetchone()
    return myresult







giveblackmail("Sam","2")
