# -*- coding: utf-8 -*-
import scrapy
import urllib.parse

from afinn import Afinn

def to_write(uni_str):
    return uni_str

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'as-xpath-2016'

    def start_requests(self):
        base_url = "https://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_38_179889/narracion/?omnaut=1"        
        yield scrapy.Request(url=(base_url))

    def parse(self, response):

        resumen = {        
        'comentarios': response.xpath('//div[@id="comments-live-en-auto"]//div[@class="cnt-narracion"]//p[contains(@class,"cnt-comentario")][11]').extract_first(),
        }
        yield resumen