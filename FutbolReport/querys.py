def seleccionar_jugador_completo(ano):
    if ano  == '2016':
        query = """
            select nombre,TO_CHAR(fecha_nacimiento, 'YYYY-MM-DD'),posicion from dw.dim_jugador
            where id_jugador in (select id_jugador from dw.fact_jornada where id_partido <= '179889')             
            group by nombre,fecha_nacimiento,posicion
            order by 1;  
            """
        return query
    elif ano  == '2017':
        query = """
            select nombre,TO_CHAR(fecha_nacimiento, 'YYYY-MM-DD'),posicion from dw.dim_jugador
            where id_jugador in (select id_jugador from dw.fact_jornada where id_partido > '179889') 
            group by nombre,fecha_nacimiento,posicion
            order by 1;  
            """
        return query
    else: 
        query = """
            select nombre, TO_CHAR(fecha_nacimiento, 'YYYY-MM-DD'),posicion from dw.dim_jugador
            where id_jugador in (select id_jugador from dw.fact_jornada) 
            group by nombre,fecha_nacimiento,posicion
            order by 1;  
            """
        return query	


query_seleccionar_equipos_jugadores= """
select equi.nombre,ROW_NUMBER() OVER(    ORDER BY equi.nombre) from stg.stg_partido par
inner join stg.stg_equipo equi
on equi.id_equipo=par.id_equipo_local
where temporada = :ano
group by equi.nombre
""" 

query_seleccionar_equipos=""" 
	select ROW_NUMBER() OVER(    ORDER BY equi.nombre),equi.nombre,equi.ano_fundacion,est.ciudad
	from stg.stg_partido par
	inner join stg.stg_equipo equi
	on equi.id_equipo=par.id_equipo_local
	inner join stg.stg_estadio est
	on equi.id_equipo= est.id_equipo
	where temporada = :ano
	group by equi.nombre,equi.ano_fundacion,est.ciudad
	""" 

query_seleccionar_puntuaciones = """ 
	select jug.nombre,jug.nacionalidad,jug.posicion,sum(puntuacion),jug.id_jugador
	,ROW_NUMBER() OVER(    ORDER BY sum(puntuacion) desc) 
	from stg.stg_suceso suc
	inner join stg.stg_jugador jug on suc.id_jugador=jug.id_jugador
	inner join stg.stg_partido par on par.id_partido=suc.id_partido
	where par.temporada = :ano
	group by jug.nombre,jug.nacionalidad,jug.posicion,jug.id_jugador  FETCH FIRST 10 ROWS ONLY"""

query_seleccionar_goleadores = """ 
	select jug.nombre,jug.nacionalidad,jug.posicion,sum(goles),jug.id_jugador
	,ROW_NUMBER() OVER(    ORDER BY sum(goles) desc) 
	from stg.stg_suceso suc
	inner join stg.stg_jugador jug on suc.id_jugador=jug.id_jugador
	inner join stg.stg_partido par on par.id_partido=suc.id_partido
	where par.temporada = :ano
	group by jug.nombre,jug.nacionalidad,jug.posicion,jug.id_jugador  FETCH FIRST 10 ROWS ONLY"""

query_seleccionar_tarjeta_amarilla = """ 
	select jug.nombre,jug.nacionalidad,jug.posicion,sum(tarjeta_amarilla),jug.id_jugador
	,ROW_NUMBER() OVER(    ORDER BY sum(tarjeta_amarilla) desc) 
	from stg.stg_suceso suc
	inner join stg.stg_jugador jug on suc.id_jugador=jug.id_jugador
	inner join stg.stg_partido par on par.id_partido=suc.id_partido
	where par.temporada = :ano
	group by jug.nombre,jug.nacionalidad,jug.posicion,jug.id_jugador  FETCH FIRST 10 ROWS ONLY""" 

query_seleccionar_tarjeta_roja=""" 
	select jug.nombre,jug.nacionalidad,jug.posicion,sum(tarjeta_roja),jug.id_jugador
	,ROW_NUMBER() OVER(    ORDER BY sum(tarjeta_roja) desc) 
	from stg.stg_suceso suc
	inner join stg.stg_jugador jug on suc.id_jugador=jug.id_jugador
	inner join stg.stg_partido par on par.id_partido=suc.id_partido
	where par.temporada = :ano
	group by jug.nombre,jug.nacionalidad,jug.posicion,jug.id_jugador  FETCH FIRST 10 ROWS ONLY""" 


query_seleccionar_minutos_jugados = """ 
	select jug.nombre,jug.nacionalidad,jug.posicion,sum(minutos_jugados),jug.id_jugador
	,ROW_NUMBER() OVER(    ORDER BY sum(minutos_jugados) desc) 
	from stg.stg_suceso suc
	inner join stg.stg_jugador jug on suc.id_jugador=jug.id_jugador
	inner join stg.stg_partido par on par.id_partido=suc.id_partido
	where par.temporada = :ano
	group by jug.nombre,jug.nacionalidad,jug.posicion,jug.id_jugador  FETCH FIRST 10 ROWS ONLY"""

query_seleccionar_titularidades = """ 
	select jug.nombre,jug.nacionalidad,jug.posicion,count(minutos_jugados),jug.id_jugador
	,ROW_NUMBER() OVER(    ORDER BY count(minutos_jugados) desc) 
	from stg.stg_suceso suc
	inner join stg.stg_jugador jug on suc.id_jugador=jug.id_jugador
	inner join stg.stg_partido par on par.id_partido=suc.id_partido
	where par.temporada = :ano
    and suc.titular = 'SI'
	group by jug.nombre,jug.nacionalidad,jug.posicion,jug.id_jugador  FETCH FIRST 10 ROWS ONLY""" 

query_fecha_minima = """select min(fecha) from stg.stg_partido 	where temporada = :ano 	"""
 
query_fecha_maxima = """select max(fecha) from stg.stg_partido 	where temporada = :ano 	"""

query_seleccionar_entrenadores = """ 
	select ROW_NUMBER() OVER(    ORDER BY nombre),query.* from (
	select equ.nombre,ent.nombre as nombre_entre,ent.ano_debut,ent.fecha_nacimiento,ent.nacionalidad
	from stg.stg_lidera lid
	inner join stg.stg_equipo equ
	on equ.id_equipo=lid.id_equipo
	inner join stg.stg_entrenador ent
	on ent.id_entrenador=lid.id_entrenador
	where fecha_inicio_contrato between (:fec_min) and (:fec_max)
	UNION
	select equ.nombre,ent.nombre,ent.ano_debut,ent.fecha_nacimiento,ent.nacionalidad
	from stg.stg_lidera lid
	inner join stg.stg_equipo equ
	on equ.id_equipo=lid.id_equipo
	inner join stg.stg_entrenador ent
	on ent.id_entrenador=lid.id_entrenador
	where fecha_inicio_contrato < (:fec_min) 
	and fecha_fin_contrato is null) as query;
	"""

query_seleccionar_jornadas =    """ 
	select ROW_NUMBER() OVER(    ORDER BY par.fecha,par.hora),equ_loc.nombre,par.resultado_local,equ_vis.nombre,par.resultado_rival,par.fecha,par.hora
    from stg.stg_partido par
    inner join stg.stg_equipo equ_loc
    on par.id_equipo_local = equ_loc.id_equipo
    inner join stg.stg_equipo equ_vis
    on par.id_equipo_rival = equ_vis.id_equipo
    where temporada=  :ano  
	and jornada = :jornada;
	"""

query_seleccionar_num_jornadas =  """
	select 
	ROW_NUMBER() OVER(    ORDER BY jornada)
	from  stg.stg_partido
	where temporada= :ano  
    group by jornada order by jornada
	"""  

query_seleccionar_jugadores = """ 
	select ROW_NUMBER() OVER(    ORDER BY nombre),query.* from    
	(select jug.nombre,jug.fecha_nacimiento,jug.nacionalidad,jug.pie,jug.posicion,valor_mercado 
	,fecha_inicio_contrato,fecha_fin_contrato
	from stg.stg_milita mil
    inner join stg.stg_equipo equ on mil.id_equipo=equ.id_equipo
    inner join stg.stg_jugador jug on jug.id_jugador = mil.id_jugador
    where equ.nombre = :nuevo_equipo  
    and fecha_inicio_contrato between (:fec_min) and (:fec_max)
	UNION
	select jug.nombre,jug.fecha_nacimiento,jug.nacionalidad,jug.pie,jug.posicion,valor_mercado 
	,fecha_inicio_contrato,fecha_fin_contrato
	from stg.stg_milita mil
    inner join stg.stg_equipo equ on mil.id_equipo=equ.id_equipo
    inner join stg.stg_jugador jug on jug.id_jugador = mil.id_jugador
    where equ.nombre = :nuevo_equipo 
    and fecha_inicio_contrato < (:fec_min) 
    and fecha_fin_contrato is null) as query
	"""

query_seleccionar_estadios =  """ 
	select ROW_NUMBER() OVER(    ORDER BY equ.nombre),equ.nombre,est.estadio,est.ciudad,est.capacidad,est.coordenada_x,est.coordenada_y,
    regexp_replace(est.estadio, ' ', '_', 'g')
    from stg.stg_estadio est
    inner join stg.stg_equipo equ
    on est.id_equipo = equ.id_equipo
	"""

QUERY_A_LA_QUE_AUN_NO_LE_HAS_DADO_NOMBRE = """ 
		select sum(puntuacion),ent.nombre || ' ('|| equ.nombre||')'
        from dw.fact_jornada jor
        inner join dw.dim_equipo equ on equ.id_equipo=jor.id_equipo_rival
        inner join dw.dim_entrenador ent on ent.id_entrenador=jor.id_entrenador_rival
        where id_jugador=631
        and id_partido between ('179510') and ('179889')
        group by  equ.nombre,ent.nombre
        order by 1   
		"""
query_puntuaciones_hora_partido =""" 
WITH porcentajes AS (
        select 
    CASE
    WHEN sum(puntuacion) >= 0 THEN sum(puntuacion)
    ELSE 0
    END AS puntuacion
    ,hora_categoria
from dw.fact_jornada inner join dw.dim_fecha on fact_jornada.id_fecha=  dim_fecha.id_fecha
    inner join dw.dim_jugador jug on jug.id_jugador = fact_jornada.id_jugador
where jug.nombre = :nombre
and jug.fecha_nacimiento = :fecha
and fact_jornada.id_partido between (:id_ini) and (:id_fin)
group by hora_categoria
order by 1 desc
     )
SELECT
hora_categoria,
ROUND((sum(puntuacion)::numeric * 100 / (Select CASE     WHEN sum(puntuacion) = 0 THEN 1 ELSE sum(puntuacion)::numeric END AS puntuacion  from porcentajes))::numeric,2) as porcentaje          
FROM porcentajes
group by hora_categoria
;
"""
#TODO MARCIAL
query_puntuaciones_rivales =""" 
select *  from 
(select   dim_equipo.nombre ,puntuacion , dim_entrenador.nombre
from dw.fact_jornada inner join dw.dim_equipo on id_equipo_rival = dim_equipo.id_equipo
inner join dw.dim_entrenador on id_entrenador_rival=dim_entrenador.id_entrenador
inner join dw.dim_jugador jug on jug.id_jugador = fact_jornada.id_jugador
where jug.nombre = :nombre
and jug.fecha_nacimiento = :fecha
and fact_jornada.id_partido between (:id_ini) and (:id_fin)
order by 2 desc
FETCH FIRST 5 ROWS ONLY) as  a 
UNION ALL
select * from 
(select   dim_equipo.nombre ,puntuacion , dim_entrenador.nombre
from dw.fact_jornada inner join dw.dim_equipo on id_equipo_rival = dim_equipo.id_equipo
inner join dw.dim_entrenador on id_entrenador_rival=dim_entrenador.id_entrenador
inner join dw.dim_jugador jug on jug.id_jugador = fact_jornada.id_jugador
where jug.nombre = :nombre
and jug.fecha_nacimiento = :fecha
and fact_jornada.id_partido between (:id_ini) and (:id_fin)
order by 2 asc
FETCH FIRST 5 ROWS ONLY)as  b order by 2 desc
"""

query_estacion_ano =""" 
select estacion_ano,sum(puntuacion)
from dw.fact_jornada inner join dw.dim_fecha on fact_jornada.id_fecha=  dim_fecha.id_fecha
inner join dw.dim_jugador jug on jug.id_jugador = fact_jornada.id_jugador
where jug.nombre = :nombre
and jug.fecha_nacimiento = :fecha
and fact_jornada.id_partido between (:id_ini) and (:id_fin)
group by estacion_ano
order by 1 desc;
"""

query_info_global =""" 
select jug.nombre,dim_equipo.nombre equipo,
sum(puntuacion) as puntos ,sum(minutos_jugados) as minutos ,sum(goles) as goles ,sum(tarjeta_amarilla) as amarillas,sum(tarjeta_roja) as rojas ,
count(titular) as titularidades from dw.fact_jornada
inner join dw.dim_jugador jug on jug.id_jugador = fact_jornada.id_jugador
inner join dw.dim_equipo on fact_jornada.id_equipo_propio=dim_equipo.id_equipo
where jug.nombre = :nombre
and jug.fecha_nacimiento = :fecha
and fact_jornada.id_partido between (:id_ini) and (:id_fin)
group by jug.id_jugador,jug.nombre,dim_equipo.nombre;
"""



query_temperatura =""" 
select dim_meteo.temperatura_categoria,sum(puntuacion)
from dw.fact_jornada inner join dw.dim_meteo on fact_jornada.id_meteo=dim_meteo.id_meteo
inner join dw.dim_jugador jug on jug.id_jugador = fact_jornada.id_jugador
where jug.nombre = :nombre
and jug.fecha_nacimiento = :fecha
and fact_jornada.id_partido between (:id_ini) and (:id_fin)
group by temperatura_categoria
order by 2 desc;
"""

query_lluvias =""" 
select dim_meteo.lluvias_categoria,sum(puntuacion)
from dw.fact_jornada inner join dw.dim_meteo on fact_jornada.id_meteo=dim_meteo.id_meteo
inner join dw.dim_jugador jug on jug.id_jugador = fact_jornada.id_jugador
where jug.nombre = :nombre
and jug.fecha_nacimiento = :fecha
and fact_jornada.id_partido between (:id_ini) and (:id_fin)
group by lluvias_categoria
order by 2 desc;
"""

query_humedad =""" 
select dim_meteo.humedad_categoria,sum(puntuacion)
from dw.fact_jornada inner join dw.dim_meteo on fact_jornada.id_meteo=dim_meteo.id_meteo
inner join dw.dim_jugador jug on jug.id_jugador = fact_jornada.id_jugador
where jug.nombre = :nombre
and jug.fecha_nacimiento = :fecha
and fact_jornada.id_partido between (:id_ini) and (:id_fin)
group by humedad_categoria
order by 2 desc;
"""