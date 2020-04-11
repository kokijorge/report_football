# -*- coding: utf-8 -*-
import scrapy
import datetime
import os
import io
import os.path
from collections import defaultdict

from bs4 import BeautifulSoup
from scrapy_selenium import SeleniumRequest
import cssutils

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
        urltmp = 'https://www.tutiempo.net/clima/03-2018/ws-80143.html'
        for dex, i in enumerate([4,5]):
            yield scrapy.Request(url=urltmp, callback=self.parse, meta={
                'dia': '0'+str(i),
                'partido': '179527',
                'url': urltmp})
            
        """for dato in self.obtener_param():
            yield scrapy.Request(url=(dato['url']), callback=self.parse, meta=dato)"""
    
    def consigueme_el_valor_desofuscando_los_estilos(self, dias, num_dia_str, selectors, columna):
        
        tdspan = dias[num_dia_str-1].findAll('td')[columna].findAll('span')
        value = ""
        for sp in tdspan:
            print (sp['class'][0])
            piece = selectors['.numspan span.%s::after' % sp['class'][0]]['content'][1:-1]
            print (piece)
            value += piece

        return value

    def parse(self, response):     	  

        soup = BeautifulSoup(response.text, 'lxml')
        tabla_medias = soup.find("table", {"class": "medias"})
        dias = tabla_medias.findAll("tr")

        tabla_clima = soup.find("div", {"class": "clima"})
        valoresenStilo = tabla_clima.find("style").get_text()
        selectors = {}
        for styles in tabla_clima.select('style'):
            css = cssutils.parseString(styles.encode_contents())
            #css = cssutils.parseString(valoresenStilo)
            for rule in css:
                if rule.type == rule.STYLE_RULE:
                    style = rule.selectorText
                    selectors[style] = {}
                    for item in rule.style:
                        propertyname = item.name
                        value = item.value
                        selectors[style][propertyname] = value  
        print (selectors)

        num_dia_int = int( response.meta['dia'])
        num_dia_str=  num_dia_int+1
        num_dia = str(num_dia_str)
        num_filas = response.selector.xpath('count(//*[@id="ColumnaIzquierda"]/div/div[4]/table/tbody/tr)').extract_first()
        if num_filas == 0:
            response.selector.xpath('count(//*[@id="ColumnaIzquierda"]/div/div[6]/table/tbody/tr)').extract_first()
        media = str(num_filas)
        temperatura =  response.selector.xpath('//*[@id="ColumnaIzquierda"]/div/div[4]/table/tbody/tr['+num_dia+']/td[2]//text()').extract_first()
        if temperatura is None:
            temperatura = self.consigueme_el_valor_desofuscando_los_estilos(dias, num_dia_str, selectors, 1)
        lluvias = response.selector.xpath('//*[@id="ColumnaIzquierda"]/div/div[4]/table/tbody/tr['+num_dia+']/td[7]//text()').extract_first()
        if lluvias is None:
            lluvias = self.consigueme_el_valor_desofuscando_los_estilos(dias, num_dia_str, selectors, 6)
        humedad = response.selector.xpath('//*[@id="ColumnaIzquierda"]/div/div[4]/table/tbody/tr['+num_dia+']/td[6]//text()').extract_first()
        if humedad is None:
            humedad = self.consigueme_el_valor_desofuscando_los_estilos(dias, num_dia_str, selectors, 5)
        velocidad_viento = response.selector.xpath('//*[@id="ColumnaIzquierda"]/div/div[4]/table/tbody/tr['+num_dia+']/td[9]//text()').extract_first()
        if velocidad_viento is None:
            velocidad_viento = self.consigueme_el_valor_desofuscando_los_estilos(dias, num_dia_str, selectors, 8)
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