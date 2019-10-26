# -*- coding: utf-8 -*-
import scrapy

class EquiposSpider(scrapy.Spider):
    name = 'equipos'
    
    def start_requests(self):
        base_url = "https://www.transfermarkt.es/laliga/startseite/wettbewerb/ES1/saison_id/2018/plus/1"
        yield scrapy.Request(url=(base_url))

    def parse(self, response):

        resumen = {        
        'club': response.xpath('//*[@id="yw1"]/table/thead/tr[1]/th[1]//text()').extract_first(),
        'plantilla':response.xpath('//*[@id="yw1"]/table/thead/tr[1]/th[4]//text()').extract_first(),
        'edad':response.xpath('//*[@id="yw1"]/table/thead/tr[1]/th[5]//text()').extract_first(),
        'extranjeros':response.xpath('//*[@id="yw1"]/table/thead/tr[1]/th[6]//text()').extract_first(),
        'valor_total':response.xpath('//*[@id="yw1"]/table/thead/tr[1]/th[11]//text()').extract_first()
        }
        
        yield resumen