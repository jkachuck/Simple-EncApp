#!/usr/bin/python3
import sqlite3

def view():
    conn=sqlite3.connect("encapp_decrypted.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM encapp")
    rows=cur.fetchall()
    conn.close()
    print(len(rows))
    for x in rows:
        print (x )


view()




