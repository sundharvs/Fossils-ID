import sqlite3
usersdb = sqlite3.connect('data/users.db')
sessionsdb = sqlite3.connect('data/sessions.db')

def usersinit():
    cursor = usersdb.execute("CREATE TABLE Users (UserID TEXT, Fossil TEXT, Score INTEGER)")

def sessionsdb():
    cursor = sessions.execute("CREATE TABLE Sessions (SessionID TEXT, Fossil TEXT, Score INTEGER)")

def readplaintext(userid):
    try:
        cursor = usersdb.execute("SELECT * FROM Users WHERE UserID = ?", (userid,))
        for row in cursor:
            return row[1]
    except sqlite3.OperationalError:
        usersinit()
        readplaintext(userid)

def writefossil(userid,fossil):
    try:
        cursor = usersdb.execute("SELECT * FROM Users WHERE UserID = ?", (userid,))
        if(cursor.fetchone != None):
            usersdb.execute("UPDATE Users SET Fossil = ? WHERE UserID = ?", (fossil, userid))
        if(cursor.fetchone() == None):
            usersdb.execute("INSERT INTO Users (UserID,Fossil,Score) VALUES (?, ?, ?);", (userid, fossil, 0))
        
        usersdb.commit()
    except sqlite3.OperationalError:
        usersinit()
        writefossil(userid,fossil)

def changescore(userid,increment):
    try:
        cursor = usersdb.execute("SELECT * FROM Users WHERE UserID = ?", (userid,))
        for row in cursor:
            score = row[2]
        
        score += increment
        usersdb.execute("UPDATE Users SET Score = ? WHERE UserID = ?", (score, userid))
        usersdb.commit()
    except sqlite3.OperationalError:
        usersinit()
        changescore(userid,increment)

def readallscores():
    scores = []

    try:
        cursor = usersdb.execute("SELECT * FROM Users")
        for row in cursor:
            scores.append([row[0],row[2]])
        
        return scores
    except sqlite3.OperationalError:
        usersinit()
        readallscores()

def changeMode(userid,mode):
    try:
        cursor = usersdb.execute("SELECT * FROM Users WHERE UserID = ?", (userid,))
        usersdb.execute("UPDATE Users SET Mode = ? WHERE UserID = ?", (mode, userid))
        usersdb.commit()
    except sqlite3.OperationalError:
        usersinit()
        changescore(userid,mode)