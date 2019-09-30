# -*- coding: utf-8 -*-
import scrapy
import urllib.parse

def to_write(uni_str):
    return uni_str

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'as-xpath'

    partidos = ["248210", "248211"]
    
    def start_requests(self):
        base_url = "https://resultados.as.com/resultados/futbol/primera/2018_2019/directo/regular_a_1_%s/narracion/?omnaut=1"
        for partido in self.partidos :
            yield scrapy.Request(url=(base_url %partido), callback=self.parse)

    def parse(self, response):
        resumen = {
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