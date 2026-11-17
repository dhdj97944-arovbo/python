import sqlite3

connection = sqlite3.connect("ITSTEP.sl3", 5)
cur = connection.cursor()

cur.execute("INSERT INTO first_table (name) VALUES ('Vasyul');")
connection.commit()

connection.close()
