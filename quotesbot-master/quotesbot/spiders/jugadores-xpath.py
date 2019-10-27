# -*- coding: utf-8 -*-
import scrapy
import json

class JuagadoresSpider(scrapy.Spider):
    name = 'jugadores-xpath'
    
    def start_requests(self):

        FILE = "equipos.json"
        equipos = None
        with open(FILE, encoding="utf8") as f:
            equipos = json.loads(f.read())

        for equipo in equipos[0:1]:
            yield scrapy.Request(url=equipo['url'], callback=self.parse, meta={'equipo': equipo})			

    def parse(self, response):

         for i in range (1,11): #equipo['plantilla']
            jugagores={
            'dorsal': response.xpath('//*[@id="yw1"]/table/tbody/tr['+str(i)+']/td[1]//text()').extract_first(),
            'nombre':response.xpath('//*[@id="yw1"]/table/tbody/tr['+str(i)+']/td[2]//text()').extract_first(),
            'fecha_nacimiento':response.xpath('//*[@id="yw1"]/table/tbody/tr['+str(i)+']/td[3]//text()').extract_first(),
            'nacionalidad':response.xpath('//*[@id="yw1"]/table/tbody/tr['+str(i)+']/td[4]/img/@title').extract_first(),
            'club_actual':response.xpath('//*[@id="yw1"]/table/tbody/tr['+str(i)+']/td[5]//img/@alt').extract_first(),
            'altura':response.xpath('//*[@id="yw1"]/table/tbody/tr['+str(i)+']/td[6]//text()').extract_first(),
            'pie':response.xpath('//*[@id="yw1"]/table/tbody/tr['+str(i)+']/td[7]//text()').extract_first(),
            'fichado':response.xpath('//*[@id="yw1"]/table/tbody/tr['+str(i)+']/td[8]//text()').extract_first(),
            'club_anterior':response.xpath('//*[@id="yw1"]/table/tbody/tr['+str(i)+']/td[9]//img/@alt').extract_first(),
            'contrato_hasta':response.xpath('//*[@id="yw1"]/table/tbody/tr['+str(i)+']/td[10]//text()').extract_first(),
            'valor_mercado':response.xpath('//*[@id="yw1"]/table/tbody/tr['+str(i)+']/td[11]//text()').extract_first()
            }
            yield jugagores
