# -*- coding: utf-8 -*-
import scrapy

class EquiposSpider(scrapy.Spider):
    name = 'equipos'
    
    def start_requests(self):
        base_url = "https://www.transfermarkt.es/laliga/startseite/wettbewerb/ES1/saison_id/2018/plus/1"

    def parse(self, response):

        resumen = {
        
        'tabla': response.xpath('//*[@id="yw1_c0"]').extract_first()
        }
        
        yield resumen