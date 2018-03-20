import sqlite3 as sql

def insert_user(username, password):
    with sql.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM users WHERE username=?", [username])
        if cur.fetchone()[0]>0: return False
        result = cur.execute(
            "INSERT INTO users (username, password)"
            " VALUES (?,?)"
            , (username, password))
        con.commit()
        return True

def db_login(username, password):
    with sql.connect('database.db') as con:
        cur = con.cursor()
        sqltext = "SELECT COUNT(*) FROM users WHERE (username=? AND password=?)"
        cur.execute(sqltext, (username, password))
        return (cur.fetchone()[0]>0)

def create_trip(name, destination, user1, user2):
    with sql.connect('database.db') as con:
        cur = con.cursor()
        sqltext = ("INSERT INTO trips (name, destination, user1, user2)"
            " VALUES (?, ?)")
        cur.execute(sqltext, (name, destination, user1, user2))
        con.commit()
        return True

def db_delete_trip(id):
    with sql.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("DELETE FROM trips WHERE id=?", [id])
        val = cur.fetchone()[0]
        cur.commit()
        return val

