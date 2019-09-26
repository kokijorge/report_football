# -*- coding: utf-8 -*-
import scrapy
import urllib.parse

def to_write(uni_str):
    return urllib.parse.unquote(uni_str.encode('utf8')).decode('utf8')

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'as-xpath'
    start_urls = [
        'https://resultados.as.com/resultados/futbol/primera/2018_2019/directo/regular_a_1_248217/narracion/?omnaut=1',
    ]

    def parse(self, response):
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