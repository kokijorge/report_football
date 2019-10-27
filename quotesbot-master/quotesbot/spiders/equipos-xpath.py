# -*- coding: utf-8 -*-
import scrapy

class EquiposSpider(scrapy.Spider):
    name = 'equipos-xpath'
    
    def start_requests(self):
        base_url = "https://www.transfermarkt.es/laliga/startseite/wettbewerb/ES1/saison_id/2018/plus/1"
        yield scrapy.Request(url=(base_url))

    def parse(self, response):

        for i in range (1,20):
        	equipos={
        	'nombre': response.xpath('//*[@id="yw1"]/table/tbody/tr['+str(i)+']/td[3]//text()').extract_first(),
        	'plantilla':response.xpath('//*[@id="yw1"]/table/tbody/tr[1]/td[4]//text()').extract_first(),
        	'edad':response.xpath('//*[@id="yw1"]/table/tbody/tr['+str(i)+']/td[5]//text()').extract_first(),
        	'extranjeros':response.xpath('//*[@id="yw1"]/table/tbody/tr['+str(i)+']/td[6]//text()').extract_first(),
        	'valor_total':response.xpath('//*[@id="yw1"]/table/tbody/tr['+str(i)+']/td[11]//text()').extract_first(),
        	'url': 'https://www.transfermarkt.es'+response.xpath('//*[@id="yw1"]/table/tbody/tr['+str(i)+']//td[4]//@href').extract_first()+'/plus/1'
        	}
        	yield equipos
