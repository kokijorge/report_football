# -*- coding: utf-8 -*-
import scrapy
import datetime

url="https://resultados.as.com/resultados/futbol/primera/2016_2017/jornada/regular_a_%d/"
#https://resultados.as.com/resultados/futbol/primera/2017_2018/jornada/regular_a_%d/
#https://resultados.as.com/resultados/futbol/primera/2016_2017/jornada/regular_a_1/
ano= url[52:56]

class JornadaSpider(scrapy.Spider):
    name = 'jornada-xpath'
    
    def jornada_ano_generator(self):
        for jorn in range(1,4):
        ##for jorn in range(1,39):
            yield (jorn)

    
    def start_requests(self):
        base_url = url
        for jor in self.jornada_ano_generator():
            yield scrapy.Request(url=(base_url %(jor)), callback=self.parse, meta={'jornada': jor})

        
    def parse(self, response):
        for i in range (1,2):
            resumen={
            'jornada': response.meta['jornada'],
            'equipo_local': response.xpath('/html/body/div[7]/div[2]/div/div[2]/div/div/div/ul/li['+str(i)+']/div[1]/a/span[1]//text()').extract_first(),
            'ano': ano,
            'equipo_visitante':response.xpath('/html/body/div[7]/div[2]/div/div[2]/div/div/div/ul/li['+str(i)+']/div[3]/a/span[2]//text()').extract_first(),
            'fecha_hora':response.xpath('/html/body/div[7]/div[2]/div/div[2]/div/div/div/ul/li['+str(i)+']/div[4]/span[1]/ul/li[1]/a/span[2]//text()').extract_first()
            }
            yield resumen