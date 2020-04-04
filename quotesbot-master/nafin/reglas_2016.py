#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from collections import defaultdict

def build_patterns():
	all = [	
		("GOL", "https://regex101.com/r/8eilSg/2", r"Goal by\s(.+)\s\(.+The pass was from\s(.+?(?=[.]))" , (0,20,False), (1,8,False) ),		
		("GOL_2", "https://regex101.com/r/UVDSfh/2", r"Goal by\s(.+)\s\(.+After a pass from\s(.+?(?=[.]))" , (0,20,False), (1,8,False) ),
		("FALTA", "https://regex101.com/r/quaIE7/4",  r"(It's a )?[Ff]oul by([^.]*)", (1,-1,False) ),		
		("AMARILLA" , "https://regex101.com/r/Ujrp8k/2", r"Yellow card to ([^.]*)", (0,-3,False)),
		("AMARILLA_2" , "https://regex101.com/r/WayZsu/1", r"Card to ([^.]*)", (0,-3,False)),
		("ROJA", "https://regex101.com/r/ze2Kla/2", r"Red card to ([^.]*)", (0,-6,False)),
		("FUERA DE JUEGO",  "https://regex101.com/r/ghDh2e/1", r"((\w+?\s)+)was offside" , (0,-1,False)),
		("PENALTY",  "https://regex101.com/r/9ztSsW/2", r"Penalty awarded against\s(.+?(?=[.])).\sfor foul on\s(.+?(?=[.]))" , (0,-5,False),(1,6,True) ),
		("CENTRO",  "https://regex101.com/r/vz3RRx/1", r"(.+)\sputs in a cross" , (0,1,False)),
		("PARADA_1",  "https://regex101.com/r/iUcDrD/5", r"(.+)[.]( He's missed the penalty | Direct free kick | Has taken a direct free kick )?(.+)\s(saves)[.]" , (2,1,False)),
		("PARADA_2",  "https://regex101.com/r/1wcK0B/6", r"(.+)[.]( He's missed the penalty | Direct free kick | Has taken a direct free kick )?(.+)\s(takes the ball)[.]" , (2,1,False))
		# goal chance(https://regex101.com/r/LwEwrF/3) 
		# revisar goles y chances
		# arreglar lo de F.Navarro
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