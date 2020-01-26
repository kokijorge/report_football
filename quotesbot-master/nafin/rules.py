all = [
("Goal.+?\.\s(.+)\s\(.+?\.(\sAssisted\sby\s)?(?(2)(((?!with)\w+\s?)+))" , 10, 3),
#  falta conseguir la asistencia que es opcional Goal.+\.\s(.+)\s\(.+shot from.+?Assisted by (.+)(with.+\.)?
("Foul by\s(.+)\s\(.+\.", -2),
("Attempt missed\.\s(.+)\s\(.+?\.(\sAssisted\sby\s)?(?(2)(((?!with)\w+\s?)+))", 4 , 2)
]