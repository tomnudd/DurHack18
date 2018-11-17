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
    sql = "UPDATE users SET %s = %s WHERE discorduname = %s"
    val = (datatype,data,uname)
    mycursor.execute(sql, val)

    mydb.commit()

def addbpoint(uname):
    mydb = mysql.connector.connect(
        host="cult.cv27lm8h5axy.eu-west-1.rds.amazonaws.com",
        user="samrobbins",
        passwd="durhackcult",
        database="testDB"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT badpoints FROM users WHERE discorduname="+ str(uname))

    x= mycursor.fetchone()
    x+=1
    sql = "UPDATE users SET badpoints = %s WHERE discorduname = %s"
    val=(x,uname)
    mycursor.execute(sql,val)
    mydb.commit()

def adduser(uname):
    mydb = mysql.connector.connect(
        host="cult.cv27lm8h5axy.eu-west-1.rds.amazonaws.com",
        user="samrobbins",
        passwd="durhackcult",
        database="testDB"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO users (discorduname) VALUES (%s)"
    val = (uname)
    mycursor.execute(sql, val)

    mydb.commit()

def giveblackmail(uname,rating):
    mydb = mysql.connector.connect(
        host="cult.cv27lm8h5axy.eu-west-1.rds.amazonaws.com",
        user="samrobbins",
        passwd="durhackcult",
        database="testDB"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM blackmail WHERE discorduname="+str(uname)+" AND rating="+int(rating)+" AND used=null")

    myresult = mycursor.fetchone()

    return(myresult)

    mycursor = mydb.cursor()

    sql = "UPDATE blackmail SET used = 1 WHERE address =" + myresult

    mycursor.execute(sql)

    mydb.commit()






insertblackmail("karina", "Is actually a russian spy", "2")