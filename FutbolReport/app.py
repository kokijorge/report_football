from flask import Flask,render_template,request ,redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__ ,static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/futbol_report"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#sesion
app.secret_key = 'mysecretkey'

def seleccionar_equipos(ano):
	data = db.session.execute("""
	select equi.nombre,ROW_NUMBER() OVER(    ORDER BY equi.nombre) from stg.stg_partido par
	inner join stg.stg_equipo equi
	on equi.id_equipo=par.id_equipo_local
	where temporada = :ano
	group by equi.nombre
	""" , {"ano": ano})
	equipos = [row for row in data]
	return  equipos

@app.route('/')
def index():	
	return redirect('2016')

@app.route('/equipos/<string:ano>')
def equipos(ano):
	data = db.session.execute(""" 
	select ROW_NUMBER() OVER(    ORDER BY equi.nombre),equi.nombre,equi.ano_fundacion,est.ciudad
	from stg.stg_partido par
	inner join stg.stg_equipo equi
	on equi.id_equipo=par.id_equipo_local
	inner join stg.stg_estadio est
	on equi.id_equipo= est.id_equipo
	where temporada = :ano
	group by equi.nombre,equi.ano_fundacion,est.ciudad
	""" , {"ano": ano})
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
	puntuaciones = db.session.execute(""" 
	select jug.nombre,jug.nacionalidad,jug.posicion,sum(puntuacion),jug.id_jugador
	,ROW_NUMBER() OVER(    ORDER BY sum(puntuacion) desc) 
	from stg.stg_suceso suc
	inner join stg.stg_jugador jug on suc.id_jugador=jug.id_jugador
	inner join stg.stg_partido par on par.id_partido=suc.id_partido
	where par.temporada = :ano
	group by jug.nombre,jug.nacionalidad,jug.posicion,jug.id_jugador  FETCH FIRST 10 ROWS ONLY""" , {"ano": ano})
	puntos = [row for row in puntuaciones]
	equipos_jugadores = seleccionar_equipos(ano)
	goles = db.session.execute(""" 
	select jug.nombre,jug.nacionalidad,jug.posicion,sum(goles),jug.id_jugador
	,ROW_NUMBER() OVER(    ORDER BY sum(goles) desc) 
	from stg.stg_suceso suc
	inner join stg.stg_jugador jug on suc.id_jugador=jug.id_jugador
	inner join stg.stg_partido par on par.id_partido=suc.id_partido
	where par.temporada = :ano
	group by jug.nombre,jug.nacionalidad,jug.posicion,jug.id_jugador  FETCH FIRST 10 ROWS ONLY""" , {"ano": ano})
	goleadores = [row for row in goles]
	tarjeta_amarilla = db.session.execute(""" 
	select jug.nombre,jug.nacionalidad,jug.posicion,sum(tarjeta_amarilla),jug.id_jugador
	,ROW_NUMBER() OVER(    ORDER BY sum(tarjeta_amarilla) desc) 
	from stg.stg_suceso suc
	inner join stg.stg_jugador jug on suc.id_jugador=jug.id_jugador
	inner join stg.stg_partido par on par.id_partido=suc.id_partido
	where par.temporada = :ano
	group by jug.nombre,jug.nacionalidad,jug.posicion,jug.id_jugador  FETCH FIRST 10 ROWS ONLY""" , {"ano": ano})
	amarillas = [row for row in tarjeta_amarilla]
	tarjeta_roja = db.session.execute(""" 
	select jug.nombre,jug.nacionalidad,jug.posicion,sum(tarjeta_roja),jug.id_jugador
	,ROW_NUMBER() OVER(    ORDER BY sum(tarjeta_roja) desc) 
	from stg.stg_suceso suc
	inner join stg.stg_jugador jug on suc.id_jugador=jug.id_jugador
	inner join stg.stg_partido par on par.id_partido=suc.id_partido
	where par.temporada = :ano
	group by jug.nombre,jug.nacionalidad,jug.posicion,jug.id_jugador  FETCH FIRST 10 ROWS ONLY""" , {"ano": ano})
	rojas = [row for row in tarjeta_roja]
	jug_minutos = db.session.execute(""" 
	select jug.nombre,jug.nacionalidad,jug.posicion,sum(minutos_jugados),jug.id_jugador
	,ROW_NUMBER() OVER(    ORDER BY sum(minutos_jugados) desc) 
	from stg.stg_suceso suc
	inner join stg.stg_jugador jug on suc.id_jugador=jug.id_jugador
	inner join stg.stg_partido par on par.id_partido=suc.id_partido
	where par.temporada = :ano
	group by jug.nombre,jug.nacionalidad,jug.posicion,jug.id_jugador  FETCH FIRST 10 ROWS ONLY""" , {"ano": ano})
	minutos = [row for row in jug_minutos]
	jug_titularidades = db.session.execute(""" 
	select jug.nombre,jug.nacionalidad,jug.posicion,count(minutos_jugados),jug.id_jugador
	,ROW_NUMBER() OVER(    ORDER BY count(minutos_jugados) desc) 
	from stg.stg_suceso suc
	inner join stg.stg_jugador jug on suc.id_jugador=jug.id_jugador
	inner join stg.stg_partido par on par.id_partido=suc.id_partido
	where par.temporada = :ano
    and suc.titular = 'SI'
	group by jug.nombre,jug.nacionalidad,jug.posicion,jug.id_jugador  FETCH FIRST 10 ROWS ONLY""" , {"ano": ano})
	titularidades = [row for row in jug_titularidades]

	return render_template('top.tpl', puntos = puntos,goleadores=goleadores , temporada_seleccionada = ano, temp=temp,equipos_jugadores=equipos_jugadores,amarillas=amarillas,rojas=rojas,minutos=minutos,titularidades=titularidades)


@app.route('/entrenadores/<string:ano>')
def entrenadores(ano):
	entero = int(ano)
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
	equipos_jugadores = seleccionar_equipos(ano)
	return render_template('entrenadores.tpl',entrenadores=entrenadores , temporada_seleccionada = ano, temp=temp,equipos_jugadores=equipos_jugadores)

@app.route('/jornadas/<string:jornada>/<string:ano>')
def jornadas(ano,jornada):
	entero = int(ano)
	if not jornada:
		jornada= '1'
	temp = str(entero+1)
	query_jornadas = db.session.execute(""" 
	select ROW_NUMBER() OVER(    ORDER BY par.fecha,par.hora),equ_loc.nombre,par.resultado_local,equ_vis.nombre,par.resultado_rival,par.fecha,par.hora
    from stg.stg_partido par
    inner join stg.stg_equipo equ_loc
    on par.id_equipo_local = equ_loc.id_equipo
    inner join stg.stg_equipo equ_vis
    on par.id_equipo_rival = equ_vis.id_equipo
    where temporada=  :ano  
	and jornada = :jornada;
	""" , {"ano": ano , "jornada":jornada})
	jornadas = [row for row in query_jornadas]
	query_num = db.session.execute(""" 
	select 
	ROW_NUMBER() OVER(    ORDER BY jornada)
	from  stg.stg_partido
	where temporada= :ano  
    group by jornada order by jornada
	""" ,  {"ano": ano})
	num_jornadas = [row for row in query_num]
	equipos_jugadores = seleccionar_equipos(ano)
	return render_template('jornadas.tpl', temporada_seleccionada = ano ,jornada_seleccionada=jornada, temp=temp,jornadas = jornadas,num_jornadas=num_jornadas,equipos_jugadores=equipos_jugadores)


@app.route('/jugadores/<string:equipo>/<string:ano>')
def jugadores(ano,equipo):
	equipos_jugadores = seleccionar_equipos(ano)
	entero = int(ano)
	temp = str(entero+1)
	nuevo_equipo = equipo.replace('%20', ' ')
	query_fec_min = db.session.execute(""" 
	select min(fecha) from stg.stg_partido 	where temporada = :ano 	""" , {"ano": ano})
	query_fec_max = db.session.execute(""" 
	select max(fecha) from stg.stg_partido 	where temporada = :ano 	""" , {"ano": ano})
	fec_min =  [row for row in query_fec_min]
	fec_max =  [row for row in query_fec_max]
	query_jug = db.session.execute(""" 
	select ROW_NUMBER() OVER(    ORDER BY jug.nombre),jug.nombre,jug.fecha_nacimiento,jug.nacionalidad,jug.pie,jug.posicion,valor_mercado from stg.stg_milita mil
    inner join stg.stg_equipo equ on mil.id_equipo=equ.id_equipo
    inner join stg.stg_jugador jug on jug.id_jugador = mil.id_jugador
    where equ.nombre = :nuevo_equipo
    and fecha_inicio_contrato between (:fec_min) and (:fec_max)
	""" , {"fec_min": fec_min,"fec_max": fec_max, "nuevo_equipo":nuevo_equipo})
	jugadores =  [row for row in query_jug]
	return render_template('jugadores.tpl', temporada_seleccionada = ano,equipos_jugadores=equipos_jugadores,jugadores=jugadores,temp=temp,nuevo_equipo=nuevo_equipo)

@app.route('/estadios/<string:ano>')
def estadios(ano):
	equipos_jugadores = seleccionar_equipos(ano)
	query_estadio = db.session.execute(""" 
	select ROW_NUMBER() OVER(    ORDER BY equ.nombre),equ.nombre,est.estadio,est.ciudad,est.capacidad,est.coordenada_x,est.coordenada_y,
    regexp_replace(est.estadio, ' ', '_', 'g')
    from stg.stg_estadio est
    inner join stg.stg_equipo equ
    on est.id_equipo = equ.id_equipo
	""")
	estadios =  [row for row in query_estadio]
	return render_template('estadios.tpl', temporada_seleccionada = ano,equipos_jugadores=equipos_jugadores,estadios=estadios)

@app.route('/informes/<string:ano>')
def informes(ano):
	equipos_jugadores = seleccionar_equipos(ano)
	return render_template('informes.tpl', temporada_seleccionada = ano,equipos_jugadores=equipos_jugadores)

@app.route('/informes/<string:tipo>/<string:ano>')
def informes_tipo(tipo,ano):
	equipos_jugadores = seleccionar_equipos(ano)
	if tipo  == 'rival' or tipo == 'tiempo':
		query_rival = db.session.execute(""" 
		select sum(puntuacion), entrenador_rival  || ' ('|| equipo_rival||')' from
		(
		select punt.partido,punt.nombre,punt.puntuacion,
		CASE
			WHEN ent.equipo_local = 'Barcelona'  THEN ent.entrenador_visitante
			ELSE ent.entrenador_local
		END AS entrenador_rival,
		CASE
			WHEN ent.equipo_local = 'Barcelona'  THEN ent.equipo_visitante
			ELSE ent.equipo_local
		END AS equipo_rival
		from tfg.dim_puntuacion punt
		inner join tfg.staging_entrenador ent
		on ent.id_partido = punt.partido
		where punt.partido between ('179510') and ('179889')
		and nombre='Messi'
		) as tabla group by entrenador_rival,equipo_rival order by 1 desc
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

if __name__ == '__main__':
	app.run(port=8000,debug= True)