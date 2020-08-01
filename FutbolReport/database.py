from flask_sqlalchemy import SQLAlchemy
import os
from querys import *

db = SQLAlchemy()


def dame_la_lista_de_jugadores_del_ano(ano):
	if ano  == '2016':
		id_ini = 179510
		id_fin = 179889
	elif ano  == '2017':
		id_ini = 214386
		id_fin = 214765
	else: 		
		id_ini = 179510
		id_fin = 214765
	query_jug = db.session.execute(query_seleccionar_jugadores , {"id_ini":id_ini, "id_fin":id_fin})
	return [row for row in query_jug]


def dame_los_estadios():
	query_estadio = db.session.execute(query_seleccionar_estadios)
	estadios =  [row for row in query_estadio]
	return estadios

def seleccionar_equipos(ano):
	data = db.session.execute(query_seleccionar_equipos, {"ano": ano})
	equipos = [row for row in data]
	return  equipos

def seleccionar_equipo_concreto(ano,equipo):
	if ano  == '2016':
		id_ini = 179510
		id_fin = 179889
	elif ano  == '2017':
		id_ini = 214386
		id_fin = 214765
	else: 		
		id_ini = 179510
		id_fin = 214765
	data = db.session.execute(query_seleccionar_equipo_concreto, {"id_ini":id_ini, "id_fin":id_fin,"equipo":equipo})
	equipo_concreto = [row for row in data]
	return  equipo_concreto

def seleccionar_entrenador_concreto(ano,entrenador):
	if ano  == '2016':
		id_ini = 179510
		id_fin = 179889
	elif ano  == '2017':
		id_ini = 214386
		id_fin = 214765
	else: 		
		id_ini = 179510
		id_fin = 214765
	data = db.session.execute(query_seleccionar_entrenador_concreto, {"id_ini":id_ini, "id_fin":id_fin,"entrenador":entrenador})
	entrenador_concreto = [row for row in data]
	return  entrenador_concreto

def seleccionar_fecha_minima(ano):
	fec_min = db.session.execute(query_fecha_minima , {"ano": ano}).fetchone()[0]
	return  fec_min

def seleccionar_fecha_maxima(ano):
	fec_max = db.session.execute(query_fecha_maxima , {"ano": ano}).fetchone()[0]
	return  fec_max

def puntuaciones_hora(nombre,fecha,ano,equipo):
	if ano  == '2016':
		id_ini = 179510
		id_fin = 179889
	elif ano  == '2017':
		id_ini = 214386
		id_fin = 214765
	else: 		
		id_ini = 179510
		id_fin = 214765
	data = db.session.execute(query_puntuaciones_hora_partido, {"nombre": nombre,"fecha": fecha, "id_ini":id_ini, "id_fin":id_fin,"equipo": equipo})
	puntuaciones = [list(row) for row in data]	
	return  puntuaciones

def puntuaciones_rivales(nombre,fecha,ano,equipo):
	if ano  == '2016':
		id_ini = 179510
		id_fin = 179889
	elif ano  == '2017':
		id_ini = 214386
		id_fin = 214765
	else: 		
		id_ini = 179510
		id_fin = 214765	
	data = db.session.execute(query_puntuaciones_rivales, {"nombre": nombre,"fecha": fecha, "id_ini":id_ini, "id_fin":id_fin,"equipo":equipo})
	puntuaciones = [list(row) for row in data]
	return puntuaciones

def puntuaciones_rivales_media(nombre,fecha,ano,equipo):
	if ano  == '2016':
		id_ini = 179510
		id_fin = 179889
	elif ano  == '2017':
		id_ini = 214386
		id_fin = 214765
	else: 		
		id_ini = 179510
		id_fin = 214765	
	data = db.session.execute(query_puntuaciones_rivales_media, {"nombre": nombre,"fecha": fecha, "id_ini":id_ini, "id_fin":id_fin,"equipo":equipo})
	puntuaciones = [list(row) for row in data]
	return puntuaciones	


def puntuaciones_estacion_ano(nombre,fecha,ano,equipo):
	if ano  == '2016':
		id_ini = 179510
		id_fin = 179889
	elif ano  == '2017':
		id_ini = 214386
		id_fin = 214765
	else: 		
		id_ini = 179510
		id_fin = 214765	
	data = db.session.execute(query_estacion_ano, {"nombre": nombre,"fecha": fecha, "id_ini":id_ini, "id_fin":id_fin,"equipo":equipo})
	puntuaciones = [list(row) for row in data]
	return puntuaciones
	

def info_global(nombre,fecha,ano,equipo):
	if ano  == '2016':
		id_ini = 179510
		id_fin = 179889
	elif ano  == '2017':
		id_ini = 214386
		id_fin = 214765
	else: 		
		id_ini = 179510
		id_fin = 214765	
	data = db.session.execute(query_info_global, {"nombre": nombre,"fecha": fecha, "id_ini":id_ini, "id_fin":id_fin,"equipo":equipo})
	informacion_global = [list(row) for row in data]
	return  informacion_global

def puntuaciones_temperatura(nombre,fecha,ano,equipo):
	if ano  == '2016':
		id_ini = 179510
		id_fin = 179889
	elif ano  == '2017':
		id_ini = 214386
		id_fin = 214765
	else: 		
		id_ini = 179510
		id_fin = 214765	
	data = db.session.execute(query_temperatura, {"nombre": nombre,"fecha": fecha, "id_ini":id_ini, "id_fin":id_fin,"equipo":equipo})
	puntuaciones_temperatura = [list(row) for row in data]
	return  puntuaciones_temperatura

def desc_partidos(partido):
	data = db.session.execute(query_desc_partidos, {"partido": partido})
	puntuaciones_partido = [list(row) for row in data]
	return  puntuaciones_partido


def puntuaciones_lluvias(nombre,fecha,ano,equipo):
	if ano  == '2016':
		id_ini = 179510
		id_fin = 179889
	elif ano  == '2017':
		id_ini = 214386
		id_fin = 214765
	else: 		
		id_ini = 179510
		id_fin = 214765	
	data = db.session.execute(query_lluvias, {"nombre": nombre,"fecha": fecha, "id_ini":id_ini, "id_fin":id_fin,"equipo":equipo})
	puntuaciones_lluvias = [list(row) for row in data]
	return  puntuaciones_lluvias

def puntuaciones_humedad(nombre,fecha,ano,equipo):
	if ano  == '2016':
		id_ini = 179510
		id_fin = 179889
	elif ano  == '2017':
		id_ini = 214386
		id_fin = 214765
	else: 		
		id_ini = 179510
		id_fin = 214765	
	data = db.session.execute(query_humedad, {"nombre": nombre,"fecha": fecha, "id_ini":id_ini, "id_fin":id_fin,"equipo":equipo})
	puntuaciones_humedad = [list(row) for row in data]
	return  puntuaciones_humedad

def puntuaciones_velocidad_viento(nombre,fecha,ano,equipo):
	if ano  == '2016':
		id_ini = 179510
		id_fin = 179889
	elif ano  == '2017':
		id_ini = 214386
		id_fin = 214765
	else: 		
		id_ini = 179510
		id_fin = 214765	
	data = db.session.execute(query_viento, {"nombre": nombre,"fecha": fecha, "id_ini":id_ini, "id_fin":id_fin,"equipo":equipo})
	puntuaciones_viento = [list(row) for row in data]
	return  puntuaciones_viento


def dame_jugadores(ano):
	query_jugador_completo = db.session.execute(seleccionar_jugador_completo(ano))
	return  [ list(jug) for jug in query_jugador_completo]

def dame_equipos(ano):
	query_equipo_completo = db.session.execute(seleccionar_equipo_completo(ano))
	return  [ list(jug) for jug in query_equipo_completo]

def dame_entrenadores(ano):
	query_entrenador_completo = db.session.execute(seleccionar_entrenador_completo(ano))
	return  [ list(jug) for jug in query_entrenador_completo]

def equipo_global(nombre,ano):
	if ano  == '2016':
		id_ini = 179510
		id_fin = 179889
	elif ano  == '2017':
		id_ini = 214386
		id_fin = 214765
	else: 		
		id_ini = 179510
		id_fin = 214765	
	data = db.session.execute(query_equipo_global, {"nombre": nombre, "id_ini":id_ini, "id_fin":id_fin})
	puntuaciones_global = [list(row) for row in data]
	return  puntuaciones_global	

def equipo_local(nombre,ano):
	if ano  == '2016':
		id_ini = 179510
		id_fin = 179889
	elif ano  == '2017':
		id_ini = 214386
		id_fin = 214765
	else: 		
		id_ini = 179510
		id_fin = 214765	
	data = db.session.execute(query_equipo_local, {"nombre": nombre, "id_ini":id_ini, "id_fin":id_fin})
	puntuaciones_local = [list(row) for row in data]
	return  puntuaciones_local

def equipo_visitante(nombre,ano):
	if ano  == '2016':
		id_ini = 179510
		id_fin = 179889
	elif ano  == '2017':
		id_ini = 214386
		id_fin = 214765
	else: 		
		id_ini = 179510
		id_fin = 214765	
	data = db.session.execute(query_equipo_visitante, {"nombre": nombre, "id_ini":id_ini, "id_fin":id_fin})
	puntuaciones_visitante = [list(row) for row in data]
	return  puntuaciones_visitante

def equipo_estacion(nombre,ano):
	if ano  == '2016':
		id_ini = 179510
		id_fin = 179889
	elif ano  == '2017':
		id_ini = 214386
		id_fin = 214765
	else: 		
		id_ini = 179510
		id_fin = 214765	
	data = db.session.execute(query_equipo_estacion, {"nombre": nombre, "id_ini":id_ini, "id_fin":id_fin})
	puntuaciones_equipo_estacion = [list(row) for row in data]
	return  puntuaciones_equipo_estacion

def equipo_mejor(nombre,ano):
	if ano  == '2016':
		id_ini = 179510
		id_fin = 179889
	elif ano  == '2017':
		id_ini = 214386
		id_fin = 214765
	else: 		
		id_ini = 179510
		id_fin = 214765	
	data = db.session.execute(query_equipo_mejor, {"nombre": nombre, "id_ini":id_ini, "id_fin":id_fin})
	puntuaciones_equipo_mejor = [list(row) for row in data]
	return  puntuaciones_equipo_mejor

def equipo_peor(nombre,ano):
	if ano  == '2016':
		id_ini = 179510
		id_fin = 179889
	elif ano  == '2017':
		id_ini = 214386
		id_fin = 214765
	else: 		
		id_ini = 179510
		id_fin = 214765	
	data = db.session.execute(query_equipo_peor, {"nombre": nombre, "id_ini":id_ini, "id_fin":id_fin})
	puntuaciones_equipo_peor = [list(row) for row in data]
	return  puntuaciones_equipo_peor


def entrenador_global(nombre,equipo,ano):
	if ano  == '2016':
		id_ini = 179510
		id_fin = 179889
	elif ano  == '2017':
		id_ini = 214386
		id_fin = 214765
	else: 		
		id_ini = 179510
		id_fin = 214765	
	data = db.session.execute(query_entrenador_global, {"nombre": nombre,"equipo": equipo, "id_ini":id_ini, "id_fin":id_fin})
	puntuaciones_global = [list(row) for row in data]
	return  puntuaciones_global	

def entrenador_local(nombre,equipo,ano):
	if ano  == '2016':
		id_ini = 179510
		id_fin = 179889
	elif ano  == '2017':
		id_ini = 214386
		id_fin = 214765
	else: 		
		id_ini = 179510
		id_fin = 214765	
	data = db.session.execute(query_entrenador_local, {"nombre": nombre,"equipo": equipo, "id_ini":id_ini, "id_fin":id_fin})
	puntuaciones_local = [list(row) for row in data]
	return  puntuaciones_local

def entrenador_visitante(nombre,equipo,ano):
	if ano  == '2016':
		id_ini = 179510
		id_fin = 179889
	elif ano  == '2017':
		id_ini = 214386
		id_fin = 214765
	else: 		
		id_ini = 179510
		id_fin = 214765	
	data = db.session.execute(query_entrenador_visitante, {"nombre": nombre,"equipo": equipo, "id_ini":id_ini, "id_fin":id_fin})
	puntuaciones_visitante = [list(row) for row in data]
	return  puntuaciones_visitante

def entrenador_estacion(nombre,equipo,ano):
	if ano  == '2016':
		id_ini = 179510
		id_fin = 179889
	elif ano  == '2017':
		id_ini = 214386
		id_fin = 214765
	else: 		
		id_ini = 179510
		id_fin = 214765	
	data = db.session.execute(query_entrenador_estacion, {"nombre": nombre,"equipo": equipo, "id_ini":id_ini, "id_fin":id_fin})
	puntuaciones_entrenador_estacion = [list(row) for row in data]
	return  puntuaciones_entrenador_estacion

def entrenador_peor(nombre,equipo,ano):
	if ano  == '2016':
		id_ini = 179510
		id_fin = 179889
	elif ano  == '2017':
		id_ini = 214386
		id_fin = 214765
	else: 		
		id_ini = 179510
		id_fin = 214765	
	data = db.session.execute(query_entrenador_peor, {"nombre": nombre,"equipo": equipo, "id_ini":id_ini, "id_fin":id_fin})
	puntuaciones_entrenador_peor = [list(row) for row in data]
	return  puntuaciones_entrenador_peor

def entrenador_mejor(nombre,equipo,ano):
	if ano  == '2016':
		id_ini = 179510
		id_fin = 179889
	elif ano  == '2017':
		id_ini = 214386
		id_fin = 214765
	else: 		
		id_ini = 179510
		id_fin = 214765	
	data = db.session.execute(query_entrenador_mejor, {"nombre": nombre,"equipo": equipo, "id_ini":id_ini, "id_fin":id_fin})
	puntuaciones_entrenador_mejor = [list(row) for row in data]
	return  puntuaciones_entrenador_mejor	


def info_partido(id_partido):
	data = db.session.execute(query_info_partido, {"id_partido": id_partido})
	info_partido = [list(row) for row in data]
	return  info_partido

def jug_concreto(ano,id_jugador):
	if ano  == '2016':
		id_ini = 179510
		id_fin = 179889
	elif ano  == '2017':
		id_ini = 214386
		id_fin = 214765
	else: 		
		id_ini = 179510
		id_fin = 214765	
	data = db.session.execute(query_jugador_concreto, {"id_jugador":id_jugador,"id_ini":id_ini, "id_fin":id_fin})
	jug = [list(row) for row in data]
	return  jug
	