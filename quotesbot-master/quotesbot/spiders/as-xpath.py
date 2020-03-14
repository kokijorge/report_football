# -*- coding: utf-8 -*-
import scrapy
import urllib.parse

from afinn import Afinn

partido_inicial = 214386

def to_write(uni_str):
    return uni_str

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'as-xpath'


    def jor_par_generator(self):
        for jorn in range(1,39):
            partido_inicial_de_jornada = partido_inicial + ((jorn-1)*10)
            for part in range(partido_inicial_de_jornada, partido_inicial_de_jornada+10):
                yield (jorn, part)

    
    def start_requests(self):
        base_url = "https://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_%d_%d/narracion/?omnaut=1"

        for jor, par in self.jor_par_generator():
            yield scrapy.Request(url=(base_url %(jor, par)), callback=self.parse, meta={'jornada': jor, 'partido': par})

    def parse(self, response):

        resumen = {
        
        'jornada': response.meta['jornada'],
        'partido':  response.meta['partido'],
        'equipo_local' :  response.xpath('//div[@class="eq-local"]//span[@class="nom"]/text()').extract_first() ,
        'resultado_local' :  response.xpath('//div[@class="marcador cf"]//span[@class="tanteo-local"]/text()').extract_first().strip() ,
        'equipo_visitante' :  response.xpath('//div[@class="eq-visit"]//span[@class="nom"]/text()').extract_first() ,
        'resultado_visitante' :  response.xpath('//div[@class="marcador cf"]//span[@class="tanteo-visit"]/text()').extract_first().strip(),
        'comentarios': []

        }
        for quote in response.xpath('//div[@id="comments-live-en-auto"]//div[@class="cnt-narracion"]//p[contains(@class,"cnt-comentario")]'):            
            comentario =  quote.xpath('.//text()[3]').extract_first() 
            minuto = quote.xpath('.//span[@class="minuto-comentario"]/text()').extract_first()                
            if len(comentario) == 1:                
                comentario ={
                'minuto': minuto,
                'text': to_write(quote.xpath('.//text()[4]').extract_first().strip())
                }
            else:
                comentario = {
                'minuto': minuto,
                'text': to_write((comentario.strip()))
                }
            resumen['comentarios'].append(comentario)
        
        yield resumen