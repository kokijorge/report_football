# -*- coding: utf-8 -*-
import scrapy
import datetime
import os
import json
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class TiempoMeteoSpider(scrapy.Spider):
    name = 'tiempoHistorico-xpath'    

    def start_requests(self):
        base_url = "https://www.tutiempo.net/clima/05-2018/ws-81810.html"
        yield scrapy.Request(url=(base_url))
        
    def parse(self, response):       	        
        num_dia = str(1+1)
        print('****************************************************************************')
        self.obtener_datos()
        print('****************************************************************************')
        resumen={
            'dia': response.xpath('//*[@id="ColumnaIzquierda"]/div/div[6]/table/tbody/tr['+num_dia+']/td[1]//text()').extract_first(),
            'temperatura': response.xpath('//*[@id="ColumnaIzquierda"]/div/div[6]/table/tbody/tr['+num_dia+']/td[2]//text()').extract_first(),
            'lluvias': response.xpath('//*[@id="ColumnaIzquierda"]/div/div[6]/table/tbody/tr['+num_dia+']/td[7]//text()').extract_first(),
            'humedad': response.xpath('//*[@id="ColumnaIzquierda"]/div/div[6]/table/tbody/tr['+num_dia+']/td[6]//text()').extract_first(),
            'velocidad_viento': response.xpath('//*[@id="ColumnaIzquierda"]/div/div[6]/table/tbody/tr['+num_dia+']/td[9]//text()').extract_first()
        }
        yield resumen