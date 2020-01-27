import sys  
reload(sys)  
sys.setdefaultencoding('utf8')


import io
import json
from collections import defaultdict

from reglas import patrones


FILE_A_PUNTUAR = "data/partido1.txt"
FILE_A_PUNTUAR = "ejemplos.txt"

print "\n\n\nVAMOS a puntuar " + FILE_A_PUNTUAR
print "================" +  "="*len(FILE_A_PUNTUAR)

with io.open(FILE_A_PUNTUAR,"r", encoding="utf-8") as f:
	comments = f.readlines()

def puntua_partido(comments):

	final = defaultdict(lambda: 0)

	for line, comment in enumerate(comments):
		print "\n{0}\t{1}".format(line+1, comment.rstrip())
		for p in patrones:
			for key, value in p.score(comment).iteritems():
				final[key.encode('utf8')] += value

	print "\nTOTALES"
	print json.dumps(final, sort_keys=True, indent=4, ensure_ascii=False)
	#print final
	return final

puntua_partido(comments)

