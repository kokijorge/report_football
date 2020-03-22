
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
cur.execute("""SELECT * FROM  tfg.staging_jugador where nombre like '%Messi%' """)
query_results = cur.fetchall()
print(query_results)

name_Database   = "prueba2"
# Create table statement -> https://pythontic.com/database/postgresql/create%20database
sqlCreateDatabase = "create database "+name_Database+";"
cur.execute(sqlCreateDatabase)

# Close the cursor and connection to so the server can allocate
# bandwidth to other requests
cur.close()
conn.close()