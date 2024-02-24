import mysql.connector


db_conn = mysql.connector.Connect(
   host="localhost", 
   user="dbeaver", 
   port='3307', 
   password="dbeaver",
   database="public")

db_cursor = db_conn.cursor()

path_to_file = "./127-0-0-1dummy_baltini20231206-12-23.sql"
with open(path_to_file, encoding="utf-8") as f:
    commands = f.read().split('\n\n')

for command in commands:    
    try:
        if not command.strip().startswith("#"):
            temp_sub_command = ""
            for per_line_command in command.strip().split("\n"):
                temp_sub_command += per_line_command
                if per_line_command.endswith(";"):
                    db_cursor.execute(temp_sub_command)
                    temp_sub_command = ""
            
    except Exception as e:
        print(command)
        raise e

db_conn.close()
