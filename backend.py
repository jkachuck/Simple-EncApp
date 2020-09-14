import sqlite3
import pyAesCrypt

decrypted_loc = "./simple_encapp.db"

def connect():
    conn=sqlite3.connect(decrypted_loc)
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS encapp (id INTEGER PRIMARY KEY, website text, webid text, year interger, webpasswd integer)")
    conn.commit()
    conn.close()

def insert(website,webid,year,webpasswd):
    conn=sqlite3.connect(decrypted_loc)
    cur=conn.cursor()
    cur.execute("INSERT INTO encapp VALUES (NULL,?,?,?,?)",(website,webid,year,webpasswd) )
    conn.commit()
    conn.close()


def view_limit():
    conn=sqlite3.connect(decrypted_loc)
    cur=conn.cursor()
    cur.execute("SELECT id,website,webid,year FROM encapp")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(website="",webid="",year="",webpasswd=""):
    conn=sqlite3.connect(decrypted_loc)
    cur=conn.cursor()
    cur.execute("SELECT * FROM encapp WHERE website=? OR webid=? OR year=? OR webpasswd=?",(website,webid,year,webpasswd))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect(decrypted_loc)
    cur=conn.cursor()
    cur.execute("DELETE FROM encapp WHERE id=? ",(id,) )
    conn.commit()
    conn.close()
    
def update(id, website,webid,year,webpasswd):
    conn=sqlite3.connect(decrypted_loc)
    cur=conn.cursor()
    cur.execute("UPDATE encapp SET website=?, webid=?, year=?, webpasswd=? WHERE id=? ",(website,webid,year,webpasswd,id) )
    conn.commit()
    conn.close()


connect()

