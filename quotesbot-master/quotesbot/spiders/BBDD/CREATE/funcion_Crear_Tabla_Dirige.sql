CREATE OR REPLACE FUNCTION stg.Crear_Tabla_Dirige() returns Void
as
$$
DECLARE
	registro Record;
	Cur_equipos Cursor for select nombre from stg.stg_equipo order by 1;
BEGIN
	DROP TABLE IF EXISTS "stg"."stg_dirige" CASCADE;
	CREATE TABLE stg.stg_dirige
	(
	  equipo text NOT NULL 
	, entrenador text NOT NULL	
	, fecha_inicio_contrato date NOT NULL
	, fecha_fin_contrato date
	);
-- Open the cursor
   OPEN Cur_equipos;
   LOOP
		-- fetch row into the film
		FETCH Cur_equipos INTO registro;
		-- INSERT
		INSERT INTO "stg"."stg_dirige"
		select equipo,entrenador,fecha_inicio_contrato,(lead(fecha-1) OVER ( ORDER BY  fecha)) as fecha_fin_contrato
		from 
			(select *,
			CASE
			WHEN entrenador = (lag(entrenador) OVER ( ORDER BY  fecha)) then NULL
			ELSE fecha
			END AS fecha_inicio_contrato
			from stg.stg_entrena where equipo= registro.nombre)
		as contrato where fecha_inicio_contrato is not null;
		EXIT WHEN NOT FOUND;     
      
   END LOOP;
   CLOSE Cur_equipos;   
END; $$
Language 'plpgsql';

--select stg.Crear_Tabla_Dirige()