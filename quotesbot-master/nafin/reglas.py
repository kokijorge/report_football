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

all = [
("GOL", r"Goal.+?\.\s(.+)\s\(.+?\.(\sAssisted\sby\s)?(?(2)(((?!with)\w+\s?)+))" , "https://regex101.com/r/iqfjCx/1", (0,10,False), (2,3,True) ),
#  falta conseguir la asistencia que es opcional Goal.+\.\s(.+)\s\(.+shot from.+?Assisted by (.+)(with.+\.)?
("FALTA", r"Foul by\s(.+)\s\(.+\.", "https://regex101.com/r/q9tZBU/1", (0,-2,False) ),
("CORNER", r"Corner.+?Conceded by\s(.+)\.", "https://regex101.com/r/n3QmXH/1", (0,-1,False) ),
("OCASION", r"Attempt missed\.\s(.+)\s\(.+?\.(\sAssisted\sby\s)?(?(2)(((?!with)\w+\s?)+))", "https://regex101.com/r/85UQmN/1", (0,4,False) , (2,2,True) ),
("T. LIBRE", r"((\w+?\s)+)\(.+?\) wins a free kick", "https://regex101.com/r/2wRDRm/1", (0,1,False)  ),
]

class Score:
	def __init__(self,score):
		self.index = score[0]
		self.points = score[1]
		self.optional = score[2]


	def __str__(self):
		return "\t\tIndex: {0}\tPoints: {1} ".format(self.index,self.points) 

class Patron:
	def __init__(self, rule):
		self.name = rule[0]
		self.regex_raw = rule[1]
		self.pattern = re.compile(self.regex_raw, re.UNICODE)

		self.url = rule[2]
		self.scores = [Score(score) for score in rule[3:]]

	def __str__(self):
		return "\n{0}\t\tURL: {1}\tREGEX: {2} \n{3} ".format(self.name,self.url, self.regex_raw, "\n".join([str(score) for score in self.scores])) 

	def score(self, comment):
		if DEBUG:
			print "scoring: " +comment
		partial = defaultdict(lambda: 0)
		result = self. pattern.match(comment)
		if result:
			groups = result.groups()
			if DEBUG:
				print "Match : " + str(groups)
			for score in self.scores:
				player = groups[score.index]
				if player: # a veces no hay segundo jugador, por ejemplo no hubo asistencia...
					points = score.points
					partial[player.strip()] += points  # no deberia tener que hacer strip si el regex estuviese bien construido
					print "\t{0} : {1} {2}".format(self.name, player,points)
				elif not score.optional:
					#petardazo porque no podemos saltarnos un player obligatorio en un patron.
					9/0
		if  len(partial):
			return partial
		else:
			return {}


patrones = []

for rule in all:
	patrones.append(Patron(rule))


# PRINTAMOS LOS PATRONES

for p in patrones:
	print p
