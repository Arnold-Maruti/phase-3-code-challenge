import sqlite3

CONN=sqlite3.connect('my_database.db')
CURSOR=CONN.cursor()