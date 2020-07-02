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

def seleccionar_equipo_completo(ano):
    if ano  == '2016':
        query = """
            select nombre from dw.dim_equipo
			where id_equipo in (select id_equipo_propio from dw.fact_jornada where id_partido <= '179889')                         
			order by 1;   
            """
        return query
    elif ano  == '2017':
        query = """            
			select nombre from dw.dim_equipo
			where id_equipo in (select id_equipo_propio from dw.fact_jornada where id_partido > '179889')                         
			order by 1; 
            """
        return query
    else: 
        query = """
            select nombre from dw.dim_equipo
			where id_equipo in (select id_equipo_propio from dw.fact_jornada)                         
			order by 1;  
            """
        return query

def seleccionar_entrenador_completo(ano):
    if ano  == '2016':
        query = """
            select dim_entrenador.nombre,dim_equipo.nombre as equipo from dw.dim_entrenador
            inner join dw.fact_jornada on fact_jornada.id_entrenador_propio= id_entrenador
            inner join dw.dim_equipo on id_equipo_propio= id_equipo
            where id_partido <= '179889'    
            group by dim_entrenador.nombre,dim_equipo.nombre
            order by 1;   
            """
        return query
    elif ano  == '2017':
        query = """
			select dim_entrenador.nombre,dim_equipo.nombre as equipo from dw.dim_entrenador
            inner join dw.fact_jornada on fact_jornada.id_entrenador_propio= id_entrenador
            inner join dw.dim_equipo on id_equipo_propio= id_equipo
            where id_partido > '179889' 
            group by dim_entrenador.nombre,dim_equipo.nombre
            order by 1;        			
            """
        return query
    else: 
        query = """
			select dim_entrenador.nombre,dim_equipo.nombre as equipo from dw.dim_entrenador
            inner join dw.fact_jornada on fact_jornada.id_entrenador_propio= id_entrenador
            inner join dw.dim_equipo on id_equipo_propio= id_equipo            
            group by dim_entrenador.nombre,dim_equipo.nombre
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
query_puntuaciones_rivales =""" 
select *  from 
(select   dim_equipo.nombre ,puntuacion  , 'puntuacion : '  || puntuacion  || ' || ' || 'entrenador : '  || dim_entrenador.nombre
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
(select   dim_equipo.nombre ,puntuacion  , 'puntuacion : '  || puntuacion  || ' || ' || 'entrenador : '  || dim_entrenador.nombre
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

query_viento =""" 
select dim_meteo.velocidad_viento_categoria,sum(puntuacion)
from dw.fact_jornada inner join dw.dim_meteo on fact_jornada.id_meteo=dim_meteo.id_meteo
inner join dw.dim_jugador jug on jug.id_jugador = fact_jornada.id_jugador
where jug.nombre = :nombre
and jug.fecha_nacimiento = :fecha
and fact_jornada.id_partido between (:id_ini) and (:id_fin)
group by velocidad_viento_categoria
order by 2 desc;
"""

query_equipo_global =""" 
WITH partidos AS (
        select id_partido,id_fecha,id_estadio,id_meteo,equipo_local.nombre as equipo_local,equipo_visitante.nombre as equipo_visitante , id_entrenador_propio,id_entrenador_rival,
resultado_propio as resultado_local,resultado_rival as resultado_rival,
CASE
    WHEN resultado_propio = resultado_rival THEN 1
    WHEN equipo_local.nombre = :nombre and resultado_propio > resultado_rival THEN 3
    WHEN equipo_visitante.nombre = :nombre and resultado_rival > resultado_propio THEN 3
    ELSE 0
END as puntos ,
CASE    
    WHEN equipo_local.nombre = :nombre THEN resultado_propio
    WHEN equipo_visitante.nombre = :nombre then resultado_rival 
    ELSE 0
END as goles_favor      ,
CASE    
    WHEN equipo_local.nombre <> :nombre THEN resultado_propio
    WHEN equipo_visitante.nombre <> :nombre then resultado_rival 
    ELSE 0
END as goles_contra     
from dw.fact_jornada
inner join dw.dim_equipo as equipo_local
on equipo_local.id_equipo = fact_jornada.id_equipo_propio
inner join dw.dim_equipo as equipo_visitante
on equipo_visitante.id_equipo = fact_jornada.id_equipo_rival
where es_local = 'SI'    
    and id_partido between (:id_ini) and (:id_fin)
    and (equipo_local.nombre= :nombre or equipo_visitante.nombre= :nombre )
group by 
id_partido,id_fecha,id_estadio,id_meteo,equipo_local.nombre,equipo_visitante.nombre, id_entrenador_propio,id_entrenador_rival,resultado_propio,resultado_rival
order by 1)
select  (select count(*) from partidos where puntos=1) as empates,
(select count(*) from partidos where puntos=3) as victorias,
(select count(*) from partidos where puntos=0) as derrotas, 
sum(goles_favor) as goles_favor,  
sum(goles_contra)  as goles_contra,
sum (puntos) puntos
from partidos 
"""

query_equipo_local =""" 
WITH partidos AS (
        select id_partido,id_fecha,id_estadio,id_meteo,equipo_local.nombre as equipo_local,equipo_visitante.nombre as equipo_visitante , id_entrenador_propio,id_entrenador_rival,
resultado_propio as resultado_local,resultado_rival as resultado_rival,
CASE
    WHEN resultado_propio = resultado_rival THEN 1
    WHEN equipo_local.nombre = :nombre and resultado_propio > resultado_rival THEN 3
    WHEN equipo_visitante.nombre = :nombre and resultado_rival > resultado_propio THEN 3
    ELSE 0
END as puntos ,
CASE    
    WHEN equipo_local.nombre = :nombre THEN resultado_propio
    WHEN equipo_visitante.nombre = :nombre then resultado_rival 
    ELSE 0
END as goles_favor      ,
CASE    
    WHEN equipo_local.nombre <> :nombre THEN resultado_propio
    WHEN equipo_visitante.nombre <> :nombre then resultado_rival 
    ELSE 0
END as goles_contra     
from dw.fact_jornada
inner join dw.dim_equipo as equipo_local
on equipo_local.id_equipo = fact_jornada.id_equipo_propio
inner join dw.dim_equipo as equipo_visitante
on equipo_visitante.id_equipo = fact_jornada.id_equipo_rival
where es_local = 'SI'    
    and id_partido between (:id_ini) and (:id_fin)
    and equipo_local.nombre= :nombre  
group by 
id_partido,id_fecha,id_estadio,id_meteo,equipo_local.nombre,equipo_visitante.nombre, id_entrenador_propio,id_entrenador_rival,resultado_propio,resultado_rival
order by 1)
select  (select count(*) from partidos where puntos=1) as empates,
(select count(*) from partidos where puntos=3) as victorias,
(select count(*) from partidos where puntos=0) as derrotas, 
sum(goles_favor) as goles_favor,  
sum(goles_contra)  as goles_contra,
sum (puntos) puntos
from partidos 
"""

query_equipo_visitante =""" 
WITH partidos AS (
        select id_partido,id_fecha,id_estadio,id_meteo,equipo_local.nombre as equipo_local,equipo_visitante.nombre as equipo_visitante , id_entrenador_propio,id_entrenador_rival,
resultado_propio as resultado_local,resultado_rival as resultado_rival,
CASE
    WHEN resultado_propio = resultado_rival THEN 1
    WHEN equipo_local.nombre = :nombre and resultado_propio > resultado_rival THEN 3
    WHEN equipo_visitante.nombre = :nombre and resultado_rival > resultado_propio THEN 3
    ELSE 0
END as puntos ,
CASE    
    WHEN equipo_local.nombre = :nombre THEN resultado_propio
    WHEN equipo_visitante.nombre = :nombre then resultado_rival 
    ELSE 0
END as goles_favor      ,
CASE    
    WHEN equipo_local.nombre <> :nombre THEN resultado_propio
    WHEN equipo_visitante.nombre <> :nombre then resultado_rival 
    ELSE 0
END as goles_contra     
from dw.fact_jornada
inner join dw.dim_equipo as equipo_local
on equipo_local.id_equipo = fact_jornada.id_equipo_propio
inner join dw.dim_equipo as equipo_visitante
on equipo_visitante.id_equipo = fact_jornada.id_equipo_rival
where es_local = 'SI'    
    and id_partido between (:id_ini) and (:id_fin)
    and equipo_visitante.nombre= :nombre  
group by 
id_partido,id_fecha,id_estadio,id_meteo,equipo_local.nombre,equipo_visitante.nombre, id_entrenador_propio,id_entrenador_rival,resultado_propio,resultado_rival
order by 1)
select  (select count(*) from partidos where puntos=1) as empates,
(select count(*) from partidos where puntos=3) as victorias,
(select count(*) from partidos where puntos=0) as derrotas, 
sum(goles_favor) as goles_favor,  
sum(goles_contra)  as goles_contra,
sum (puntos) puntos
from partidos 
"""

query_equipo_estacion =""" 
WITH partidos AS (
        select id_partido,fact_jornada.id_fecha,id_estadio,id_meteo,equipo_local.nombre as equipo_local,equipo_visitante.nombre as equipo_visitante , id_entrenador_propio,id_entrenador_rival,
resultado_propio as resultado_local,resultado_rival as resultado_rival,
CASE
    WHEN resultado_propio = resultado_rival THEN 1
    WHEN equipo_local.nombre = :nombre   and resultado_propio > resultado_rival THEN 3
    WHEN equipo_visitante.nombre = :nombre   and resultado_rival > resultado_propio THEN 3
    ELSE 0
END as puntos ,
CASE    
    WHEN equipo_local.nombre = :nombre   THEN resultado_propio
    WHEN equipo_visitante.nombre = :nombre   then resultado_rival 
    ELSE 0
END as goles_favor      ,
CASE    
    WHEN equipo_local.nombre <> :nombre   THEN resultado_propio
    WHEN equipo_visitante.nombre <> :nombre   then resultado_rival 
    ELSE 0
END as goles_contra   ,
    estacion_ano
from dw.fact_jornada
inner join dw.dim_equipo as equipo_local
on equipo_local.id_equipo = fact_jornada.id_equipo_propio
inner join dw.dim_equipo as equipo_visitante
on equipo_visitante.id_equipo = fact_jornada.id_equipo_rival
    inner join dw.dim_fecha on fact_jornada.id_fecha=  dim_fecha.id_fecha
where es_local = 'SI'    
    and id_partido between (:id_ini) and (:id_fin)
    and (equipo_visitante.nombre= :nombre   or equipo_local.nombre= :nombre   )
group by 
id_partido,fact_jornada.id_fecha,id_estadio,id_meteo,equipo_local.nombre,equipo_visitante.nombre, id_entrenador_propio,id_entrenador_rival,resultado_propio,resultado_rival,estacion_ano
order by 1)
select  
estacion_ano,sum (puntos) puntos
from partidos group by estacion_ano
"""

query_equipo_mejor =""" 
WITH partidos AS (
        select id_partido,fact_jornada.id_fecha,id_estadio,id_meteo,equipo_local.nombre as equipo_local,equipo_visitante.nombre as equipo_visitante , id_entrenador_propio,id_entrenador_rival,
resultado_propio as resultado_local,resultado_rival as resultado_rival,
CASE
    WHEN resultado_propio = resultado_rival THEN 1
    WHEN equipo_local.nombre = :nombre and resultado_propio > resultado_rival THEN 3
    WHEN equipo_visitante.nombre = :nombre and resultado_rival > resultado_propio THEN 3
    ELSE 0
END as puntos ,
CASE    
    WHEN equipo_local.nombre = :nombre THEN resultado_propio
    WHEN equipo_visitante.nombre = :nombre then resultado_rival 
    ELSE 0
END as goles_favor      ,
CASE    
    WHEN equipo_local.nombre <> :nombre THEN resultado_propio
    WHEN equipo_visitante.nombre <> :nombre then resultado_rival 
    ELSE 0
END as goles_contra   ,
    estacion_ano
from dw.fact_jornada
inner join dw.dim_equipo as equipo_local
on equipo_local.id_equipo = fact_jornada.id_equipo_propio
inner join dw.dim_equipo as equipo_visitante
on equipo_visitante.id_equipo = fact_jornada.id_equipo_rival
    inner join dw.dim_fecha on fact_jornada.id_fecha=  dim_fecha.id_fecha
where es_local = 'SI'    
   and id_partido between (:id_ini) and (:id_fin)
    and (equipo_visitante.nombre= :nombre or equipo_local.nombre= :nombre )
group by 
id_partido,fact_jornada.id_fecha,id_estadio,id_meteo,equipo_local.nombre,equipo_visitante.nombre, id_entrenador_propio,id_entrenador_rival,resultado_propio,resultado_rival,estacion_ano
order by 1)
select  
CASE
    WHEN equipo_local = :nombre THEN equipo_visitante    
    ELSE equipo_local
END AS equipo ,goles_favor
from 
partidos
order by goles_favor desc FETCH FIRST 5 ROWS ONLY
"""

query_equipo_peor =""" 
WITH partidos AS (
        select id_partido,fact_jornada.id_fecha,id_estadio,id_meteo,equipo_local.nombre as equipo_local,equipo_visitante.nombre as equipo_visitante , id_entrenador_propio,id_entrenador_rival,
resultado_propio as resultado_local,resultado_rival as resultado_rival,
CASE
    WHEN resultado_propio = resultado_rival THEN 1
    WHEN equipo_local.nombre = :nombre and resultado_propio > resultado_rival THEN 3
    WHEN equipo_visitante.nombre = :nombre and resultado_rival > resultado_propio THEN 3
    ELSE 0
END as puntos ,
CASE    
    WHEN equipo_local.nombre = :nombre THEN resultado_propio
    WHEN equipo_visitante.nombre = :nombre then resultado_rival 
    ELSE 0
END as goles_favor      ,
CASE    
    WHEN equipo_local.nombre <> :nombre THEN resultado_propio
    WHEN equipo_visitante.nombre <> :nombre then resultado_rival 
    ELSE 0
END as goles_contra   ,
    estacion_ano
from dw.fact_jornada
inner join dw.dim_equipo as equipo_local
on equipo_local.id_equipo = fact_jornada.id_equipo_propio
inner join dw.dim_equipo as equipo_visitante
on equipo_visitante.id_equipo = fact_jornada.id_equipo_rival
    inner join dw.dim_fecha on fact_jornada.id_fecha=  dim_fecha.id_fecha
where es_local = 'SI'    
   and id_partido between (:id_ini) and (:id_fin)
    and (equipo_visitante.nombre= :nombre or equipo_local.nombre= :nombre )
group by 
id_partido,fact_jornada.id_fecha,id_estadio,id_meteo,equipo_local.nombre,equipo_visitante.nombre, id_entrenador_propio,id_entrenador_rival,resultado_propio,resultado_rival,estacion_ano
order by 1)
select  
CASE
    WHEN equipo_local = :nombre THEN equipo_visitante    
    ELSE equipo_local
END AS equipo ,goles_contra
from 
partidos
order by goles_contra desc FETCH FIRST 5 ROWS ONLY
"""

query_entrenador_global =""" 
WITH partidos as(select id_partido,id_fecha,id_estadio,equipo_local.nombre equipo_local,equipo_visitante.nombre equipo_visitante
,entrenador_local.nombre entrenador_local,entrenador_rival.nombre entrenador_visitante,resultado_propio as resultado_local,resultado_rival as resultado_rival,
CASE
WHEN resultado_propio = resultado_rival THEN 1
WHEN resultado_propio > resultado_rival THEN 3
ELSE 0
END as puntos,
resultado_propio as goles_favor, resultado_rival as goles_contra 
from dw.fact_jornada
inner join dw.dim_equipo as equipo_local
on equipo_local.id_equipo = fact_jornada.id_equipo_propio
inner join dw.dim_equipo as equipo_visitante
on equipo_visitante.id_equipo = fact_jornada.id_equipo_rival
inner join dw.dim_entrenador entrenador_local on fact_jornada.id_entrenador_propio= entrenador_local.id_entrenador
inner join dw.dim_entrenador entrenador_rival on fact_jornada.id_entrenador_rival= entrenador_rival.id_entrenador
where id_partido between (:id_ini) and (:id_fin)
and es_local = 'SI'
and entrenador_local.nombre = :nombre
and equipo_local.nombre = :equipo
group by id_partido,id_fecha,id_estadio,equipo_local.nombre,equipo_visitante.nombre,entrenador_local.nombre,entrenador_rival.nombre,resultado_propio,resultado_rival
UNION ALL
select id_partido,id_fecha,id_estadio,equipo_local.nombre equipo_local,equipo_visitante.nombre equipo_visitante
,entrenador_local.nombre entrenador_local,entrenador_rival.nombre entrenador_visitante,resultado_propio as resultado_local,resultado_rival as resultado_rival,
CASE
WHEN resultado_propio = resultado_rival THEN 1
WHEN resultado_rival > resultado_propio THEN 3
ELSE 0
END as puntos,
resultado_rival as goles_favor, resultado_propio as goles_contra  
from dw.fact_jornada
inner join dw.dim_equipo as equipo_local
on equipo_local.id_equipo = fact_jornada.id_equipo_propio
inner join dw.dim_equipo as equipo_visitante
on equipo_visitante.id_equipo = fact_jornada.id_equipo_rival
inner join dw.dim_entrenador entrenador_local on fact_jornada.id_entrenador_propio= entrenador_local.id_entrenador
inner join dw.dim_entrenador entrenador_rival on fact_jornada.id_entrenador_rival= entrenador_rival.id_entrenador
where id_partido between (:id_ini) and (:id_fin)
and es_local = 'SI'
and entrenador_rival.nombre = :nombre
and equipo_visitante.nombre = :equipo
group by id_partido,id_fecha,id_estadio,equipo_local.nombre,equipo_visitante.nombre,entrenador_local.nombre,entrenador_rival.nombre,resultado_propio,resultado_rival
order by 1)
select  (select count(*) from partidos where puntos=1) as empates,
(select count(*) from partidos where puntos=3) as victorias,
(select count(*) from partidos where puntos=0) as derrotas, 
sum(goles_favor) as goles_favor,  
sum(goles_contra)  as goles_contra,
sum (puntos) puntos
from partidos
"""
query_entrenador_local =""" 
WITH partidos as(select id_partido,id_fecha,id_estadio,equipo_local.nombre equipo_local,equipo_visitante.nombre equipo_visitante
,entrenador_local.nombre entrenador_local,entrenador_rival.nombre entrenador_visitante,resultado_propio as resultado_local,resultado_rival as resultado_rival,
CASE
WHEN resultado_propio = resultado_rival THEN 1
WHEN resultado_propio > resultado_rival THEN 3
ELSE 0
END as puntos,
resultado_propio as goles_favor, resultado_rival as goles_contra 
from dw.fact_jornada
inner join dw.dim_equipo as equipo_local
on equipo_local.id_equipo = fact_jornada.id_equipo_propio
inner join dw.dim_equipo as equipo_visitante
on equipo_visitante.id_equipo = fact_jornada.id_equipo_rival
inner join dw.dim_entrenador entrenador_local on fact_jornada.id_entrenador_propio= entrenador_local.id_entrenador
inner join dw.dim_entrenador entrenador_rival on fact_jornada.id_entrenador_rival= entrenador_rival.id_entrenador
where id_partido between (:id_ini) and (:id_fin)
and es_local = 'SI'
and entrenador_local.nombre = :nombre
and equipo_local.nombre = :equipo
group by id_partido,id_fecha,id_estadio,equipo_local.nombre,equipo_visitante.nombre,entrenador_local.nombre,entrenador_rival.nombre,resultado_propio,resultado_rival
order by 1)
select  (select count(*) from partidos where puntos=1) as empates,
(select count(*) from partidos where puntos=3) as victorias,
(select count(*) from partidos where puntos=0) as derrotas, 
sum(goles_favor) as goles_favor,  
sum(goles_contra)  as goles_contra,
sum (puntos) puntos
from partidos 
"""

query_entrenador_visitante =""" 
WITH partidos as(
select id_partido,id_fecha,id_estadio,equipo_local.nombre equipo_local,equipo_visitante.nombre equipo_visitante
,entrenador_local.nombre entrenador_local,entrenador_rival.nombre entrenador_visitante,resultado_propio as resultado_local,resultado_rival as resultado_rival,
CASE
WHEN resultado_propio = resultado_rival THEN 1
WHEN resultado_rival > resultado_propio THEN 3
ELSE 0
END as puntos,
resultado_rival as goles_favor, resultado_propio as goles_contra  
from dw.fact_jornada
inner join dw.dim_equipo as equipo_local
on equipo_local.id_equipo = fact_jornada.id_equipo_propio
inner join dw.dim_equipo as equipo_visitante
on equipo_visitante.id_equipo = fact_jornada.id_equipo_rival
inner join dw.dim_entrenador entrenador_local on fact_jornada.id_entrenador_propio= entrenador_local.id_entrenador
inner join dw.dim_entrenador entrenador_rival on fact_jornada.id_entrenador_rival= entrenador_rival.id_entrenador
where id_partido between (:id_ini) and (:id_fin)
and es_local = 'SI'
and entrenador_rival.nombre = :nombre
and equipo_visitante.nombre = :equipo
group by id_partido,id_fecha,id_estadio,equipo_local.nombre,equipo_visitante.nombre,entrenador_local.nombre,entrenador_rival.nombre,resultado_propio,resultado_rival
order by 1)
select  (select count(*) from partidos where puntos=1) as empates,
(select count(*) from partidos where puntos=3) as victorias,
(select count(*) from partidos where puntos=0) as derrotas, 
sum(goles_favor) as goles_favor,  
sum(goles_contra)  as goles_contra,
sum (puntos) puntos
from partidos 
"""

query_entrenador_estacion =""" 
WITH partidos as(select id_partido,fact_jornada.id_fecha,id_estadio,equipo_local.nombre equipo_local,equipo_visitante.nombre equipo_visitante
,entrenador_local.nombre entrenador_local,entrenador_rival.nombre entrenador_visitante,resultado_propio as resultado_local,resultado_rival as resultado_rival,
CASE
WHEN resultado_propio = resultado_rival THEN 1
WHEN resultado_propio > resultado_rival THEN 3
ELSE 0
END as puntos,
resultado_propio as goles_favor, resultado_rival as goles_contra ,estacion_ano
from dw.fact_jornada
inner join dw.dim_equipo as equipo_local
on equipo_local.id_equipo = fact_jornada.id_equipo_propio
inner join dw.dim_equipo as equipo_visitante
on equipo_visitante.id_equipo = fact_jornada.id_equipo_rival
inner join dw.dim_entrenador entrenador_local on fact_jornada.id_entrenador_propio= entrenador_local.id_entrenador
inner join dw.dim_entrenador entrenador_rival on fact_jornada.id_entrenador_rival= entrenador_rival.id_entrenador
inner join dw.dim_fecha on fact_jornada.id_fecha=  dim_fecha.id_fecha
where id_partido between (:id_ini) and (:id_fin)
and es_local = 'SI'
and entrenador_local.nombre = :nombre
and equipo_local.nombre = :equipo
group by id_partido,fact_jornada.id_fecha,id_estadio,equipo_local.nombre,equipo_visitante.nombre,entrenador_local.nombre,entrenador_rival.nombre,resultado_propio,resultado_rival,estacion_ano
UNION ALL
select id_partido,fact_jornada.id_fecha,id_estadio,equipo_local.nombre equipo_local,equipo_visitante.nombre equipo_visitante
,entrenador_local.nombre entrenador_local,entrenador_rival.nombre entrenador_visitante,resultado_propio as resultado_local,resultado_rival as resultado_rival,
CASE
WHEN resultado_propio = resultado_rival THEN 1
WHEN resultado_rival > resultado_propio THEN 3
ELSE 0
END as puntos,
resultado_rival as goles_favor, resultado_propio as goles_contra ,estacion_ano 
from dw.fact_jornada
inner join dw.dim_equipo as equipo_local
on equipo_local.id_equipo = fact_jornada.id_equipo_propio
inner join dw.dim_equipo as equipo_visitante
on equipo_visitante.id_equipo = fact_jornada.id_equipo_rival
inner join dw.dim_entrenador entrenador_local on fact_jornada.id_entrenador_propio= entrenador_local.id_entrenador
inner join dw.dim_entrenador entrenador_rival on fact_jornada.id_entrenador_rival= entrenador_rival.id_entrenador
inner join dw.dim_fecha on fact_jornada.id_fecha=  dim_fecha.id_fecha
where id_partido between (:id_ini) and (:id_fin)
and es_local = 'SI'
and entrenador_rival.nombre = :nombre
and equipo_visitante.nombre = :equipo
group by id_partido,fact_jornada.id_fecha,id_estadio,equipo_local.nombre,equipo_visitante.nombre,entrenador_local.nombre,entrenador_rival.nombre,resultado_propio,resultado_rival,estacion_ano
order by 1)
select  
estacion_ano,sum (puntos) puntos
from partidos group by estacion_ano
"""