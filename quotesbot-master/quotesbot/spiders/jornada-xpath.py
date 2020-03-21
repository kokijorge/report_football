# -*- coding: utf-8 -*-
import scrapy
import datetime
from bs4 import BeautifulSoup
import re

url="https://resultados.as.com/resultados/futbol/primera/2017_2018/jornada/regular_a_%d/"
#https://resultados.as.com/resultados/futbol/primera/2017_2018/jornada/regular_a_%d/
#https://resultados.as.com/resultados/futbol/primera/2016_2017/jornada/regular_a_%d/
ano= url[52:56]

class JornadaSpider(scrapy.Spider):
    name = 'jornada-xpath'
    
    def jornada_ano_generator(self):        
        for jorn in range(1,39):
            yield (jorn)

    
    def start_requests(self):
        base_url = url
        for jor in self.jornada_ano_generator():
            yield scrapy.Request(url=(base_url %(jor)), callback=self.parse, meta={'jornada': jor})

        
    def parse(self, response):

        # Beautifulsoup
        # https://docs.scrapy.org/en/latest/faq.html#can-i-use-scrapy-with-beautifulsoup        
        # https://www.crummy.com/software/BeautifulSoup/bs4/doc/        
        soup = BeautifulSoup(response.text, 'lxml')
        mydivs = soup.findAll("li", {"class": "list-resultado"})
        print("He encontrado {} resultados".format(len(mydivs)) )
        for res in mydivs:
            equipos = res.findAll('div', {"itemprop": "performer"})
            local = equipos[0].get_text().strip()
            visitante = equipos[1].get_text().strip()
            todo = res.find('div', {"class": "cont-resultado"})
            pag = todo.find('a').get('href')
            inicio = pag.rfind("_") +1
            fin = pag.rfind("/")
            id_partido = pag[inicio:fin]
            fecha_hora = res.find('span', {"class": "fecha"}).get_text().strip()            
            resumen={
            'id_partido': id_partido,
            'jornada': response.meta['jornada'],
            'ano': ano,            
            'equipo_local': local,
            'equipo_visitante':visitante,            
            'fecha_hora':fecha_hora
            }
            yield resumen

