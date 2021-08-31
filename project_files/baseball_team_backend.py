import sqlite3
#backend

#Function to connect to database and create player table/relation
def playerData():
    con = sqlite3.connect("player.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE player (id INTEGER PRIMARY KEY, PID text, Firstname text, Lastname text, Age text, Position text, Batting_Avg text, ERA text)")
    con.commit()
    con.close()

#Insert a new player
def addPlayerRec(PID, Firstname, Lastname, Age, Position, Batting_Avg, ERA):
    con = sqlite3.connect("player.db")
    cur = con.cursor()
    cur.execute("INSERT INTO player VALUES(NULL, ?,?,?,?,?,?,?)", (PID, Firstname, Lastname, Age, Position, Batting_Avg, ERA))
    con.commit()
    con.close()
#View  all the records from table player
def view():
    con = sqlite3.connect("player.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM player")
    row = cur.fetchall()
    con.close()
    return row
#Delete a specific player
def delete(id):
    con = sqlite3.connect("player.db")
    cur = con.cursor()
    cur.execute("DELETE FROM player WHERE id = ?", (id,))
    con.commit()
    con.close()
#Search for player given attributes
def search(PID="", Firstname="", Lastname="", Age="", Position="", Batting_Avg="", ERA=""):
    con = sqlite3.connect("player.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM player WHERE PID=? OR Firstname=? OR Lastname=? OR Age=? OR Position=? OR Batting_Avg=? OR ERA=? \
        ", (PID, Firstname, Lastname, Age, Position, Batting_Avg, ERA))
    row = cur.fetchall()
    con.close()
    return row
#Update player record info
def update(id, PID="", Firstname="", Lastname="", Age="", Position="", Batting_Avg="", ERA=""):
    con = sqlite3.connect("player.db")
    cur = con.cursor()
    cur.execute("UPDATE player SET PID=? OR Firstname=? OR Lastname=? OR Age=? OR Position=? OR Batting_Avg=? OR ERA=? WHERE id=? \
        ", (PID, Firstname, Lastname, Age, Position, Batting_Avg, ERA, id))
    con.commit()
    con.close()