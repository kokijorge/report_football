# -*- coding: utf-8 -*-
import scrapy
import urllib.parse

def to_write(uni_str):
    return uni_str

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'as-xpath'
    partido = "248210"
    start_urls = [
        'https://resultados.as.com/resultados/futbol/primera/2018_2019/directo/regular_a_1_%s/narracion/?omnaut=1' %(partido),
    ]

    def parse(self, response):
        yield{
        'equipo_local' :  response.xpath('//div[@class="eq-local"]//span[@class="nom"]/text()').extract_first() ,
        'resultado_local' :  response.xpath('//div[@class="marcador cf"]//span[@class="tanteo-local"]/text()').extract_first().strip() ,
        'equipo_visitante' :  response.xpath('//div[@class="eq-visit"]//span[@class="nom"]/text()').extract_first() ,
        'resultado_visitante' :  response.xpath('//div[@class="marcador cf"]//span[@class="tanteo-visit"]/text()').extract_first().strip() 
        }
        for quote in response.xpath('//div[@id="comments-live-es-auto"]//div[@class="cnt-narracion"]//p[contains(@class,"cnt-comentario")]'):
            comentario =  quote.xpath('.//text()[3]').extract_first() 
            minuto = quote.xpath('.//span[@class="minuto-comentario"]/text()').extract_first()                
            if len(comentario) == 1:                
                yield {
                'minuto': minuto,
                'text': to_write(quote.xpath('.//text()[4]').extract_first().strip())
                }
            else:
                yield {
                'minuto': minuto,
                'text': to_write((comentario.strip()))
                }
        partido = str(int(partido)+1)
        if partido is not "248212":
            yield scrapy.Request(response.urljoin())