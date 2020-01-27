#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from collections import defaultdict
from rules_raw import all

DEBUG = False
FILE_A_PUNTUAR = "data/partido1.txt"


class Score:
	def __init__(self,score):
		self.index = score[0]
		self.points = score[1]
	def __str__(self):
		return "  Index: {0}\tPoints: {1} ".format(self.index,self.points) 

class Regex:
	def __init__(self, rule):
		self.name = rule[0]
		self.regex_raw = rule[1]
		self.pattern = re.compile(self.regex_raw, re.MULTILINE | re.UNICODE)

		self.url = rule[2]
		self.scores = [Score(score) for score in rule[3:]]

	def __str__(self):
		return "\n\n{0}\tURL: {1}\tREGEX: {2} \n{3} ".format(self.name,self.url, self.regex_raw, "\n".join([str(score) for score in self.scores])) 

	def score(self, comment):
		if DEBUG:
			print "scoring: " +comment
		partial = defaultdict(lambda: 0)
		result = self. pattern.match(comment)
		if result:
			groups = result.groups()
			if DEBUG:
				print "MAtch : " + str(groups)
			for score in self.scores:
				player = groups[score.index]
				points = score.points
				partial[player] += points
				print "{0} : {1}".format(player,points)
		if  len(partial):
			return partial
		else:
			return {}



		



regexes = []

for rule in all:
	regexes.append(Regex(rule))


for r in regexes:
	print r

print "\n\n\nVAMOS a puntuar " + FILE_A_PUNTUAR

with open(FILE_A_PUNTUAR) as f:
	#for c in f.readlines():
	#	comments.append( (c, afinn.score(c) ) )

	comments = f.readlines()

results = [r.score(comment) for comment in comments for r in regexes]

if DEBUG:
	print results

END = defaultdict(lambda: 0)
for result in results:
	for key, value in result.iteritems():
		END[key] += value

print "\nTOTALES"
print END



# P