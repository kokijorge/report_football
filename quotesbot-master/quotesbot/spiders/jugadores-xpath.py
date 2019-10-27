# -*- coding: utf-8 -*-
import scrapy
import json

class JuagadoresSpider(scrapy.Spider):
    name = 'jugadores-xpath'
    
    def start_requests(self): #aquí tengo que pasarles las URLs que cogí en equipos

        FILE = "equipos.json"
        equipos = None
        with open(FILE, encoding="utf8") as f:
            equipos = json.loads(f.read())

        for equipo in equipos[0:1]:
            yield scrapy.Request(url=equipo['url'], callback=self.parse, meta={'equipo': equipo})			

    def parse(self, response):

        resumen = {
            'tabla': response.xpath('//*[@id="yw1"]/table//text()').extract_first()
            }
        yield resumen