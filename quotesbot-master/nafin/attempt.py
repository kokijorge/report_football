# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"Attempt missed\.\s(.+)\s\(.+?\.(\sAssisted\sby\s)?(?(2)(((?!with)\w+\s?)+))"

test_str = ("Foul by Anthony Lozano (Girona).\n"
	"Rubén Alcaraz (Real Valladolid) wins a free kick in the defensive half.\n"
	"Attempt missed. Álex Granell (Girona) left footed shot from more than 35 yards misses to the right. Assisted by Pere Pons.\n"
	"Foul by Borja Fernández (Real Valladolid).\n"
	"Borja García (Girona) wins a free kick in the defensive half.\n"
	"Substitution, Girona. Patrick Roberts replaces Cristhian Stuani.\n"
	"Attempt missed. Borja García (Girona) right footed shot from outside the box is high and wide to the right. Assisted by Marc Muniesa.\n"
	"Foul by Pere Pons (Girona).\n"
	"Attempt missed. Iago Aspas (Celta de Vigo) header from the centre of the box misses to the left. Assisted by Hugo Mallo with a cross.\n"
	"Offside, Espanyol. Sergi Darder tries a through ball, but Borja Iglesias is caught offside.\n"
	"Attempt blocked. Stanislav Lobotka (Celta de Vigo) right footed shot from outside the box is blocked. Assisted by Brais Méndez.\n"
	"Foul by Marc Roca (Espanyol).\n"
	"Brais Méndez (Celta de Vigo) wins a free kick in the attacking half.\n"
	"Attempt missed. Brais Méndez (Celta de Vigo) left footed shot from outside the box is too high. Assisted by Stanislav Lobotka.\n"
	"Attempt missed. Borja Iglesias (Espanyol) right footed shot from the centre of the box misses to the left. Assisted by Pablo Piatti.\n"
	"Corner,Celta de Vigo. Conceded by Dídac Vilá.\n")

matches = re.finditer(regex, test_str, re.MULTILINE | re.UNICODE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
