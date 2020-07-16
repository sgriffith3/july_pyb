#!/usr/bin/env python3
"""
Request:
    Export data from a table on a database and upload it to a storage area like box

What this code does:
    This code creates a sqlite database (mydb.db) with one table, and inserts one entry into it.
    Then, the code reads the data on the table, and saves it into a file.
    Finally, this code uses the boxsdk to upload our new file
"""

import sqlite3

# You will need to pip install boxsdk
# python3 -m pip install boxsdk
from boxsdk import DevelopmentClient

# This will prompt you for your Development Token - Get it from your box project
client = DevelopmentClient()


def build_db():
    """
    This function builds and populates the database
    """

    # This will connect to an existing database or create a new database
    conn = sqlite3.connect("mydb.db")

    # This sets up a cursor object to interact with the database
    d_b = conn.cursor()

    # This creates a table if it is not already there, called Users, with the four fields listed
    d_b.execute("""CREATE TABLE IF NOT EXISTS Users (fname,lname,uname,age)""")

    # This command populates the database with some specific values
    d_b.execute(
        """
              INSERT INTO Users (fname,lname,uname,age) 
              VALUES ('Sam','Griffith','sgriffith3','27')"""
    )

    # This command essentially is the "save" button
    # This is where the changes made will actually get applied
    conn.commit()
    conn.close()


def build_file(filename):
    """
    This function reads all the information from the Users table and saves it into a file
    """

    # This will connect to an existing database or create a new database
    conn = sqlite3.connect("mydb.db")

    # This sets up a cursor object to interact with the database
    d_b = conn.cursor()

    # Select all the information from the table called Users
    users = d_b.execute("""SELECT * from Users""")

    # The fetchall() function returns an iterable object
    all_users = users.fetchall()

    # Iterate through all lines of the database, and save them into a list
    user_info = []
    for user in all_users:
        inf = ""
        for info in user:
            inf += f" | {info}"
        user_info.append(inf)
    print(user_info)
    print(type(user_info))
    with open(filename, "w") as fyl:
        fyl.writelines(user_info)
    conn.close()


def upload_to_box(filename, folder_id):
    """
    This function uploads our file "filename" to a specific folder inside of our box account
    """
    new_file = client.folder(folder_id).upload(filename)
    print(
        'File "{0}" uploaded to Box with file ID {1}'.format(new_file.name, new_file.id)
    )


def main():
    """
    This is the main function
    """
    build_db()
    filename = input("What is the name of the file you wish to upload?\n")
    build_file(filename)
    folder_id = input("What folder do you wish to upload to? Provide your folder_id:\n")
    upload_to_box(filename, folder_id)


main()
# folder_id = '118025580874'
