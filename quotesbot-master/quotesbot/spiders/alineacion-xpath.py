# -*- coding: utf-8 -*-
import scrapy
import urllib.parse
from bs4 import BeautifulSoup

partido_inicial = 214386
#partido_inicial = 179510

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'alineacion-xpath'

    def jor_par_generator(self):                        
        for jorn in range(1,39):        
            partido_inicial_de_jornada = partido_inicial + ((jorn-1)*10)
            for part in range(partido_inicial_de_jornada, partido_inicial_de_jornada+10):            
                yield (jorn, part)        

    def start_requests(self):
        base_url = "https://resultados.as.com/resultados/futbol/primera/2017_2018/directo/regular_a_%d_%d/narracion/"
        for jor, par in self.jor_par_generator():
            yield scrapy.Request(url=(base_url %(jor, par)), callback=self.parse, meta={'jornada': jor, 'partido': par})
    

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        local = soup.find("div", {"class": "campo-loc"})
        titulares_local = local.findAll("div", {"class": "jugador"})
        visitante = soup.find("div", {"class": "campo-vis"})
        titulares_visitante = visitante.findAll("div", {"class": "jugador"})
        suplentes_local = soup.find("div", {"class": "banquillo-local"})
        suplentes_visitante = soup.find("div", {"class": "banquillo-visitante"})
        entrenador_local = suplentes_local.find("p", {"class": "entrenador"}).get_text().strip()
        banquillo_local = suplentes_local.find("ul", {"class": "jugador"})
        jugadores_banquillo_local = banquillo_local.findAll("li")
        banquillo_visitante = suplentes_visitante.find("ul", {"class": "jugador"})
        jugadores_banquillo_visitante = banquillo_visitante.findAll("li")
        entrenador_visitante = suplentes_visitante.find("p", {"class": "entrenador"}).get_text().strip()
        alineacion_local_titulares = []
        alineacion_visitante_titulares = []
        alineacion_local_suplentes = []
        alineacion_visitante_suplentes = []        

        for quote in titulares_local:
            nombre = quote.find("p", {"class": "nom-jugador"}).get_text().strip()
            dorsal = quote.find("div", {"class": "camiseta-jugador"}).get_text().strip()
            gol =  quote.find("div", {"class": "cont-evento-partido gol"})            
            if gol is None:
                num_goles = 0
            else:
                evento = gol.find("span", {"class": "evento-partido"})
                num_goles = len(evento.findAll("span", {"class": "dato"}))
            tarjeta =  quote.find("div", {"class": "cont-evento-partido tarjeta"})
            if tarjeta is None:
                tarjeta_amarilla = 0
                tarjeta_roja = 0
            else:
                tarjeta_amarilla = len(tarjeta.findAll("span", {"class": "as-icon-tarjeta-roja amarilla"}))
                tarjeta_roja = len(tarjeta.findAll("span", {"class": "as-icon-tarjeta-roja roja"}))
            cambio =  quote.find("div", {"class": "cont-evento-partido cambio"})                   
            if cambio is None:
                minutos = 90
            else:
                minutos_string = cambio.find("strong").get_text()
                minutos = int(minutos_string[0:-1])
            dic_local = {
            'nombre': nombre,
            'dorsal': dorsal,
            'goles': num_goles,
            'tarjeta_amarilla': tarjeta_amarilla,
            'tarjeta_roja': tarjeta_roja,
            'minutos':minutos
            }
            alineacion_local_titulares.append(dic_local)

        for quote in titulares_visitante:
            nombre = quote.find("p", {"class": "nom-jugador"}).get_text().strip()
            dorsal = quote.find("div", {"class": "camiseta-jugador"}).get_text().strip()
            gol =  quote.find("div", {"class": "cont-evento-partido gol"})
            if gol is None:
                num_goles = 0
            else:
                evento = gol.find("span", {"class": "evento-partido"})
                num_goles = len(evento.findAll("span", {"class": "dato"}))
            tarjeta =  quote.find("div", {"class": "cont-evento-partido tarjeta"})
            if tarjeta is None:
                tarjeta_amarilla = 0
                tarjeta_roja = 0
            else:
                tarjeta_amarilla = len(tarjeta.findAll("span", {"class": "as-icon-tarjeta-roja amarilla"}))
                tarjeta_roja = len(tarjeta.findAll("span", {"class": "as-icon-tarjeta-roja roja"}))
            cambio =  quote.find("div", {"class": "cont-evento-partido cambio"})                   
            if cambio is None:
                minutos = 90
            else:
                minutos_string = cambio.find("strong").get_text()
                minutos = int(minutos_string[0:-1])          
            dic_visitante = {
            'nombre': nombre,
            'dorsal': dorsal,
            'goles': num_goles,
            'tarjeta_amarilla': tarjeta_amarilla,
            'tarjeta_roja': tarjeta_roja,
            'minutos':minutos
            }
            alineacion_visitante_titulares.append(dic_visitante)  

        for quote in jugadores_banquillo_local:            
            jugador = quote.find("a")
            if jugador is None:
                jugador = quote.find("span" , {"class": "sin-ficha"})
            dorsal = jugador.find("span").get_text().strip()
            jugador.span.extract()
            jugador_suplente = jugador.get_text().strip()
            gol =  quote.find("div", {"class": "cont-evento-partido gol"})
            if gol is None:
                num_goles = 0
            else:
                evento = gol.find("span", {"class": "evento-partido"})
                num_goles = len(evento.findAll("span", {"class": "dato"}))
            tarjeta =  quote.find("div", {"class": "cont-evento-partido tarjeta"})
            if tarjeta is None:
                tarjeta_amarilla = 0
                tarjeta_roja = 0
            else:
                tarjeta_amarilla = len(tarjeta.findAll("span", {"class": "as-icon-tarjeta-roja amarilla"}))
                tarjeta_roja = len(tarjeta.findAll("span", {"class": "as-icon-tarjeta-roja roja"}))
            cambio =  quote.find("div", {"class": "cont-evento-partido cambio"})
            if cambio is None:
                minutos = 0
            else:
                if len(cambio.findAll("strong")) > 1 :
                    diferencia_minutos = cambio.findAll("strong")
                    salida_string = diferencia_minutos[1].get_text()
                    entrada_string = diferencia_minutos[0].get_text()
                    salida = int(salida_string[0:-1])
                    entrada = int(entrada_string[0:-1])
                    minutos = salida - entrada
                else:                    
                    minutos_string = cambio.find("strong").get_text()
                    minutos = 90 - int(minutos_string[0:-1])  
            dic_ban_loc = {
            'nombre': jugador_suplente,
            'dorsal': dorsal,
            'goles': num_goles,
            'tarjeta_amarilla': tarjeta_amarilla,
            'tarjeta_roja': tarjeta_roja,
            'minutos': minutos
            }
            alineacion_local_suplentes.append(dic_ban_loc)
              
        for quote in jugadores_banquillo_visitante:
            jugador = quote.find("a")
            if jugador is None:
                jugador = quote.find("span" , {"class": "sin-ficha"})                        
            dorsal = jugador.find("span").get_text().strip()
            jugador.span.extract()
            jugador_suplente = jugador.get_text().strip()
            gol =  quote.find("div", {"class": "cont-evento-partido gol"})
            if gol is None:
                num_goles = 0
            else:
                evento = gol.find("span", {"class": "evento-partido"})
                num_goles = len(evento.findAll("span", {"class": "dato"}))
            tarjeta =  quote.find("div", {"class": "cont-evento-partido tarjeta"})
            if tarjeta is None:
                tarjeta_amarilla = 0
                tarjeta_roja = 0
            else:
                tarjeta_amarilla = len(tarjeta.findAll("span", {"class": "as-icon-tarjeta-roja amarilla"}))
                tarjeta_roja = len(tarjeta.findAll("span", {"class": "as-icon-tarjeta-roja roja"}))
            cambio =  quote.find("div", {"class": "cont-evento-partido cambio"})
            if cambio is None:
                minutos = 0
            else:
                if len(cambio.findAll("strong")) > 1 :
                    diferencia_minutos = cambio.findAll("strong")
                    salida_string = diferencia_minutos[1].get_text()
                    entrada_string = diferencia_minutos[0].get_text()
                    salida = int(salida_string[0:-1])
                    entrada = int(entrada_string[0:-1])
                    minutos = salida - entrada
                else:                    
                    minutos_string = cambio.find("strong").get_text()
                    minutos = 90 - int(minutos_string[0:-1])                
            dic_ban_vis = {
            'nombre': jugador_suplente,
            'dorsal': dorsal,
            'goles': num_goles,
            'tarjeta_amarilla': tarjeta_amarilla,
            'tarjeta_roja': tarjeta_roja,
            'minutos': minutos
            }
            alineacion_visitante_suplentes.append(dic_ban_vis)

        resumen = {        
        'partido':  response.meta['partido'],
        'jornada':  response.meta['jornada'],
        'entrenador_local' : entrenador_local,
        'titulares_local': alineacion_local_titulares,
        'suplentes_local': alineacion_local_suplentes,
        'entrenador_visitante' :  entrenador_visitante, 
        'titulares_visitante': alineacion_visitante_titulares,
        'suplentes_visitante': alineacion_visitante_suplentes
        }
        
        yield resumen        