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

select sum(puntuacion) puntuacion_total,ROUND(AVG(puntuacion)::numeric,2) as  puntuacion_media,count(*) as partidos 
from dw.fact_jornada where id_jugador in (707,708) and resultado_jugador = 'victoria';
select sum(puntuacion) puntuacion_total,ROUND(AVG(puntuacion)::numeric,2) as  puntuacion_media,count(*) as partidos 
from dw.fact_jornada where id_jugador in (707,708) and resultado_jugador = 'empate';
select sum(puntuacion) puntuacion_total,ROUND(AVG(puntuacion)::numeric,2) as  puntuacion_media,count(*) as partidos 
from dw.fact_jornada where id_jugador in (707,708) and resultado_jugador = 'derrota';

--en funcion del clima

select puntuacion,fact_jornada.id_meteo,dim_meteo.temperatura_categoria,dim_meteo.humedad_categoria,dim_meteo.lluvias_categoria,dim_meteo.velocidad_viento_categoria
from dw.fact_jornada inner join dw.dim_meteo on fact_jornada.id_meteo=dim_meteo.id_meteo
where id_jugador in (707,708)
order by 1 desc;

--en funcion de la hora del partido

select puntuacion,hora_categoria
from dw.fact_jornada inner join dw.dim_fecha on fact_jornada.id_fecha=  dim_fecha.id_fecha
where id_jugador in (707,708)
order by 1 desc;

-- los 5 rivales contra los que jugó mejor

select puntuacion, dim_equipo.nombre,dim_entrenador.nombre,es_local
from dw.fact_jornada inner join dw.dim_equipo on id_equipo_rival = dim_equipo.id_equipo
inner join dw.dim_entrenador on id_entrenador_rival=dim_entrenador.id_entrenador
where id_jugador in (707,708)
order by 1 desc
FETCH FIRST 5 ROWS ONLY;

-- los 5 rivales contra los que jugó peor

select puntuacion, dim_equipo.nombre,dim_entrenador.nombre,es_local
from dw.fact_jornada inner join dw.dim_equipo on id_equipo_rival = dim_equipo.id_equipo
inner join dw.dim_entrenador on id_entrenador_rival=dim_entrenador.id_entrenador
where id_jugador in (707,708)
order by 1 asc
FETCH FIRST 5 ROWS ONLY;