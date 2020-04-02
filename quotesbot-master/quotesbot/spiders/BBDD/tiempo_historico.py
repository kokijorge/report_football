import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE

#https://pynative.com/python-postgresql-tutorial/#Python_PostgreSQL_Database_Connection
#https://towardsdatascience.com/python-and-postgresql-how-to-access-a-postgresql-database-like-a-data-scientist-b5a9c5a0ea43

conn = psycopg2.connect(host="localhost", port = 5432, database="prueba1", user="postgres", password="postgres")

conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
# Create a cursor object
cur = conn.cursor()

# A sample query of all data from the "vendors" table in the "suppliers" database
cur.execute("""select dia,id_partido,url from tfg.staging_tiempo_historico """)
print("The number of parts: ", cur.rowcount)
query_results = cur.fetchall()
print(query_results)
#row = cur.fetchone()
#while row is not None:
#	 print(row)
#    row = cur.fetchone()

cur.close()
conn.close()