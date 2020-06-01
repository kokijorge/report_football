from flask_sqlalchemy import SQLAlchemy
import os
from querys import *

db = SQLAlchemy()


def dame_la_lista_de_jugadores_del_ano(anoInt,equipo):
	fec_min = seleccionar_fecha_minima(anoInt)
	fec_max = seleccionar_fecha_maxima(anoInt)
	query_jug = db.session.execute(query_seleccionar_jugadores , {"fec_min": fec_min,"fec_max": fec_max, "nuevo_equipo":equipo})
	return [row for row in query_jug]


def dame_los_rivales ():
	query_rival = db.session.execute(QUERY_A_LA_QUE_AUN_NO_LE_HAS_DADO_NOMBRE)
	rivales =   [row for row in query_rival]
	lista_rivales = ",".join(["['"+rival[1]+"',"+str(rival[0])+"]" for rival in rivales])
	return lista_rivales	

def dame_los_estadios():
	query_estadio = db.session.execute(query_seleccionar_estadios)
	estadios =  [row for row in query_estadio]
	return estadios

def seleccionar_equipos(ano):
	data = db.session.execute(query_seleccionar_equipos_jugadores, {"ano": ano})
	equipos = [row for row in data]
	return  equipos

def seleccionar_fecha_minima(ano):
	fec_min = db.session.execute(query_fecha_minima , {"ano": ano}).fetchone()[0]
	return  fec_min

def seleccionar_fecha_maxima(ano):
	fec_max = db.session.execute(query_fecha_maxima , {"ano": ano}).fetchone()[0]
	return  fec_max

def puntuaciones_hora():
	data = db.session.execute(query_puntuaciones_hora_partido)
	puntuaciones = [row for row in data]
	lista_puntuaciones = ",".join(["['"+punt[1]+"',"+str(punt[0])+"]" for punt in puntuaciones])
	return  lista_puntuaciones

def puntuaciones_rivales():
	data = db.session.execute(query_puntuaciones_rivales)
	puntuaciones = [row for row in data]
	lista_puntuaciones = ",".join(["['"+punt[1]+"',"+str(punt[0])+"]" for punt in puntuaciones])
	return  lista_puntuaciones

def estacion_ano():
	data = db.session.execute(query_estacion_ano)
	puntuaciones = [row for row in data]
	lista_puntuaciones = ",".join(["['"+punt[0]+"',"+str(punt[1])+"]" for punt in puntuaciones])
	return  lista_puntuaciones 
	

def info_global():
	data = db.session.execute(query_info_global)
	info = [row for row in data]
	#informacion_global = ",".join(["['"+punt[0]+"',"+str(punt[1])+"]" for punt in info])
	#informacion_global = ",".join(["['"+punt[0]+"',"+punt[1]+"',"+str(punt[2])+"',"+str(punt[3])+"',"+str(punt[4])+"',"+str(punt[5])+"',"+str(punt[6])+"',"+str(punt[7])+"]" for punt in info])
	return  informacion_global