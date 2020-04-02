

import io
import json
from collections import defaultdict

from reglas_2016 import patterns
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


#FILE_A_PUNTUAR = "as2016_2017.json"
FILE_A_PUNTUAR = "as2017_2018.json"

print ("\n\n\nVAMOS a puntuar " + FILE_A_PUNTUAR)


def puntua_partido(comments):

	final = defaultdict(lambda: 0)

	for line, comment in enumerate(comments):		
		for p in patterns:
			for key, value in p.puntua(comment).items():
				final[key] += value	
	return final

