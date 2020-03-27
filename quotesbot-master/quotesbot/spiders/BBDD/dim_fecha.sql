DROP TABLE if exists tfg.dim_fecha;

CREATE TABLE tfg.dim_fecha
(
  fecha_dim_id              INT NOT NULL,
  fecha_actual              DATE NOT NULL,
  hora              VARCHAR(5) NOT NULL,
  dia_nombre                 VARCHAR(11) NOT NULL,
  dia_de_la_semana              INT NOT NULL,
  dia_del_mes             INT NOT NULL,
  dia_del_ano              INT NOT NULL,
  semana_del_mes            INT NOT NULL,
  semana_del_ano             INT NOT NULL,
  mes_actual             INT NOT NULL,
  mes_nombre               VARCHAR(11) NOT NULL,
  ano_actual              INT NOT NULL,
  ano_futbolistico              INT NOT NULL
);

ALTER TABLE tfg.dim_fecha ADD CONSTRAINT dim_fecha_fecha_dim_id_pk PRIMARY KEY (fecha_dim_id);

CREATE INDEX dim_fecha_fecha_actual_idx
  ON tfg.dim_fecha(fecha_actual);

COMMIT;

INSERT INTO tfg.dim_fecha
SELECT
  TO_CHAR(datum, 'yyyymmddHH24')::INT AS fecha_dim_id,  
  datum::DATE AS fecha_actual,
  to_char(datum, 'HH24:00')::text AS hora,
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
       EXTRACT(ISOYEAR FROM datum) AS ano_actual,
	   CASE	   
		WHEN TO_CHAR(datum, 'mm')::INT < 8  THEN TO_CHAR(datum - ('1 year'::interval), 'yyyy')::INT
		WHEN TO_CHAR(datum, 'mm')::INT > 7  THEN TO_CHAR(datum, 'yyyy')::INT
	   END AS ano_futbolistico
FROM generate_series('2016-01-01 00:00:00'::timestamp, '2019-01-01 23:59:59'::timestamp, '1 hour') datum;

COMMIT;