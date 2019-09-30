# -*- coding: utf-8 -*-
import scrapy
import urllib.parse

def to_write(uni_str):
    return uni_str

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'as-xpath'
    jornada = 1
    partido = 248210
    
    def start_requests(self):
        base_url = "https://resultados.as.com/resultados/futbol/primera/2018_2019/directo/regular_a_%d_%d/narracion/?omnaut=1"
        while self.jornada<3: 
            yield scrapy.Request(url=(base_url %(self.jornada, self.partido)), callback=self.parse)
            self.partido = self.partido +1 
            if self.partido % 10 == 0 :
                self.jornada = self.jornada +1

    def parse(self, response):
        resumen = {
        'partido': self.partido,
        'jornada': self.jornada,
        'equipo_local' :  response.xpath('//div[@class="eq-local"]//span[@class="nom"]/text()').extract_first() ,
        'resultado_local' :  response.xpath('//div[@class="marcador cf"]//span[@class="tanteo-local"]/text()').extract_first().strip() ,
        'equipo_visitante' :  response.xpath('//div[@class="eq-visit"]//span[@class="nom"]/text()').extract_first() ,
        'resultado_visitante' :  response.xpath('//div[@class="marcador cf"]//span[@class="tanteo-visit"]/text()').extract_first().strip(),
        'comentarios': []

        }
        for quote in response.xpath('//div[@id="comments-live-es-auto"]//div[@class="cnt-narracion"]//p[contains(@class,"cnt-comentario")]'):
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
        #print (dir(self))
        
        #print (dir(response))