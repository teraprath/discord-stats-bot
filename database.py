import mysql.connector
import config

mydb = mysql.connector.connect(
    host = config.host,
    user = config.user,
    password = config.password,
    database = config.database
)

cursor = mydb.cursor()

def init():
    sql = "SHOW TABLES LIKE 'user'"
    cursor.execute(sql)
    res = cursor.fetchone()
    if res:
        print("Table 'user' found.")
        return
    else:
        cursor.execute("CREATE TABLE user (id INT AUTO_INCREMENT PRIMARY KEY, userid VARCHAR(255), username VARCHAR(255), discriminator VARCHAR(255), level INT, exp INT, nexp INT, rank INT, avatar VARCHAR(255))")
        print("Table 'user' created.")
        return

def registerUser(userid, username, discriminator, avatar):
    sql = "INSERT INTO user (userid, username, discriminator, level, exp, nexp, avatar) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    nexp = int(((50*(1**2))+(50*1)))
    val = (str(userid), str(username), str(discriminator), 1, 0, nexp, str(avatar))
    cursor.execute(sql, val)
    mydb.commit()
    print(f"{userid} ({username}#{discriminator}) registered in database.")

def getUserData(userid, column):
    cursor.execute(f"SELECT {column} FROM user WHERE userid = '{userid}'")
    result = cursor.fetchone()[0]
    return result

def updateUser(userid, column, value):
    sql = f"UPDATE user SET {column} = {value} WHERE userid = '{userid}'"
    cursor.execute(sql)
    mydb.commit()

def checkUser(userid):
    cursor.execute(f"SELECT * FROM user WHERE userid = '{userid}'")
    result = cursor.fetchone()
    if result is None:
        return False
    else:
        return True

def updateRanking():
    sql = "SELECT userid FROM user ORDER BY level DESC"
    cursor.execute(sql)
    list = cursor.fetchall()
    rank = 0
    for user in list:
        rank += 1
        updateUser(user[0], "rank", rank)

def getRanking():
    sql = "SELECT userid FROM user ORDER BY level DESC LIMIT 10"
    cursor.execute(sql)
    list = cursor.fetchall()
    return list