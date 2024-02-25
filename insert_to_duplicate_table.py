import mysql.connector
import pathlib
import os


def set_path_to_sql_file(file_name=""):
    current_path = pathlib.Path(__file__).absolute()
    config_dir_path = current_path.parent.joinpath(f"sql_file/{file_name}")
    return config_dir_path

db_conn = mysql.connector.Connect(
   host="localhost", 
   user="dbeaver", 
   port='3307', 
   password="dbeaver",
   database="public")

db_cursor = db_conn.cursor()

for file in os.listdir(set_path_to_sql_file()):
    try:
        complete_path_to_sql_file = set_path_to_sql_file(file)
        query_insert = open(complete_path_to_sql_file).read()
        db_cursor.execute(query_insert)
    except Exception as e:
        raise e
    else:
        print(f'{query_insert}\n')
        print('query above executed successfully!')
        print('------------------------------')

db_conn.close()