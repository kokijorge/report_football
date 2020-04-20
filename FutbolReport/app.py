from flask import Flask,render_template,request ,redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__ ,static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/prueba1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#sesion
app.secret_key = 'mysecretkey'
ano ='2017'

@app.route('/')
def index():	
	return redirect('2016')

@app.route('/equipos/<string:id>')
def equipos(id):
	data = db.session.execute(""" 
	select nombre, plantilla, edad, extranjeros, valor_total,
	ROW_NUMBER() OVER(    ORDER BY nombre)
	from tfg.staging_equipo  where ano = :ano""" , {"ano": id})
	equipos = [row for row in data]
	entero = int(id)
	temp = str(entero+1)
	return render_template('equipos.html', equipos = equipos , temporada_seleccionada = id,temp=temp)

@app.route('/<int:id>')
def temporada(id):
	return render_template('base.tpl', temporada_seleccionada = id)

@app.route('/top/<string:id>')
def top(id):
	entero = int(id)
	temp = str(entero+1)
	if entero == 2016:
		ini = '179510'
		fin = '179889'
	if entero == 2017:
		ini = '214386'
		fin = '214765'
	puntuaciones = db.session.execute(""" 
	select nombre,sum(puntuacion),ROW_NUMBER() OVER(    ORDER BY sum(puntuacion) desc) 
	from tfg.dim_puntuacion where partido between (:ini) and (:fin)   
	group by nombre  FETCH FIRST 10 ROWS ONLY""" , {"ini": ini, "fin":fin})
	puntos = [row for row in puntuaciones]

	goles = db.session.execute(""" 
	select nombre,sum(goles),ROW_NUMBER() OVER(    ORDER BY sum(goles) desc)
	from tfg.staging_alineacion where partido between (:ini) and (:fin)   
	group by nombre  FETCH FIRST 10 ROWS ONLY""" , {"ini": ini, "fin":fin})
	goleadores = [row for row in goles]

	return render_template('top.html', puntos = puntos,goleadores=goleadores , temporada_seleccionada = id, temp=temp)


@app.route('/entrenadores/<string:id>')
def entrenadores(id):
	entero = int(id)
	temp = str(entero+1)
	if entero == 2016:
		ini = '179510'
		fin = '179889'
	if entero == 2017:
		ini = '214386'
		fin = '214765'
	query_entrenadores = db.session.execute(""" 
	select 
		equipo,entrenador,count(id_partido),
		(select jornada as jornada_desde from tfg.staging_jornada where id_partido = min(entrenadores.id_partido)),
		(select jornada as jornada_hasta from tfg.staging_jornada where id_partido = max(entrenadores.id_partido)),
		ROW_NUMBER() OVER(    ORDER BY equipo,(select jornada as jornada_desde from tfg.staging_jornada where id_partido = min(entrenadores.id_partido)) asc)
	from
		(select equipo_local as equipo ,entrenador_local as entrenador ,id_partido from  tfg.staging_entrenador
 		where id_partido between (:ini) and (:fin)
		UNION
		select equipo_visitante as equipo ,entrenador_visitante as entrenador,id_partido from  tfg.staging_entrenador
 		where id_partido between (:ini) and (:fin)
		) as entrenadores
	group by equipo,entrenador;
	""" , {"ini": ini, "fin":fin})
	entrenadores = [row for row in query_entrenadores]		
	
	return render_template('entrenadores.html',entrenadores=entrenadores , temporada_seleccionada = id, temp=temp)

@app.route('/jornadas/<string:jornada>/<string:id>')
def jornadas(id,jornada):
	entero = int(id)
	temp = str(entero+1)
	if entero == 2016:
		ini = '179510'
		fin = '179889'
	if entero == 2017:
		ini = '214386'
		fin = '214765'
	query_jornadas = db.session.execute(""" 
	select 
	ROW_NUMBER() OVER(    ORDER BY fecha,hora),
	equipo_local,resultado_local,equipo_visitante,resultado_visitante,fecha,hora
	from tfg.staging_jornada
	where id_partido between (:ini) and (:fin)
	and jornada = jornada;
	""" , {"ini": ini, "fin":fin , "jornada":jornada})
	jornadas = [row for row in query_jornadas]
	return render_template('jornadas.html', temporada_seleccionada = id ,jornada_seleccionada=jornada, temp=temp,jornadas = jornadas)

@app.route('/informes/<string:id>')
def informes(id):
	return render_template('informes.html', temporada_seleccionada = id)

@app.route('/jugadores/<string:id>')
def jugadores(id):
	return render_template('jugadores.html', temporada_seleccionada = id)

@app.route('/estadios/<string:id>')
def estadios(id):
	return render_template('estadios.html', temporada_seleccionada = id)

if __name__ == '__main__':
	app.run(port=8000,debug= True)