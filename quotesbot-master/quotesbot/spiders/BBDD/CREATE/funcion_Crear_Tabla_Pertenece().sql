CREATE OR REPLACE FUNCTION stg.Crear_Tabla_Pertenece() returns Void
as
$$
DECLARE
	registro Record;
	Cur_jugadores Cursor for select nombre,fecha_nacimiento from stg.aux_jugador2 group by nombre,fecha_nacimiento order by 1;
BEGIN
	DROP TABLE IF EXISTS "stg"."stg_pertenece" CASCADE;
	CREATE TABLE stg.stg_pertenece
	(
	  nombre text
	, fecha_nacimiento date NOT NULL
	, equipo text
	, fecha_inicio_contrato date NOT NULL
	, fecha_fin_contrato date
    , valor_mercado text
	);
-- Open the cursor
   OPEN Cur_jugadores;
   LOOP
    -- fetch row into the film
      FETCH Cur_jugadores INTO registro;
	  INSERT INTO "stg"."stg_pertenece"
      	select nombre,fecha_nacimiento,equipo,fecha_inicio_contrato,(lead(fecha-1) OVER ( ORDER BY  fecha)) as fecha_fin_contrato,valor_mercado
        from (
        	select jor.fecha,ali.nombre,ali.equipo,jug.fecha_nacimiento,jug.valor_mercado,
        	CASE
            	WHEN ali.equipo = (lag(ali.equipo) OVER ( ORDER BY  jor.fecha)) then NULL
            	ELSE jor.fecha
        	END AS fecha_inicio_contrato
        	from stg.stg_alineacion as ali
        	inner join stg.aux_jugador2 as jug on jug.nombre= ali.nombre and jug.equipo=ali.equipo and jug.ano_futbolistico=ali.ano_futbolistico and jug.dorsal=ali.dorsal
        	inner join stg.stg_jornada jor on jor.id_partido=ali.id_partido
        	where ali.nombre= registro.nombre
        	and  jug.fecha_nacimiento= registro.fecha_nacimiento
        order by 1) 
        as contrato where fecha_inicio_contrato is not null;  
    -- exit when no more row to fetch
      EXIT WHEN NOT FOUND;     
      
   END LOOP;
   CLOSE Cur_jugadores;
END; $$
Language 'plpgsql';

--select stg.Crear_Tabla_Pertenece()   