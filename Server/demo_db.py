"""
    The point of this script is to create a database, then create
    a table, storing names and passwords, inside of it and finally
    add some users manually. The user of the script must provide
    the host name of the mysql server, the name of the user and the
    password in order for it to work. You can also change the constants
    DB_NAME and TABLE_NAME if you want.
"""

import mysql.connector

# The name of the database we will create
DB_NAME = "LoginDB"
# The name of the table storing the names and passwords
TABLE_NAME = "name_passwd"

# Connect to the mysql server
try:
    db = mysql.connector.connect(host="localhost",
                                user="root",
                                passwd="root",
                                )
except:
    print("Couldn't connect to the server.")
    exit(-1)

cursor = db.cursor()

cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
cursor.execute(f"USE {DB_NAME}")
cursor.execute(f"""CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                    name VARCHAR(255) PRIMARY KEY,
                    password VARCHAR(255) NOT NULL
                )""")

# Some accounts to insert in the database
accounts = [
    ("John", "1234"),
    ("George", "qwer"),
    ("Marie", "password"),
    ("Helen", "0000")
]

insert_sql = f"INSERT INTO {TABLE_NAME} VALUES (%s, %s)"

# Insert all the accounts
try:
    cursor.executemany(insert_sql, accounts)
    db.commit()
# In case the script has already been run
except:
    pass
