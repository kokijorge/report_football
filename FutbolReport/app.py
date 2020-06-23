from database import *
from flask import Flask,render_template,request ,redirect, url_for,flash,jsonify
import json
import flask
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__ ,static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI","postgresql://postgres:postgres@localhost:5432/futbol_report")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

#sesion
app.secret_key = 'mysecretkey'


@app.route('/')
def index():	
	return redirect('2016')

@app.route('/equipos/<string:ano>')
def equipos(ano):
	data = db.session.execute( query_seleccionar_equipos, {"ano": ano})
	equipos = [row for row in data]
	entero = int(ano)
	temp = str(entero+1)
	equipos_jugadores = seleccionar_equipos(ano)
	return render_template('equipos.tpl', equipos = equipos , temporada_seleccionada = ano,temp=temp,equipos_jugadores=equipos_jugadores)

@app.route('/<string:ano>')
def temporada(ano):
	equipos_jugadores = seleccionar_equipos(ano)
	return render_template('base.tpl', temporada_seleccionada = ano,equipos_jugadores=equipos_jugadores)

@app.route('/top/<string:ano>')
def top(ano):
	entero = int(ano)
	temp = str(entero+1)
	puntuaciones = db.session.execute(query_seleccionar_puntuaciones , {"ano": ano})
	puntos = [row for row in puntuaciones]
	equipos_jugadores = seleccionar_equipos(ano)
	goles = db.session.execute( query_seleccionar_goleadores, {"ano": ano})
	goleadores = [row for row in goles]
	tarjeta_amarilla = db.session.execute(query_seleccionar_tarjeta_amarilla, {"ano": ano})
	amarillas = [row for row in tarjeta_amarilla]
	tarjeta_roja = db.session.execute(query_seleccionar_tarjeta_roja, {"ano": ano})
	rojas = [row for row in tarjeta_roja]
	jug_minutos = db.session.execute(query_seleccionar_minutos_jugados , {"ano": ano})
	minutos = [row for row in jug_minutos]
	jug_titularidades = db.session.execute(query_seleccionar_titularidades, {"ano": ano})
	titularidades = [row for row in jug_titularidades]

	return render_template('top.tpl', puntos = puntos,goleadores=goleadores , temporada_seleccionada = ano, temp=temp,equipos_jugadores=equipos_jugadores,amarillas=amarillas,rojas=rojas,minutos=minutos,titularidades=titularidades)


@app.route('/entrenadores/<string:ano>')
def entrenadores(ano):
	entero = int(ano)
	temp = str(entero+1)
	fec_min = seleccionar_fecha_minima(ano)
	fec_max = seleccionar_fecha_maxima(ano)
	query_entrenadores = db.session.execute(query_seleccionar_entrenadores , {"fec_min": fec_min,"fec_max": fec_max})
	entrenadores = [row for row in query_entrenadores]		
	equipos_jugadores = seleccionar_equipos(ano)
	return render_template('entrenadores.tpl',entrenadores=entrenadores , temporada_seleccionada = ano, temp=temp,equipos_jugadores=equipos_jugadores)

@app.route('/jornadas/<string:jornada>/<string:ano>')
def jornadas(ano,jornada):
	entero = int(ano)
	if not jornada:
		jornada= '1'
	temp = str(entero+1)
	query_jornadas = db.session.execute(query_seleccionar_jornadas , {"ano": ano , "jornada":jornada})
	jornadas = [row for row in query_jornadas]
	query_num = db.session.execute(query_seleccionar_num_jornadas,  {"ano": ano})
	num_jornadas = [row for row in query_num]
	equipos_jugadores = seleccionar_equipos(ano)
	return render_template('jornadas.tpl', temporada_seleccionada = ano ,jornada_seleccionada=jornada, temp=temp,jornadas = jornadas,num_jornadas=num_jornadas,equipos_jugadores=equipos_jugadores)


@app.route('/jugadores/<string:equipo>/<string:ano>')
def jugadores(ano,equipo):
	equipos_jugadores = seleccionar_equipos(ano)
	entero = int(ano)
	temp = str(entero+1)
	nuevo_equipo = equipo.replace('%20', ' ')
	jugadores = dame_la_lista_de_jugadores_del_ano(ano,nuevo_equipo)

	return render_template('jugadores.tpl', temporada_seleccionada = ano,equipos_jugadores=equipos_jugadores,jugadores=jugadores,temp=temp,nuevo_equipo=nuevo_equipo)

@app.route('/estadios/<string:ano>')
def estadios(ano):
	equipos_jugadores = seleccionar_equipos(ano)
	estadios =  dame_los_estadios()
	return render_template('estadios.tpl', temporada_seleccionada = ano,equipos_jugadores=equipos_jugadores,estadios=estadios)

@app.route('/informes/<string:ano>')
def informes(ano):
	equipos_jugadores = seleccionar_equipos(ano)
	return render_template('informes.tpl', temporada_seleccionada = ano,equipos_jugadores=equipos_jugadores)

@app.route('/informes/completo_jugador/')
def informes_completo_jugador():	
	anos_jugadores_select = {'2016': dame_jugadores('2016'), '2017': dame_jugadores('2017'),'todo': dame_jugadores('todo')}	
	return render_template('informes_completo_jugador.tpl',anos_jugadores_select=anos_jugadores_select)

@app.route('/informes/completo_equipo/')
def informes_completo_equipo():	
	anos_equipos_select = {'2016': dame_equipos('2016'), '2017': dame_equipos('2017'),'todo': dame_equipos('todo')}	
	return render_template('informes_completo_equipo.tpl',anos_equipos_select=anos_equipos_select)

@app.route('/informes/completo_entrenador/')
def informes_completo_entrenador():	
	anos_entrenadores_select = {'2016': dame_entrenadores('2016'), '2017': dame_entrenadores('2017'),'todo': dame_entrenadores('todo')}	
	return render_template('informes_completo_entrenador.tpl',anos_entrenadores_select=anos_entrenadores_select)

@app.route('/jugador_completo')
def jugador_completo():
	jugador = request.args.get('nombre')
	fecha = request.args.get('fecha')
	ano = request.args.get('ano')

	return { 'jugador':jugador, 'fecha':fecha, 'ano':ano
		, 	'puntuaciones_rivales' : puntuaciones_rivales(jugador,fecha,ano)
		,	'puntuaciones_hora_partido' : puntuaciones_hora(jugador,fecha,ano)
		,	'puntuaciones_estacion_ano' : puntuaciones_estacion_ano(jugador,fecha,ano)
		,	'puntuaciones_info_global' : info_global(jugador,fecha,ano)
		,	'puntuaciones_temperatura' : puntuaciones_temperatura(jugador,fecha,ano)
		,	'puntuaciones_lluvias' : puntuaciones_lluvias(jugador,fecha,ano)
		,	'puntuaciones_humedad' : puntuaciones_humedad(jugador,fecha,ano)
		,	'puntuaciones_viento' : puntuaciones_velocidad_viento(jugador,fecha,ano)}


@app.route('/equipo_completo')
def equipo_completo():
	equipo = request.args.get('nombre')	
	ano = request.args.get('ano')
	return { 'equipo':equipo, 'ano':ano
	,	'puntuaciones_equipo_global' : equipo_global(equipo,ano)
	,	'puntuaciones_equipo_local' : equipo_local(equipo,ano)
	,	'puntuaciones_equipo_visitante' : equipo_visitante(equipo,ano)
	,	'puntuaciones_equipo_estacion' : equipo_estacion(equipo,ano)
	,	'puntuaciones_equipo_mejor' : equipo_mejor(equipo,ano)
	,	'puntuaciones_equipo_peor' : equipo_peor(equipo,ano)}


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8000,debug= True)
