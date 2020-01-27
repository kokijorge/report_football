all = [
("GOL", r"Goal.+?\.\s(.+)\s\(.+?\.(\sAssisted\sby\s)?(?(2)(((?!with)\w+\s?)+))" , "https://regex101.com/r/iqfjCx/1", (0,10), (2,3) ),
#  falta conseguir la asistencia que es opcional Goal.+\.\s(.+)\s\(.+shot from.+?Assisted by (.+)(with.+\.)?
("FALTA", r"Foul by\s(.+)\s\(.+\.", "https://regex101.com/r/q9tZBU/1", (0,-2) ),
("OCASION", r"Attempt missed\.\s(.+)\s\(.+?\.(\sAssisted\sby\s)?(?(2)(((?!with)\w+\s?)+))", "https://regex101.com/r/85UQmN/1", (0,4) , (2,2) )
]