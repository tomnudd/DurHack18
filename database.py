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

# This works fine, but there may be some errors that could be handled better if the datatype is not one of the columns
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
    mycursor.execute(sql)

    mydb.commit()

# This works, but a feature is also needed to read the number of bad points a user has,
# things could also be handled better if a user triggers this, but their account has not been added
def addbpoint(uname,number):
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
        x=x+number
        sql = "UPDATE users SET badpoints = \"{}\" WHERE discorduname = \"{}\"".format(x,uname)
        print(sql)
        mycursor.execute(sql)
        mydb.commit()

# If the user has already been created, they should not be created again
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

    mycursor.execute("SELECT blackmail FROM blackmail WHERE discorduname= \"{}\" AND rating= \"{}\" AND used=0 ORDER BY RAND()".format(uname,rating))

    myresult = mycursor.fetchone()
    if(myresult==None):
        mycursor.execute(
            "SELECT blackmail FROM blackmail WHERE discorduname= \"{}\" AND used=0 ORDER BY RAND()".format(uname))
        if(myresult=None):
            mycursor.execute(
                "SELECT blackmail FROM blackmail WHERE discorduname= \"{}\" ORDER BY RAND()".format(uname))
            if(myresult=None):
                return 0

    for i in myresult:
        return i


    mycursor = mydb.cursor()

    sql = "UPDATE blackmail SET used = 1 WHERE address =" + myresult

    mycursor.execute(sql)

    mydb.commit()

giveblackmail("Sam","2")
