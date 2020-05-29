import os 
from flask import Flask,render_template,request ,redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from querys import *

app = Flask(__name__ ,static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI","postgresql://postgres:postgres@localhost:5432/futbol_report")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#sesion
app.secret_key = 'mysecretkey'

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
	fec_min = seleccionar_fecha_minima(ano)
	fec_max = seleccionar_fecha_maxima(ano)
	query_jug = db.session.execute(query_seleccionar_jugadores , {"fec_min": fec_min,"fec_max": fec_max, "nuevo_equipo":nuevo_equipo})
	jugadores =  [row for row in query_jug]
	return render_template('jugadores.tpl', temporada_seleccionada = ano,equipos_jugadores=equipos_jugadores,jugadores=jugadores,temp=temp,nuevo_equipo=nuevo_equipo)

@app.route('/estadios/<string:ano>')
def estadios(ano):
	equipos_jugadores = seleccionar_equipos(ano)
	query_estadio = db.session.execute(query_seleccionar_estadios)
	estadios =  [row for row in query_estadio]
	return render_template('estadios.tpl', temporada_seleccionada = ano,equipos_jugadores=equipos_jugadores,estadios=estadios)

@app.route('/informes/<string:ano>')
def informes(ano):
	equipos_jugadores = seleccionar_equipos(ano)
	return render_template('informes.tpl', temporada_seleccionada = ano,equipos_jugadores=equipos_jugadores)

@app.route('/informes/<string:tipo>/<string:ano>')
def informes_tipo(tipo,ano):
	equipos_jugadores = seleccionar_equipos(ano)
	if tipo  == 'rival' or tipo == 'tiempo' or tipo == 'completo_jugador':
		query_rival = db.session.execute(""" 
		select sum(puntuacion),ent.nombre || ' ('|| equ.nombre||')'
        from dw.fact_jornada jor
        inner join dw.dim_equipo equ on equ.id_equipo=jor.id_equipo_rival
        inner join dw.dim_entrenador ent on ent.id_entrenador=jor.id_entrenador_rival
        where id_jugador=631
        and id_partido between ('179510') and ('179889')
        group by  equ.nombre,ent.nombre
        order by 1   
		""")
		rivales =   [row for row in query_rival]
		lista_rivales = ",".join(["['"+rival[1]+"',"+str(rival[0])+"]" for rival in rivales])
		return render_template('informes_'+tipo+'.tpl', temporada_seleccionada = ano,equipos_jugadores=equipos_jugadores,tipo=tipo,lista_rivales=lista_rivales)
	else:
		return render_template('informes_'+tipo+'.tpl', temporada_seleccionada = ano,equipos_jugadores=equipos_jugadores,tipo=tipo)
#	elif test expression:
#    	Body of elif
#	else: 
#    	Body of else

@app.route('/informes/completo_jugador')
def informes_completo_jugador():
	query_jugador_completo = db.session.execute(seleccionar_jugador_completo('2016'))
	jugadores =   [row for row in query_jugador_completo]		
	return render_template('informes_completo_jugador.tpl',jugadores = jugadores)


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8000,debug= True)