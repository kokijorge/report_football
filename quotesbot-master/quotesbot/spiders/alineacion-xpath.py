# -*- coding: utf-8 -*-
import scrapy
import urllib.parse
from bs4 import BeautifulSoup

#partido_inicial = 179510
partido_inicial = 179512

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'alineacion-xpath'

    def jor_par_generator(self):        
        for jorn in range(1,2):
        #for jorn in range(1,39):
            partido_inicial_de_jornada = partido_inicial + ((jorn-1)*10)
            #for part in range(partido_inicial_de_jornada, partido_inicial_de_jornada+10):
            for part in range(partido_inicial_de_jornada, partido_inicial_de_jornada+1):
                yield (jorn, part)

    def start_requests(self):
        base_url = "https://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_%d_%d/narracion/"

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
        entrenador_visitante = suplentes_visitante.find("p", {"class": "entrenador"}).get_text().strip()
        print ("####################################################")
        for quote in titulares_local:
            nombre = quote.find("p", {"class": "nom-jugador"}).get_text().strip()
            dorsal = quote.find("div", {"class": "camiseta-jugador"}).get_text().strip()            
            print ("NOMBRE ----->>> ", nombre)
            print ("DORSAL ----->>> ", dorsal)
        print ("ENTRENADOR_LOCAL ----->>> ", entrenador_local)
        print ("####################################################")
        for quote in titulares_visitante:
            nombre = quote.find("p", {"class": "nom-jugador"}).get_text().strip()
            dorsal = quote.find("div", {"class": "camiseta-jugador"}).get_text().strip()            
            print ("NOMBRE ----->>> ", nombre)
            print ("DORSAL ----->>> ", dorsal)
        print ("ENTRENADOR_VISITANTE ----->>> ", entrenador_visitante)
        print ("####################################################")
        '''
        resumen = {
        'jornada': response.meta['jornada'],
        'partido':  response.meta['partido'],        
        'comentarios': []
        }
        for quote in mycom:
            minuto = quote.find("span", {"class": "minuto-comentario"}).get_text().strip()
            quote.span.extract() # quita el primer span
            quote.span.extract() # quita el segundo span
            texto_1 = quote.get_text().strip()            
            texto_2 = self.espaciar_caracteres(texto_1)
            texto = self.retocar_caracteres(texto_2)
            comentario = {
            'minuto': minuto,
            'text': texto
            }
            resumen['comentarios'].append(comentario)
        
        yield resumen
        '''