DROP TABLE if exists dw.dim_fecha;

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

INSERT INTO dw.dim_fecha
SELECT
  --TO_CHAR(datum, 'yyyymmddHH24')::INT AS id_fecha,  
  CASE
  WHEN (to_char(datum, 'HH24')::int) >= 6 and (to_char(datum, 'HH24')::int) <= 13 THEN TO_CHAR(datum, 'yyyymmdd1')::INT
  WHEN (to_char(datum, 'HH24')::int) > 13 and (to_char(datum, 'HH24')::int) <= 19 THEN TO_CHAR(datum, 'yyyymmdd2')::INT
  ELSE TO_CHAR(datum, 'yyyymmdd3')::INT
  END AS id_fecha, 
  datum::DATE AS fecha_actual,
  --to_char(datum, 'HH24:00')::text AS hora,
CASE
  WHEN (to_char(datum, 'HH24')::int) >= 6 and (to_char(datum, 'HH24')::int) <= 13 THEN 'Mañana'
  WHEN (to_char(datum, 'HH24')::int) > 13 and (to_char(datum, 'HH24')::int) <= 19 THEN 'Tarde'
  ELSE 'Noche'
  END AS hora_categoria, 
CASE
		WHEN rtrim(TO_CHAR(datum, 'Day')) = 'Monday' THEN 'Lunes'
		WHEN rtrim(TO_CHAR(datum, 'Day')) = 'Tuesday' THEN 'Martes'
		WHEN rtrim(TO_CHAR(datum, 'Day')) = 'Wednesday' THEN 'Miércoles'
		WHEN rtrim(TO_CHAR(datum, 'Day')) = 'Thursday' THEN 'Jueves'
		WHEN rtrim(TO_CHAR(datum, 'Day')) = 'Friday' THEN 'Viernes'
		WHEN rtrim(TO_CHAR(datum, 'Day')) = 'Saturday' THEN 'Sábado'
		WHEN rtrim(TO_CHAR(datum, 'Day')) = 'Sunday' THEN 'Domingo'
	   END AS dia_nombre,
       EXTRACT(ISODOW FROM datum) AS dia_de_la_semana,
	   CASE 
       WHEN EXTRACT(ISODOW FROM datum) > 4 THEN 'SI'
       ELSE 'NO' 
       END AS es_fin_de_semana,
       EXTRACT(DAY FROM datum) AS dia_del_mes,
       EXTRACT(DOY FROM datum) AS dia_del_ano,
       TO_CHAR(datum, 'W')::INT AS semana_del_mes,
       EXTRACT(WEEK FROM datum) AS semana_del_ano,
       EXTRACT(MONTH FROM datum) AS mes_actual,
       CASE
		WHEN rtrim(TO_CHAR(datum, 'Month')) = 'January' THEN 'Enero'
		WHEN rtrim(TO_CHAR(datum, 'Month')) = 'February' THEN 'Febrero'
		WHEN rtrim(TO_CHAR(datum, 'Month')) = 'March' THEN 'Marzo'
		WHEN rtrim(TO_CHAR(datum, 'Month')) = 'April' THEN 'Abril'
		WHEN rtrim(TO_CHAR(datum, 'Month')) = 'May' THEN 'Mayo'
		WHEN rtrim(TO_CHAR(datum, 'Month')) = 'June' THEN 'Junio'
		WHEN rtrim(TO_CHAR(datum, 'Month')) = 'July' THEN 'Julio'
		WHEN rtrim(TO_CHAR(datum, 'Month')) = 'August' THEN 'Agosto'
		WHEN rtrim(TO_CHAR(datum, 'Month')) = 'September' THEN 'Septiembre'
		WHEN rtrim(TO_CHAR(datum, 'Month')) = 'October' THEN 'Octubre'
		WHEN rtrim(TO_CHAR(datum, 'Month')) = 'November' THEN 'Noviembre'
		WHEN rtrim(TO_CHAR(datum, 'Month')) = 'December' THEN 'Diciembre'
	   END AS mes_nombre,
	   CASE 
  WHEN (TO_CHAR(datum, 'mmdd')::INT ) > 320  and  (TO_CHAR(datum, 'mmdd')::INT ) < 621 then 'Primavera'
  WHEN (TO_CHAR(datum, 'mmdd')::INT ) > 620  and  (TO_CHAR(datum, 'mmdd')::INT ) < 921 then 'Verano'
  WHEN (TO_CHAR(datum, 'mmdd')::INT ) > 920  and  (TO_CHAR(datum, 'mmdd')::INT ) < 1221 then 'Otoño'
  ELSE  'Invierno'
  END AS estacion_ano,
       EXTRACT(ISOYEAR FROM datum) AS ano_actual,
	   CASE	   
		WHEN TO_CHAR(datum, 'mm')::INT < 8  THEN TO_CHAR(datum - ('1 year'::interval), 'yyyy')::INT
		WHEN TO_CHAR(datum, 'mm')::INT > 7  THEN TO_CHAR(datum, 'yyyy')::INT
	   END AS ano_futbolistico
FROM generate_series('2016-01-01 00:00:00'::timestamp, '2019-01-01 23:59:59'::timestamp, '1 hour') datum;
