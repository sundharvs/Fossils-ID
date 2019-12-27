import sqlite3

def init():
    conn = sqlite3.connect("data.db")
    cursor = conn.execute("CREATE TABLE Users (UserID TEXT, Fossil TEXT, Score TEXT)")

def readplaintext(userid):
    conn = sqlite3.connect('data/users.db')
    try:
        cursor = conn.execute("SELECT * FROM Users WHERE USERID = ?", (userid,))
        for row in cursor:
            return row[1]
    except sqlite3.OperationalError:
        init()
        readplaintext(userid)

def writeplaintext(userid,plaintext):
    conn = sqlite3.connect('data/users.db')
    try:
        cursor = conn.execute("SELECT * FROM Users WHERE USERID = ?", (userid,))
        if(cursor.fetchone != None):
            conn.execute("UPDATE Users SET PLAINTEXT = ? WHERE USERID = ?", (plaintext, userid))
        if(cursor.fetchone() == None):
            conn.execute("INSERT INTO Users (USERID,PLAINTEXT,SCORE) VALUES (?, ?, ?);", (userid, plaintext, 0))
        
        conn.commit()
    except sqlite3.OperationalError:
        init()
        writeplaintext(userid,plaintext)

def changescore(userid,increment):
    conn = sqlite3.connect('data/users.db')

    try:
        cursor = conn.execute("SELECT * FROM Users WHERE USERID = ?", (userid,))
        for row in cursor:
            score = row[2]
        
        score += increment
        conn.execute("UPDATE Users SET SCORE = ? WHERE USERID = ?", (score, userid))
        conn.commit()
    except sqlite3.OperationalError:
        init()
        changescore(userid,increment)

def readallscores():
    scores = []
    conn = sqlite3.connect('data/users.db')

    try:
        cursor = conn.execute("SELECT * FROM Users")
        for row in cursor:
            scores.append([row[0],row[2]])
        
        return scores
    except sqlite3.OperationalError:
        init()
        readallscores()