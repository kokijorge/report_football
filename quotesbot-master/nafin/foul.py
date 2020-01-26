# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"Foul by\s(.+)\s\(.+\."

test_str = ("\n"
	"Foul by Antonio Barragán (Real Betis).\n"
	"Attempt blocked. Takashi Inui (Real Betis) right footed shot from outside the box is blocked.\n"
	"José Luis Morales (Levante) wins a free kick in the defensive half.\n"
	"Foul by Andrés Guardado (Real Betis).\n"
	"Foul by Antonio Sanabria (Real Betis).\n"
	"Sanjin Prcic (Levante) wins a free kick in the defensive half.\n"
	"Antonio Luna (Levante) is shown the yellow card.\n"
	"Foul by Coke (Levante).\n"
	"Andrés Guardado (Real Betis) wins a free kick in the defensive half.\n"
	"Sanjin Prcic (Levante) wins a free kick on the left wing.\n"
	"Foul by Antonio Barragán (Real Betis).\n"
	"Delay over. They are ready to continue.\n"
	"Delay in match(Real Betis).\n"
	"Jason (Levante) wins a free kick in the defensive half.\n"
	"Foul by Andrés Guardado (Real Betis).\n"
	"Corner,Levante. Conceded by Andrés Guardado.\n"
	"Substitution, Real Betis. Antonio Barragán \n"
	"Pedro Porro (Girona) wins a free kick in the defensive half.\n"
	"Foul by Anuar Mohamed (Real Valladolid).\n"
	"Kiko Olivas (Real Valladolid) wins a free kick in the defensive half.\n"
	"Foul by Cristhian Stuani (Girona).\n"
	"Foul by Anthony Lozano (Girona).\n"
	"Keko (Real Valladolid) wins a free kick in the defensive half.\n"
	"Attempt missed. Cristhian Stuani (Girona) right footed shot from the right side of the box is close, but misses to the left. Assisted by Borja García.\n"
	"Álex Granell (Girona) wins a free kick in the defensive half.\n"
	"Foul by Anuar Mohamed (Real Valladolid).\n"
	"Substitution, Real Valladolid. Óscar Plano replaces Chris Ramos.\n"
	"Attempt missed. Portu (Girona) right footed shot from a difficult angle on the right is high and wide to the right.\n"
	"Marc Muniesa (Girona) wins a free kick in the defensive half.\n"
	"Foul by Anuar Mohamed (Real Valladolid).\n")

matches = re.finditer(regex, test_str, re.MULTILINE | re.UNICODE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
