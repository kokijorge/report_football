# -*- coding: utf-8 -*-
import scrapy
import datetime

class JornadaSpider(scrapy.Spider):
    name = 'jornada-xpath'
    
    def start_requests(self):
        base_url = "https://resultados.as.com/resultados/futbol/primera/2016_2017/jornada/regular_a_1/"
        yield scrapy.Request(url=(base_url))
        
    def parse(self, response):
        for i in range (1,1):
            resumen={
            'equipo_local': response.xpath('/html/body/div[7]/div[2]/div/div[2]/div/div/div/ul/li['+str(i)+']/div[1]/a/span[1]//text()').extract_first(),
            'equipo_visitante':response.xpath('/html/body/div[7]/div[2]/div/div[2]/div/div/div/ul/li['+str(i)+']/div[3]/a/span[2]//text()').extract_first(),
            'fecha_hora':response.xpath('/html/body/div[7]/div[2]/div/div[2]/div/div/div/ul/li['+str(i)+']/div[4]/span[1]/ul/li[1]/a/span[2]//text()').extract_first()
            }
            yield resumen