# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"Goal.+?\.\s(.+)\s\(.+?\.(\sAssisted\sby\s)?(?(2)(((?!with)\w+\s?)+))"

test_str = ("Attempt missed\\.\\s(.+)\\s\\(.+?\\.(\\sAssisted\\sby\\s)?(?(2)(((?!with)\\w+\\s?)+))\n\n\n\n\n\n"
	"Goal!Real Betis 0, Levante 3. José Luis Morales (Levante) right footed shot from the centre of the box to the bottom left corner. Assisted by Raphael Dwamena.\n"
	"Corner,Levante. Conceded by Antonio Barragán.\n"
	"Attempt saved. José Luis Morales (Levante) right footed shot from the centre of the box is saved in the centre of the goal. Assisted by Chema Rodríguez.\n\n"
	"Goal!Athletic Club 2, Leganés 1. Iker Muniain (Athletic Club) right footed shot from very close range to the bottom right corner. Assisted by Raúl García with a cross.\n\n"
	"Goal!Real Betis 0, Levante 2. José Luis Morales (Levante) right footed shot from the centre of the box to the bottom left corner following a fast break.\n"
	"Corner,Real Betis. Conceded by Chema Rodríguez.\n"
	"Foul by Roger Martí (Levante).\n\n"
	"Goal!Barcelona 2, Alavés 0. Coutinho (Barcelona) right footed shot from the centre of the box to the centre of the goal. Assisted by Arthur.\n"
	"Attempt saved. Coutinho (Barcelona) right footed shot from the centre of the box is saved in the bottom left corner. Assisted by Lionel Messi with a through ball.")

matches = re.finditer(regex, test_str, re.MULTILINE | re.UNICODE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
