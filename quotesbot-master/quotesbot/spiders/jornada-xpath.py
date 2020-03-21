# -*- coding: utf-8 -*-
import scrapy
import datetime
from bs4 import BeautifulSoup

url="https://resultados.as.com/resultados/futbol/primera/2016_2017/jornada/regular_a_%d/"
#https://resultados.as.com/resultados/futbol/primera/2017_2018/jornada/regular_a_%d/
#https://resultados.as.com/resultados/futbol/primera/2016_2017/jornada/regular_a_1/
ano= url[52:56]

class JornadaSpider(scrapy.Spider):
    name = 'jornada-xpath'
    
    def jornada_ano_generator(self):
        for jorn in range(1,4):
        ##for jorn in range(1,39):
            yield (jorn)

    
    def start_requests(self):
        base_url = url
        for jor in self.jornada_ano_generator():
            yield scrapy.Request(url=(base_url %(jor)), callback=self.parse, meta={'jornada': jor})

        
    def parse(self, response):

        # Decidi abandonar xpath y volver a mi querido Beautifulsoup.... desde entonces todo perfecto
        # https://docs.scrapy.org/en/latest/faq.html#can-i-use-scrapy-with-beautifulsoup
        # Aqui lo has de aprender:
        # https://www.crummy.com/software/BeautifulSoup/bs4/doc/

        # use lxml to get decent HTML parsing speed
        soup = BeautifulSoup(response.text, 'lxml')
        mydivs = soup.findAll("li", {"class": "list-resultado"})
        print("He encontrado {} resultados".format(len(mydivs)) )
        for res in mydivs:
            equipos = res.findAll('div', {"itemprop": "performer"})
            local = equipos[0].get_text().strip()
            visitante = equipos[1].get_text().strip()
            resultado = res.find('div', {"class": "cont-resultado"}).get_text().strip()

            # <time itemprop="startDate" content="2016-08-20T18:15:00+02:00"></time>
            fecha_hora = res.find('span', {"class": "fecha"}).get_text().strip()
            
            resumen={
            'ano': ano,
            'jornada': response.meta['jornada'],
            'equipo_local': local,
            'equipo_visitante':visitante,
            'resultado': resultado,
            'fecha_hora':fecha_hora
            }
            yield resumen

