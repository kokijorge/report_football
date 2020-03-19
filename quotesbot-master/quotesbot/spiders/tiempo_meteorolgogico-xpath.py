# -*- coding: utf-8 -*-
import scrapy
import datetime
import os
import json

class TiempoMeteoSpider(scrapy.Spider):
    name = 'tiempoMeteo-xpath'
    
    def start_requests(self):
        FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),"estadios2017_2018.json")
        #estadios2016_2017.json
        #estadios2017_2018.json
        estadios = None
        with open(FILE, encoding="utf8") as f:
            estadios = json.loads(f.read())

        for estadio in estadios[0:20]:
            yield scrapy.Request(url=estadio['url'], callback=self.parse, meta={'estadio': estadio})
        
    def parse(self, response):
       	x = datetime.datetime.now()       	
       	num_totales = response.xpath('count(//*[@id="page"]/main/div[4]/div/section[5]/div/div[1]/div)').extract_first()
        num_filas = int(num_totales[:-2])
        for i in range (2,num_filas+1):
            resumen={
                'fecha': "%s/%s/%s" % (x.day, x.month, x.year),
                'ciudad': response.meta['estadio']['ciudad'],
                'horas': response.xpath('//*[@id="page"]/main/div[4]/div/section[5]/div/div[1]/div['+str(i)+']/div[1]//text()').extract_first(),
                'temperatura': response.xpath('//*[@id="page"]/main/div[4]/div/section[5]/div/div[1]/div['+str(i)+']/div[2]/span//text()').extract_first(),
                'velocidad_viento': response.xpath('//*[@id="page"]/main/div[4]/div/section[5]/div/div[1]/div['+str(i)+']/div[4]/span//text()').extract_first(),            
                'lluvias': response.xpath('//*[@id="page"]/main/div[4]/div/section[5]/div/div[1]/div['+str(i)+']/div[7]/span[2]//text()').extract_first(),
                'nieve': response.xpath('//*[@id="page"]/main/div[4]/div/section[5]/div/div[1]/div['+str(i)+']/div[8]/span[2]//text()').extract_first(),
                'nubes': response.xpath('//*[@id="page"]/main/div[4]/div/section[5]/div/div[1]/div['+str(i)+']/div[9]/span[2]//text()').extract_first(),
                'tormenta': response.xpath('//*[@id="page"]/main/div[4]/div/section[5]/div/div[1]/div['+str(i)+']/div[10]/span[2]//text()').extract_first().strip(),
                'humedad': response.xpath('//*[@id="page"]/main/div[4]/div/section[5]/div/div[1]/div['+str(i)+']/div[12]/span[2]//text()').extract_first(),
                'prob_precipitacion': response.xpath('//*[@id="page"]/main/div[4]/div/section[5]/div/div[1]/div['+str(i)+']/div[14]/span[2]//text()').extract_first()
            }
            yield resumen