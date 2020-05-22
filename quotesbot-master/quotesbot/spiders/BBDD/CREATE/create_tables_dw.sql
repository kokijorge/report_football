--DROP TABLE IF EXISTS "dw"."fact_jornada" CASCADE;
--DROP TABLE IF EXISTS "dw"."dim_jugador" CASCADE;
--DROP TABLE IF EXISTS "dw"."dim_equipo" CASCADE;
--DROP TABLE IF EXISTS "dw"."dim_entrenador" CASCADE;
--DROP TABLE IF EXISTS "dw"."dim_fecha" CASCADE;
--DROP TABLE IF EXISTS "dw"."dim_estadio" CASCADE;
--DROP TABLE IF EXISTS "dw"."dim_meteo" CASCADE;
--DROP TABLE IF EXISTS "dw"."aux_jornada" CASCADE;

CREATE TABLE "dw"."aux_jornada" (	
	"nombre" text NOT NULL,
	"fecha_nacimiento" date,
	"fecha"              DATE NOT NULL,  
	"hora_categoria"		text NOT NULL,	
	"estadio" text NOT NULL,
	"temperatura_categoria" text,
	"lluvias_categoria" text,
	"humedad_categoria" text,
	"velocidad_viento_categoria" text,	
	"resultado_jugador" text NOT NULL,
	"puntuacion" int2 NOT NULL,
	"titular" varchar(2),
	"es_local" varchar(2),
	"equipo_propio" text ,
	"equipo_contrario" text ,
	"entrenador_propio" text,
	"fec_nac_ent_propio" date ,
	"entrenador_contrario" text,
	"fec_nac_ent_contrario" date ,
	"tarjeta_amarilla" int2 NOT NULL,
	"tarjeta_roja" int2 NOT NULL,
	"minutos_jugados" int2 NOT NULL,	
	"goles" int2 NOT NULL,
	"resultado_propio" int2 NOT NULL,
	"resultado_contrario" int2 NOT NULL,
	"id_partido" int8 NOT NULL
)
WITH (
	OIDS = False
);

CREATE TABLE "dw"."fact_jornada" (	
	"id_jugador" int4 NOT NULL,
	"id_partido" int8 NOT NULL,
	"id_fecha" int4 NOT NULL,	
	"id_estadio" int4 NOT NULL,
	"id_meteo" int4 NOT NULL,	
	"resultado_jugador" text NOT NULL,
	"puntuacion" int2 NOT NULL,
	"titular" varchar(2),
	"es_local" varchar(2),
	"id_equipo_propio" int4 NOT NULL,
	"id_equipo_rival" int4 NOT NULL,
	"id_entrenador_propio" int4 NOT NULL,
	"id_entrenador_rival" int4 NOT NULL,
	"tarjeta_amarilla" int2 NOT NULL,
	"tarjeta_roja" int2 NOT NULL,
	"minutos_jugados" int2 NOT NULL,
	"goles" int2 NOT NULL,		
	"resultado_propio" int2 NOT NULL,
	"resultado_rival" int2 NOT NULL,
	FOREIGN KEY (id_jugador) REFERENCES "dw"."dim_jugador" (id_jugador),
	FOREIGN KEY (id_equipo_propio) REFERENCES "dw"."dim_equipo" (id_equipo),
	FOREIGN KEY (id_entrenador_propio) REFERENCES "dw"."dim_entrenador" (id_entrenador),
	FOREIGN KEY (id_equipo_rival) REFERENCES "dw"."dim_equipo" (id_equipo),
	FOREIGN KEY (id_entrenador_rival) REFERENCES "dw"."dim_entrenador" (id_entrenador),
	FOREIGN KEY (id_estadio) REFERENCES "dw"."dim_estadio" (id_estadio),
	FOREIGN KEY (id_meteo) REFERENCES "dw"."dim_meteo" (id_meteo),
	FOREIGN KEY (id_fecha) REFERENCES "dw"."dim_fecha" (id_fecha)
)
WITH (
	OIDS = False
);

ALTER TABLE "dw"."fact_jornada" OWNER TO "postgres";

CREATE TABLE "dw"."dim_jugador" (
	"id_jugador" SERIAL,
	"nombre" text NOT NULL,
	"fecha_nacimiento" date,
	"fecha_inicio_contrato" date,
	"fecha_fin_contrato" date,
	"es_valido" varchar(2),	
	"altura" text,	
	"nacionalidad" text NOT NULL,		
	"pie" text,
	"posicion" text NOT NULL,
	CONSTRAINT "dim_jugador_id_jugador_pk" PRIMARY KEY("id_jugador")
)
WITH (
	OIDS = False
);

ALTER TABLE "dw"."dim_jugador" OWNER TO "postgres";

CREATE TABLE "dw"."dim_equipo" (
	"id_equipo" SERIAL,
	"nombre" text ,
	"ano_fundacion" int2,
	CONSTRAINT "dim_equipo_id_equipo_pk" PRIMARY KEY("id_equipo")
)
WITH (
	OIDS = False
);

ALTER TABLE "dw"."dim_equipo" OWNER TO "postgres";

CREATE TABLE "dw"."dim_entrenador" (
	"id_entrenador" SERIAL,
	"nombre" text,
	"fecha_nacimiento" date , 
	"fecha_inicio_contrato" date,
	"fecha_fin_contrato" date,
	"es_valido" varchar(2),
	"ano_debut" int2, 
	"nacionalidad" text,
	CONSTRAINT "dim_entrenador_id_entrenador_pk" PRIMARY KEY("id_entrenador")
)
WITH (
	OIDS = False
);

ALTER TABLE "dw"."dim_entrenador" OWNER TO "postgres";

CREATE TABLE dw.dim_fecha
(
  id_fecha             INT4 NOT NULL,
  fecha_actual              DATE NOT NULL,
  --hora              VARCHAR(5) NOT NULL,
  hora_categoria		text NOT NULL,
  dia_nombre                 VARCHAR(11) NOT NULL,
  dia_de_la_semana              INT2 NOT NULL,
  es_fin_de_semana 				varchar(2),
  dia_del_mes             INT2 NOT NULL,
  dia_del_ano              INT2 NOT NULL,
  semana_del_mes            INT2 NOT NULL,
  semana_del_ano             INT2 NOT NULL,
  mes_actual             INT2 NOT NULL,
  mes_nombre               VARCHAR(11) NOT NULL,
  estacion_ano				text NOT NULL,
  ano_actual              INT2 NOT NULL,
  ano_futbolistico              INT2 NOT NULL
);

ALTER TABLE dw.dim_fecha ADD CONSTRAINT dim_fecha_fecha_dim_id_pk PRIMARY KEY (id_fecha);

CREATE INDEX dim_fecha_fecha_actual_idx
  ON dw.dim_fecha(fecha_actual);

CREATE TABLE "dw"."dim_estadio" (
	"id_estadio" SERIAL,
	"estadio" text,
	"ciudad" text,
	"capacidad" int8,	
	"coordenada_x" text,
	"coordenada_y" text	,
	CONSTRAINT "dim_estadio_id_estadio_pk" PRIMARY KEY("id_estadio")
)
WITH (
	OIDS = False
);

ALTER TABLE "dw"."dim_estadio" OWNER TO "postgres";

CREATE TABLE "dw"."dim_meteo" (
	"id_meteo" SERIAL,	
	"temperatura_categoria" text,
	"lluvias_categoria" text,
	"humedad_categoria" text,
	"velocidad_viento_categoria" text,
	CONSTRAINT "dim_meteo_id_meteo_pk" PRIMARY KEY("id_meteo")
)
WITH (
	OIDS = False
);

ALTER TABLE "dw"."dim_meteo" OWNER TO "postgres";
