# -*- coding: utf-8 -*-
import scrapy
import datetime
import os
import io
import os.path
from collections import defaultdict
import json

FILE = 'quotesbot/spiders/file2.txt'
JSON = 'quotesbot/spiders/data.json'

class TiempoMeteoSpider(scrapy.Spider):
    name = 'tiempoHistorico-xpath'    

    def leer_file(self):
        with io.open(FILE,"r", encoding="utf-8") as f:
            comments = f.readlines()
        total = len(comments)        
        datos = []

        for comentario in comments[1:total]:                
            datos.append({
            'dia': comentario[0:2],
            'partido': comentario[3:9],
            'url': comentario[10:-1]})            

        for dato in datos:
            yield dato

    def start_requests(self):
        base_url = "https://www.tutiempo.net/clima/05-2018/ws-81810.html"
        for dato in self.leer_file():
            yield scrapy.Request(url=(dato['url']), callback=self.parse, meta=dato)
        
    def parse(self, response):       	        
        
        print('****************************************************************************')
        print(response.meta['dia'])
        print(response.meta['partido'])
        print(response.meta['url'])

        print('****************************************************************************')
        '''resumen={
            'dia': response.xpath('//*[@id="ColumnaIzquierda"]/div/div[6]/table/tbody/tr['+num_dia+']/td[1]//text()').extract_first(),
            'temperatura': response.xpath('//*[@id="ColumnaIzquierda"]/div/div[6]/table/tbody/tr['+num_dia+']/td[2]//text()').extract_first(),
            'lluvias': response.xpath('//*[@id="ColumnaIzquierda"]/div/div[6]/table/tbody/tr['+num_dia+']/td[7]//text()').extract_first(),
            'humedad': response.xpath('//*[@id="ColumnaIzquierda"]/div/div[6]/table/tbody/tr['+num_dia+']/td[6]//text()').extract_first(),
            'velocidad_viento': response.xpath('//*[@id="ColumnaIzquierda"]/div/div[6]/table/tbody/tr['+num_dia+']/td[9]//text()').extract_first()
        }
        yield resumen
        '''