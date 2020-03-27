--Limpiar BBDD
---------------------------------------------------------------------------------------------------------------------------------------------------------
-- PUNTUACION

CREATE TABLE tfg.dim_puntuacion
(
  nombre                 VARCHAR(30) NOT NULL,
  puntuacion              INT NOT NULL
);
---------------------------------------------------------------------------------------------------------------------------------------------------------
--JUGADORES:

select jugador.equipo,jugador.nombre,alineacion.nombre,alineacion.dorsal
from tfg.staging_jugador jugador
inner join tfg.staging_alineacion alineacion
on jugador.dorsal = alineacion.dorsal
and jugador.equipo= alineacion.equipo
and jugador.nombre like '%' || alineacion.nombre ||'%'
and jugador.equipo= 'Alavés'
group by jugador.equipo,jugador.nombre,alineacion.nombre,alineacion.dorsal order by 4;

select * from tfg.staging_jugador where equipo = 'Alavés' and ano=2016  order by 1;
select * from tfg.staging_alineacion where equipo = 'Alavés' and partido<214386 order by 1;
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