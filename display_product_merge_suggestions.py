import mysql.connector
import pandas as pd


db_conn = mysql.connector.Connect(
   host="localhost", 
   user="dbeaver", 
   port='3307', 
   password="dbeaver",
   database="public")

query = """
SELECT
		pd.title AS group_title,
		count(pdl.product_id) AS product_count,
		pd.updated_at
	FROM public.product_duplicate_lists_dummy pdl
	LEFT JOIN public.product_duplicates_dummy pd ON
		pdl.product_duplicate_id = pd.id
	GROUP BY 1,3;
"""

df = pd.read_sql(query, db_conn)
print(df.head())
