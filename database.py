import mysql.connector
def insertblackmail(uname,blackmails,ratings):
    mydb = mysql.connector.connect(
      host="cult.cv27lm8h5axy.eu-west-1.rds.amazonaws.com",
      user="samrobbins",
      passwd="durhackcult",
      database="testDB"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO blackmail (discorduname, blackmail, rating) VALUES (%s, %s, %s)"
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
    sql = "UPDATE users SET {} = \"{}\" WHERE discorduname = \"{}\"".format(datatype, data, uname)
    print(sql)
    #val = (datatype,data,uname)
    #mycursor.execute(sql, val)
    mycursor.execute(sql)

    mydb.commit()

def addbpoint(uname):
    mydb = mysql.connector.connect(
        host="cult.cv27lm8h5axy.eu-west-1.rds.amazonaws.com",
        user="samrobbins",
        passwd="durhackcult",
        database="testDB"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT badpoints FROM users WHERE discorduname= \"{}\"".format(uname))
    myresult=mycursor.fetchone()
    for x in myresult:
        x+=1
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

    mycursor.execute("SELECT blackmail FROM blackmail WHERE discorduname= \"{}\" AND rating= \"{}\"".format(uname,rating))

    myresult = mycursor.fetchone()
    for i in myresult:
        return i


    mycursor = mydb.cursor()

    sql = "UPDATE blackmail SET used = 1 WHERE address =" + myresult

    mycursor.execute(sql)

    mydb.commit()






print(giveblackmail("Karina",1))