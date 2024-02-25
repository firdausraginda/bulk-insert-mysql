import mysql.connector


db_conn = mysql.connector.Connect(
   host="localhost", 
   user="dbeaver", 
   port='3307', 
   password="dbeaver",
   database="public")

db_cursor = db_conn.cursor()

query = """
SELECT
		pd.title AS group_title,
		count(pdl.product_id) AS product_count,
		pd.updated_at
	FROM public.product_duplicate_lists pdl
	LEFT JOIN public.product_duplicates pd ON
		pdl.product_duplicate_id = pd.id
	GROUP BY 1,3;
"""

try:
    db_cursor.execute(query)
    query_result = db_cursor.fetchall()
    for item in query_result:
        print(item)
except Exception as e:
    raise e

db_conn.close()
