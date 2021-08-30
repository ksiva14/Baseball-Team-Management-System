import sqlite3
#backend

def playerData():
    con = sqlite3.connect("player.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE player(id INTEGER PRIMARY KEY, PID text, Firstname text, Lastname text, Age text, Position text, Batting_Avg text, ERA text)")
    con.commit()
    con.close()

def addPlayerRec(PID, Firstname, Lastname, Age, Position, Batting_Avg, ERA):
    con = sqlite3.connect("player.db")
    cur = con.cursor()
    cur.execute("INSERT INTO player VALUES(NULL, ?,?,?,?,?,?,?", PID, Firstname, Lastname, Age, Position, Batting_Avg, ERA)
    con.commit()
    con.close()

def view():
    con = sqlite3.connect("player.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM player")
    row = cur.fetchall()
    con.close()
    return row

def delete(id):
    con = sqlite3.connect("player.db")
    cur = con.cursor()
    cur.execute("DELETE FROM player WHERE id = ?", (id,))
    con.commit()
    con.close()

def search(PID="", Firstname="", Lastname="", Age="", Position="", Batting_Avg="", ERA=""):
    con = sqlite3.connect("player.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM player WHERE PID=? OR Firstname=? OR Lastname=? OR Age=? OR Position=? OR Batting_Avg=?, OR ERA=? \
        ", (PID, Firstname, Lastname, Age, Position, Batting_Avg, ERA))
    row = cur.fetchall()
    con.close()
    return row

def update(id, PID="", Firstname="", Lastname="", Age="", Position="", Batting_Avg="", ERA=""):
    con = sqlite3.connect("player.db")
    cur = con.cursor()
    cur.execute("UPDATE player SET PID=? OR Firstname=? OR Lastname=? OR Age=? OR Position=? OR Batting_Avg=?, OR ERA=? WHERE id=? \
        ", (PID, Firstname, Lastname, Age, Position, Batting_Avg, ERA, id))
    con.commit()
    con.close()