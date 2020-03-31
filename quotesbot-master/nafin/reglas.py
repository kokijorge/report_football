#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from collections import defaultdict

def build_patterns():
	all = [
	#2017-2018
		("GOL", "https://regex101.com/r/iqfjCx/1", r"Goal.+?\.\s(.+)\s\(.+?\.(\sAssisted\sby\s)?(?(2)(((?!with|following)\w+\s?)+))" , (0,10,False), (2,3,True) ),
		("FALTA", "https://regex101.com/r/q9tZBU/1",  r"Foul by\s(.+)\s\(.+\.", (0,-2,False) ),
		("CORNER", "https://regex101.com/r/n3QmXH/1", r"Corner.+?Conceded by\s(.+)\.", (0,-1,False) ),
		("OCASION", "https://regex101.com/r/85UQmN/4", r"Attempt missed\.\s(.+)\s\(.+?\.(\sAssisted\sby\s)?(?(2)(((?!with|following|from)\w+\s?)+))", (0,4,False) , (2,2,True) ),
		("T.LIBRE", "https://regex101.com/r/2wRDRm/2", r"((\w+?\s)+)\(.+?\) wins a free kick", (0,1,False)  ),
		("FUERA DE JUEGO",  "https://regex101.com/r/LDDCEN/2", r"Offside.+?but\s(.+)\sis\scaught\soffside" , (0,-1,False)),
		("TIRO AL PALO", "https://regex101.com/r/a4FWkt/2", r"((\w+?\s)+)\(.+?\)\shits\sthe\sbar.+?\." , (0,3,False)),
		("OCASION MANIFIESTA",  "https://regex101.com/r/JXnV7v/2" ,r"Dangerous play by\s(.+)\s\(.+\." , (0,2,False)),
		("AMARILLA" , "https://regex101.com/r/xINlXr/3", r"((\w+?\s)+)\(.+?\) is shown the yellow card.*", (0,-2,False)),
		("ROJA", "https://regex101.com/r/xUJPp2/2", r"((\w+?\s)+)\(.+?\) is shown the red card", (0,-6,False)),
		("PENALTI CONSEGUIDO",  "https://regex101.com/r/bD0s7T/2" , r"Penalty.+?[.]\s(.+)\sdraws\s.*", (0,4,False)),
		("PENALTI CONCEDIDO", "https://regex101.com/r/raGpDg/2", r"Penalty conceded by\s(.+)\s\(.+\.",(0,-4,False))
	#2016-2017
	]
	result = []
	for rule in all:
		result.append(Patron(rule))
	return result



class Puntuacion:
	def __init__(self,score):
		self.index = score[0]
		self.points = score[1]
		self.optional = score[2]


	def __str__(self):
		return "\t\tIndex: {0}\tPoints: {1} ".format(self.index,self.points) 

class Patron:
	def __init__(self, rule):
		self.name = rule[0]
		self.url = rule[1]
		self.regex_raw = rule[2]
		self.pattern = re.compile(self.regex_raw, re.UNICODE)
		self.scores = [Puntuacion(score) for score in rule[3:]]

	def __str__(self):
		return "\n{0}\t\tURL: {1}\tREGEX: {2} \n{3} ".format(self.name,self.url, self.regex_raw, "\n".join([str(score) for score in self.scores])) 

	def puntua(self, comment):		
		partial = defaultdict(lambda: 0)
		result = self.pattern.match(comment)
		if result:
			groups = result.groups()			
			for score in self.scores:
				player = groups[score.index]
				if player: # a veces no hay segundo jugador, por ejemplo no hubo asistencia...
					points = score.points
					partial[player.strip()] += points  # no deberia tener que hacer strip si el regex estuviese bien construido					
				elif not score.optional:					
					9/0
		return dict(partial)


patterns = build_patterns()

# PRINTAMOS LOS PATRONES
#for p in patterns:
#	print (p)