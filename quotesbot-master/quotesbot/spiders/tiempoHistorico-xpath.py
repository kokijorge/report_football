# -*- coding: utf-8 -*-
import scrapy
import datetime
import os
import io
import os.path
from collections import defaultdict

FILE = 'file.txt'

class TiempoMeteoSpider(scrapy.Spider):
    name = 'tiempoHistorico-xpath'    

    def obtener_param(self):
        with io.open(FILE,"r", encoding="utf-8") as f:
            comments = f.readlines()
        total = len(comments)        
        datos = []

        for comentario in comments[1:11]:                
            datos.append({
            'dia': comentario[0:2],
            'partido': comentario[3:9],
            'url': comentario[10:-1]})            

        for dato in datos:
            yield dato

    def start_requests(self):        
        for dato in self.obtener_param():
            yield scrapy.Request(url=(dato['url']), callback=self.parse, meta=dato)
        
    def parse(self, response):     	        
        num_dia_int = int( response.meta['dia'])
        num_dia_str=  num_dia_int+1
        num_dia = str(num_dia_str)
        num_filas = response.xpath('count(//*[@id="ColumnaIzquierda"]/div/div[4]/table/tbody/tr)').extract_first()
        if num_filas == 0:
            response.xpath('count(//*[@id="ColumnaIzquierda"]/div/div[6]/table/tbody/tr)').extract_first()
        media = str(num_filas)
        temperatura =  response.xpath('//*[@id="ColumnaIzquierda"]/div/div[4]/table/tbody/tr['+num_dia+']/td[2]//text()').extract_first()
        if temperatura is None:
            temperatura =  response.xpath('//*[@id="ColumnaIzquierda"]/div/div[6]/table/tbody/tr['+num_dia+']/td[2]//text()').extract_first()        
        lluvias = response.xpath('//*[@id="ColumnaIzquierda"]/div/div[4]/table/tbody/tr['+num_dia+']/td[7]//text()').extract_first()
        if lluvias is None:
            lluvias = response.xpath('//*[@id="ColumnaIzquierda"]/div/div[6]/table/tbody/tr['+num_dia+']/td[7]//text()').extract_first()        
        humedad = response.xpath('//*[@id="ColumnaIzquierda"]/div/div[4]/table/tbody/tr['+num_dia+']/td[6]//text()').extract_first()
        if humedad is None:
            humedad = response.xpath('//*[@id="ColumnaIzquierda"]/div/div[6]/table/tbody/tr['+num_dia+']/td[6]//text()').extract_first()        
        velocidad_viento = response.xpath('//*[@id="ColumnaIzquierda"]/div/div[4]/table/tbody/tr['+num_dia+']/td[9]//text()').extract_first()
        if velocidad_viento is None:
            velocidad_viento = response.xpath('//*[@id="ColumnaIzquierda"]/div/div[6]/table/tbody/tr['+num_dia+']/td[9]//text()').extract_first()
        resumen={
            'dia': response.meta['dia'],
            'temperatura': temperatura,            
            'lluvias': lluvias,
            'humedad': humedad,
            'velocidad_viento': velocidad_viento,
            'partido': response.meta['partido'],            
            'url': response.meta['url']
        }
        yield resumen