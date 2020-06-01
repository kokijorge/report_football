--QUERYS INFORMES

--buscar jugador

select nombre,fecha_nacimiento,posicion from dw.dim_jugador
where id_jugador in (select id_jugador from dw.fact_jornada where id_partido <= '179889') 
-- <= '179889' ->temp 2016
-- > '179889' ->temp 2017
-- total sin el where
group by nombre,fecha_nacimiento,poscion
order by 1;

-- seleccionamos a orellana en 2017 -> id_jugador (706,707,708) -> en 2017 coge 707 y 708
--Diferencia entre puntuaciones si es local o no

select sum(puntuacion),count(*) as partidos from dw.fact_jornada where id_jugador in (707,708)
and es_local = 'SI';

select sum(puntuacion),count(*) as partidos from dw.fact_jornada where id_jugador in (707,708)
and es_local = 'NO';

--en funcion del resultado

select sum(puntuacion) puntuacion_total,ROUND(AVG(puntuacion)::numeric,2) as  puntuacion_media_partido,count(*) as partidos
,'victoria' as resultado
from dw.fact_jornada where id_jugador in (707,708) and resultado_jugador = 'victoria'
UNION ALL
select sum(puntuacion) puntuacion_total,ROUND(AVG(puntuacion)::numeric,2) as  puntuacion_media_partido,count(*) as partidos
,'empate' as resultado
from dw.fact_jornada where id_jugador in (707,708) and resultado_jugador = 'empate'
UNION ALL
select sum(puntuacion) puntuacion_total,ROUND(AVG(puntuacion)::numeric,2) as  puntuacion_media_partido,count(*) as partidos 
,'derrota' as resultado
from dw.fact_jornada where id_jugador in (707,708) and resultado_jugador = 'derrota';

--en funcion del clima

select puntuacion,fact_jornada.id_meteo,dim_meteo.temperatura_categoria,dim_meteo.humedad_categoria,dim_meteo.lluvias_categoria,dim_meteo.velocidad_viento_categoria
from dw.fact_jornada inner join dw.dim_meteo on fact_jornada.id_meteo=dim_meteo.id_meteo
where id_jugador in (707,708)
order by 1 desc;

--en funcion de la estacion del año

select sum(puntuacion),estacion_ano
from dw.fact_jornada inner join dw.dim_fecha on fact_jornada.id_fecha=  dim_fecha.id_fecha
where id_jugador in (631)
group by estacion_ano
order by 1 desc;

--en funcion de la hora del partido sacando porcentaje

WITH porcentajes AS (
        select 
    CASE
    WHEN sum(puntuacion) >= 0 THEN sum(puntuacion)
    ELSE 0
    END AS puntuacion
    ,hora_categoria
from dw.fact_jornada inner join dw.dim_fecha on fact_jornada.id_fecha=  dim_fecha.id_fecha
where id_jugador in (707,708)
    and fact_jornada.id_partido between (179510) and (179889) 
group by hora_categoria
order by 1 desc
     )
SELECT
ROUND((sum(puntuacion)::numeric * 100 / (Select sum(puntuacion)::numeric  from porcentajes))::numeric,2) as porcentaje     
,hora_categoria
FROM porcentajes
group by hora_categoria
;

-- toda la info
select dim_jugador.nombre,dim_equipo.nombre equipo,
sum(puntuacion) as puntos ,sum(minutos_jugados) as minutos ,sum(goles) as goles ,sum(tarjeta_amarilla) as amarillas,sum(tarjeta_roja) as rojas ,
count(titular) as titularidades from dw.fact_jornada
inner join dw.dim_jugador on dim_jugador.id_jugador = fact_jornada.id_jugador
inner join dw.dim_equipo on fact_jornada.id_equipo_propio=dim_equipo.id_equipo
where dim_jugador.id_jugador in (707,708)
group by dim_jugador.id_jugador,dim_jugador.nombre,dim_equipo.nombre;

-- los 5 rivales contra los que jugó mejor los 5 rivales contra los que jugó peor

select *  from 
(select puntuacion,  dim_equipo.nombre || ' ('|| dim_entrenador.nombre||')'
from dw.fact_jornada inner join dw.dim_equipo on id_equipo_rival = dim_equipo.id_equipo
inner join dw.dim_entrenador on id_entrenador_rival=dim_entrenador.id_entrenador
where id_jugador in (707,708)
order by 1 desc
FETCH FIRST 5 ROWS ONLY) as  a 
UNION ALL
select * from 
(select puntuacion, dim_equipo.nombre || ' ('|| dim_entrenador.nombre||')'
from dw.fact_jornada inner join dw.dim_equipo on id_equipo_rival = dim_equipo.id_equipo
inner join dw.dim_entrenador on id_entrenador_rival=dim_entrenador.id_entrenador
where id_jugador in (707,708)
order by 1 asc
FETCH FIRST 5 ROWS ONLY)as  b