# -*- coding: utf-8 -*-
import scrapy
import datetime
import os
import io
import os.path
from collections import defaultdict
import json
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

FILE = 'file.txt'
JSON = 'data.json'

class TiempoMeteoSpider(scrapy.Spider):
    name = 'tiempoHistorico-xpath'    

    def leer_file(self):
        with io.open(FILE,"r", encoding="utf-8") as f:
            comments = f.readlines()
        total = len(comments)        
        datos = {}
        datos['data']=[]
        for comentario in comments[1:total]:                
            datos['data'].append({
            'dia': comentario[0:2],
            'partido': comentario[3:9],
            'url': comentario[10:-1]})            

        if os.path.isfile('data.json'):
            from os import remove
            remove('data.json')                    

        json_str = json.dumps(datos)
        with open('data.json', 'w') as file:
            json.dump(datos, file, indent=4)

    def leer_json(self):
        with io.open(JSON,"r", encoding="utf-8") as f:
            comments = f.read()
        jornadas = json.loads(comments)
        total= len(jornadas)
        print(jornadas)  
        """for jornada in jornadas[0:total]:
            dia = jornada['dia']
            partido = jornada['partido']
            url = jornada['url']
            print(jornada)"""

    def start_requests(self):
        base_url = "https://www.tutiempo.net/clima/05-2018/ws-81810.html"
        yield scrapy.Request(url=(base_url))
        
    def parse(self, response):       	        
        num_dia = str(1+1)
        print('****************************************************************************')
        self.leer_file()
        self.leer_json()
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