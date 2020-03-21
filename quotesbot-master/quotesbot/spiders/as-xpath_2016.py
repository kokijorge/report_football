# -*- coding: utf-8 -*-
import scrapy
import urllib.parse
from bs4 import BeautifulSoup

from afinn import Afinn

def to_write(uni_str):
    return uni_str

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'as-xpath-2016'

    def start_requests(self):
        base_url = "https://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_38_179889/narracion/?omnaut=1"        
        yield scrapy.Request(url=(base_url))

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        mydivs = soup.find("div", {"id": "comments-live-en-auto"})
        #mycom = mydivs.findAll("p", {"class": "cnt-comentario"})        
        print(mydivs)
        print("He encontrado {} resultados".format(len(mydivs)))
        #comentarios es un array de:
        #'minuto': minuto,
        #'text': to_write(quote.xpath('.//text()[4]').extract_first().strip())
        '''for res in mydivs:
            minuto = res.findAll('div', {"id": "comments-live-en-auto"})
            local = equipos[0].get_text().strip()
            visitante = equipos[1].get_text().strip()         
            resumen={
            'id_partido': id_partido,
            'jornada': response.meta['jornada'],
            'ano': ano,            
            'equipo_local': local,
            'equipo_visitante':visitante,            
            'fecha_hora':fecha_hora
            }
            yield resumen
        '''