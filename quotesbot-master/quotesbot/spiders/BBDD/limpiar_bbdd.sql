--Limpiar BBDD
---------------------------------------------------------------------------------------------------------------------------------------------------------
--JUGADORES:

select jugador.equipo,jugador.nombre as jug_nom ,alineacion.nombre as alin_nom,alineacion.dorsal
from tfg.staging_jugador jugador
inner join tfg.staging_alineacion alineacion
on jugador.dorsal = alineacion.dorsal
and jugador.equipo= alineacion.equipo
and jugador.nombre like '%' || alineacion.nombre ||'%'
and jugador.equipo= alineacion.equipo
and jugador.ano = 2016
and alineacion.partido<214386
group by jugador.equipo,jugador.nombre,alineacion.nombre,alineacion.dorsal order by 1;
--2016-2017 -> 179510 
--2017-2018 -> 214386

UPDATE tfg.staging_jugador jugador
SET nombre = alineacion.nombre
FROM tfg.staging_alineacion alineacion
WHERE 
jugador.dorsal = alineacion.dorsal
and jugador.equipo= alineacion.equipo
and jugador.nombre like '%' || alineacion.nombre ||'%'
and jugador.equipo= 'Sevilla'
and jugador.ano = 2016
and alineacion.partido<214386;

select * from tfg.staging_jugador where nombre not in (select nombre from tfg.staging_alineacion where equipo='Sevilla'
and partido<214386 group by nombre  ) and ano = 2016 and equipo= 'Sevilla' and dorsal<>0;
---------------------------------------------------------------------------------------------------------------------------------------------------------
--Puntuacion:

CREATE TABLE tfg.dim_puntuacion
(
  partido 			double precision,
  nombre                 VARCHAR(30) NOT NULL,
  puntuacion              INT NOT NULL
);

select punt.partido,punt.nombre,alineacion.nombre,alineacion.dorsal
from tfg.dim_puntuacion punt
inner join tfg.staging_alineacion alineacion
on punt.nombre like '%' || alineacion.nombre ||'%'
and alineacion.equipo= 'Levante'
group by punt.partido,punt.nombre,alineacion.nombre,alineacion.dorsal order by 4;

---------------------------------------------------------------------------------------------------------------------------------------------------------

CREATE TABLE tfg.staging_estadio
(
  estadio TEXT
, ciudad TEXT
, capacidad DOUBLE PRECISION
, equipo TEXT
)
;CREATE INDEX idx_staging_estadio_lookup ON tfg.staging_estadio(estadio, ciudad, capacidad, equipo)
;