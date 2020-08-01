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
	return redirect('/top/2016')

@app.route('/equipos/<string:ano>')
def equipos(ano):	
	equipos = seleccionar_equipos(ano)
	entero = int(ano)
	temp = str(entero+1)	
	return render_template('equipos.tpl', equipos = equipos , temporada_seleccionada = ano,temp=temp)

@app.route('/equipos/<string:ano>/<string:equipo>')
def equipo_concreto(ano,equipo):
	equipo_concreto = seleccionar_equipo_concreto(ano,equipo)
	entero = int(ano)
	temp = str(entero+1)	
	return render_template('equipo_concreto.tpl', equipo_concreto = equipo_concreto , temporada_seleccionada = ano,temp=temp)

@app.route('/<string:ano>')
def temporada(ano):
	return render_template('base.tpl', temporada_seleccionada = ano)

@app.route('/top/<string:ano>')
def top(ano):
	entero = int(ano)
	temp = str(entero+1)
	puntuaciones = db.session.execute(query_seleccionar_puntuaciones , {"ano": ano})
	puntos = [row for row in puntuaciones]	
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

	return render_template('top.tpl', puntos = puntos,goleadores=goleadores , temporada_seleccionada = ano, temp=temp,amarillas=amarillas,rojas=rojas,minutos=minutos,titularidades=titularidades)


@app.route('/entrenadores/<string:ano>')
def entrenadores(ano):
	entero = int(ano)
	temp = str(entero+1)
	fec_min = seleccionar_fecha_minima(ano)
	fec_max = seleccionar_fecha_maxima(ano)
	query_entrenadores = db.session.execute(query_seleccionar_entrenadores , {"fec_min": fec_min,"fec_max": fec_max})
	entrenadores = [row for row in query_entrenadores]			
	return render_template('entrenadores.tpl',entrenadores=entrenadores , temporada_seleccionada = ano, temp=temp)

@app.route('/entrenadores/<string:ano>/<string:entrenador>')
def entrenador_concreto(ano,entrenador):
	entrenador_concreto = seleccionar_entrenador_concreto(ano,entrenador)
	entero = int(ano)
	temp = str(entero+1)	
	return render_template('entrenador_concreto.tpl', entrenador_concreto = entrenador_concreto , temporada_seleccionada = ano,temp=temp)

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
	return render_template('jornadas.tpl', temporada_seleccionada = ano ,jornada_seleccionada=jornada, temp=temp,jornadas = jornadas,num_jornadas=num_jornadas)

@app.route('/jornadas/<string:jornada>/<string:ano>/<string:partido>')
def partido(ano,jornada,partido):
	entero = int(ano)
	if not jornada:
		jornada= '1'
	temp = str(entero+1)
	partidos = desc_partidos(partido)
	info_partidos = info_partido(partido)
	return render_template('partidos.tpl', temporada_seleccionada = ano ,jornada_seleccionada=jornada, partidos=partidos,temp=temp,info_partidos=info_partidos)

@app.route('/jugadores/<string:ano>')
def jugadores(ano):	
	entero = int(ano)
	temp = str(entero+1)	
	jugadores = dame_la_lista_de_jugadores_del_ano(ano)

	return render_template('jugadores.tpl', temporada_seleccionada = ano,jugadores=jugadores,temp=temp)

@app.route('/jugadores/<string:ano>/<string:id_jugador>')
def jugador_concreto(ano,id_jugador):	
	entero = int(ano)
	temp = str(entero+1)	
	#nuevo_equipo = equipo.replace('%20', ' ')
	jugadores = jug_concreto(ano,id_jugador)
	return render_template('jugador_concreto.tpl', temporada_seleccionada = ano,jugadores=jugadores,temp=temp)

@app.route('/estadios/')
def estadios():
	estadios =  dame_los_estadios()
	return render_template('estadios.tpl',estadios=estadios)

@app.route('/informes/')
def informes():
	return render_template('informes.tpl')

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
	equipo = request.args.get('equipo')

	return { 'jugador':jugador, 'fecha':fecha, 'ano':ano ,'equipo':equipo
		, 	'puntuaciones_rivales' : puntuaciones_rivales(jugador,fecha,ano,equipo)
		, 	'puntuaciones_rivales_media' : puntuaciones_rivales_media(jugador,fecha,ano,equipo)
		,	'puntuaciones_hora_partido' : puntuaciones_hora(jugador,fecha,ano,equipo)
		,	'puntuaciones_estacion_ano' : puntuaciones_estacion_ano(jugador,fecha,ano,equipo)
		,	'puntuaciones_info_global' : info_global(jugador,fecha,ano,equipo)
		,	'puntuaciones_temperatura' : puntuaciones_temperatura(jugador,fecha,ano,equipo)
		,	'puntuaciones_lluvias' : puntuaciones_lluvias(jugador,fecha,ano,equipo)
		,	'puntuaciones_humedad' : puntuaciones_humedad(jugador,fecha,ano,equipo)
		,	'puntuaciones_viento' : puntuaciones_velocidad_viento(jugador,fecha,ano,equipo)}


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

@app.route('/entrenador_completo')
def entrenador_completo():
	entrenador = request.args.get('nombre')
	equipo = request.args.get('equipo')
	ano = request.args.get('ano')

	return { 'entrenador':entrenador, 'equipo':equipo, 'ano':ano
		,	'puntuaciones_entrenador_global' : entrenador_global(entrenador,equipo,ano)
		,	'puntuaciones_entrenador_local' : entrenador_local(entrenador,equipo,ano)
		,	'puntuaciones_entrenador_visitante' : entrenador_visitante(entrenador,equipo,ano)				
		,	'puntuaciones_entrenador_estacion' : entrenador_estacion(entrenador,equipo,ano)
		,	'puntuaciones_entrenador_mejor' : entrenador_mejor(entrenador,equipo,ano)
		,	'puntuaciones_entrenador_peor' : entrenador_peor(entrenador,equipo,ano)
		}

@app.route('/informes/iteractivo_jugador/')
def informes_iteractivo_jugador():	
	anos_jugadores_a = {'2016': dame_jugadores('2016'), '2017': dame_jugadores('2017'),'todo': dame_jugadores('todo')}	
	anos_jugadores_b = {'2016': dame_jugadores('2016'), '2017': dame_jugadores('2017'),'todo': dame_jugadores('todo')}	
	return render_template('informes_iteractivo_jugador.tpl',anos_jugadores_select_a=anos_jugadores_a,anos_jugadores_select_b=anos_jugadores_b)

@app.route('/jugador_iteractivo')
def jugador_iteractivo():
	jugador = request.args.get('nombre')
	fecha = request.args.get('fecha')
	ano = request.args.get('ano')

	return { 'jugador':jugador, 'fecha':fecha, 'ano':ano}

@app.route('/informes/iteractivo_equipo/')
def informes_iteractivo_equipo():		
	return render_template('informes_iteractivo_equipo.tpl')

@app.route('/informes/iteractivo_entrenador/')
def informes_iteractivo_entrenador():		
	return render_template('informes_iteractivo_entrenador.tpl')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=80,debug= True)

