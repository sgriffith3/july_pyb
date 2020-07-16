import sqlite3

conn = sqlite3.connect("mydb.db")

db = conn.cursor()

db.execute("""CREATE TABLE IF NOT EXISTS Users (fname,lname,uname,age)""")

db.execute("""INSERT INTO Users (fname,lname,uname,age) VALUES ('Sam','Griffith','sgriffith3','27')""")

conn.commit()

users = db.execute("""SELECT * from Users""")
all_users = users.fetchall()
for user in all_users:
    print(user)

