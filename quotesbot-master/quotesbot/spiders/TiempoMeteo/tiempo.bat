@echo off
set anio=%date:~6,4%
set mes=%date:~3,2%
set dia=%date:~0,2%
set hora=%time:~0,2%
set hora=%hora: =0%
set minuto=%time:~3,2%
set segundo=%time:~6,2%
scrapy crawl tiempoMeteo-xpath -o resultado_%dia%_%mes%_%anio%_%hora%%minuto%%segundo%.json 
exit