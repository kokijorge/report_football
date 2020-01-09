# -*- coding: utf-8 -*-
import scrapy
import datetime

class TiempoMeteoSpider(scrapy.Spider):
    name = 'tiempoMeteo-xpath'
    
    def start_requests(self):
        base_url = "https://www.eltiempo.es/naron.html?v=por_hora"
        yield scrapy.Request(url=(base_url))
        
    def parse(self, response):
       	x = datetime.datetime.now()       	
       	#num_filas = response.xpath('count(//*[@id="page"]/main/div[4]/div/section[5]/div/div[1])').extract_first()
       	i=2       	
       	resumen ={
        	'fecha': "%s/%s/%s" % (x.day, x.month, x.year),
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