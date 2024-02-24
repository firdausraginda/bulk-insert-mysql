import mysql.connector

db_conn = mysql.connector.Connect(
   host="localhost", 
   user="dbeaver", 
   port='3307', 
   password="dbeaver",
   database="public")

db_cursor = db_conn.cursor()

with open("./127-0-0-1dummy_baltini20231206-12-23.sql", encoding="utf-8") as f:
    commands = f.read().split(';')

for command in commands:
    try:
        db_cursor.execute(command)
    except Exception as e:
        continue
    else:
        print(command)

db_conn.close()
