

import io
import json
from collections import defaultdict

from reglas import patterns
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


#FILE_A_PUNTUAR = "prueba.json"
FILE_A_PUNTUAR = "as2017_2018.json"

print ("\n\n\nVAMOS a puntuar " + FILE_A_PUNTUAR)


with io.open(FILE_A_PUNTUAR,"r", encoding="utf-8") as f:
	comments = f.read()

def puntua_partido(comments):

	final = defaultdict(lambda: 0)

	for line, comment in enumerate(comments):
		#print ("\n{0}\t{1}".format(line+1, comment.rstrip()))
		for p in patterns:
			for key, value in p.puntua(comment).items():
				final[key] += value

	print ("\nTOTALES")
	#print (json.dumps(final, sort_keys=True, indent=4, ensure_ascii=False))
	return final

jornadas = json.loads(comments)
total= len(jornadas)

for jornada in jornadas[0:total]:
	p = jornada['partido']
	partido =  str(p)
	min_com = jornada['comentarios']
	num_com = (len(min_com))
	a = puntua_partido([min_com['text'] for min_com in min_com[:num_com]])
	elementos = a.items()
	print (len (elementos))
	print (a.items())
	conn = psycopg2.connect(host="localhost", port = 5432, database="prueba1", user="postgres", password="postgres")
	conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
	cur = conn.cursor()	
	for nombre,puntuacion in elementos:	
		punt = str(puntuacion)		
		sqlInsert = """INSERT INTO tfg.dim_puntuacion(partido,nombre, puntuacion)VALUES ('"""+partido+"""','"""+nombre+"""', """+punt+""");"""
		print(sqlInsert)
		cur.execute(sqlInsert)	
	cur.close()
	conn.close()	