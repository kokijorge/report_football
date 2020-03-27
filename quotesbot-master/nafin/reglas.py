#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from collections import defaultdict

DEBUG = False

"""
Match ends, Real Betis 0, Levante 3. -> ejemplo de que no hay puntuacion

Goal!Real Betis 0, Levante 3. José Luis Morales (Levante) right footed shot from the centre of the box to the bottom left corner. Assisted by Raphael Dwamena. -> ejemplo de doble puntuacion 10 para el que mete gol 3 para la asistencia

Foul by Gerard Gumbau (Leganés) -> ejemplo de restar, -2

Attempt missed. Juan Camilo Hernández (Huesca) left footed shot from outside the box misses to the left. Assisted by Gonzalo Melero -> ejemplo de ocacion, 4 al primero 2 al segundo

Attempt missed. Javi Guerra (Rayo Vallecano) right footed shot from the centre of the box is too high following a set piece situation -> ejemplo de puntuacion 2  
OJO que le estoy dando 4

Corner,Real Madrid. Conceded by Borja García -> ejemplo de puntuacion negativa -1

Manu García (Alavés) wins a free kick in the defensive half -> puntuacion +1
"""


def build_patterns():
	all = [
		("GOL", "https://regex101.com/r/iqfjCx/1", r"Goal.+?\.\s(.+)\s\(.+?\.(\sAssisted\sby\s)?(?(2)(((?!with|following)\w+\s?)+))" , (0,10,False), (2,3,True) ),
		("FALTA", "https://regex101.com/r/q9tZBU/1",  r"Foul by\s(.+)\s\(.+\.", (0,-2,False) ),
		("CORNER", "https://regex101.com/r/n3QmXH/1", r"Corner.+?Conceded by\s(.+)\.", (0,-1,False) ),
		("OCASION", "https://regex101.com/r/85UQmN/2", r"Attempt missed\.\s(.+)\s\(.+?\.(\sAssisted\sby\s)?(?(2)(((?!with|following)\w+\s?)+))", (0,4,False) , (2,2,True) ),
		("T.LIBRE", "https://regex101.com/r/2wRDRm/2", r"((\w+?\s)+)\(.+?\) wins a free kick", (0,1,False)  ),
		## "fuera de juego"  https://regex101.com/r/LDDCEN/1 
		## "tiro al palo" https://regex101.com/r/a4FWkt/1
		## "ocasion manifiesta"  https://regex101.com/r/JXnV7v/1
		## "amarilla" https://regex101.com/r/xINlXr/1 # no me coge el acento?
		## "tarjeta roja" https://regex101.com/r/xUJPp2/1
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
		if DEBUG:
			print ("scoring: " +comment)
		partial = defaultdict(lambda: 0)
		result = self.pattern.match(comment)
		if result:
			groups = result.groups()
			if DEBUG:
				print ("Match : " + str(groups))
			for score in self.scores:
				player = groups[score.index]
				if player: # a veces no hay segundo jugador, por ejemplo no hubo asistencia...
					points = score.points
					partial[player.strip()] += points  # no deberia tener que hacer strip si el regex estuviese bien construido
					print ("\t{0} : {1} {2}".format(self.name, player,points))
				elif not score.optional:
					#petardazo porque no podemos saltarnos un player obligatorio en un patron.
					9/0
		return dict(partial)


patterns = build_patterns()

# PRINTAMOS LOS PATRONES
for p in patterns:
	print (p)
