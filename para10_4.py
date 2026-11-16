import sqlite3

connection = sqlite3.connect("ITSTEP.sl3", 5)
cur = connection.cursor()

print(cur)
print(connection)

cur.execute("UPDATE first_table SET name='Dima' WHERE rowid=2;")
connection.commit()

connection.close()
