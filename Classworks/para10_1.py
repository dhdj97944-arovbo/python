import sqlite3

connection = sqlite3.connect("ITSTEP.sl3", 5)
cur = connection.cursor()

cur.execute("CREATE TABLE first_table (name TEXT);")
connection

connection.close()
