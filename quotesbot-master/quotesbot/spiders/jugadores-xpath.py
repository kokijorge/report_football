# -*- coding: utf-8 -*-
import scrapy

class JuagadoresSpider(scrapy.Spider):
    name = 'jugadores'
    
    def start_requests(self): #aquí tengo que pasarles las URLs que cogí en equipos
        base_url = "https://www.transfermarkt.es/laliga/startseite/wettbewerb/ES1/saison_id/2018/plus/1"
        yield scrapy.Request(url=(base_url))

    def parse(self, response):

        resumen = {
        #para cada equipo saco tabla de jgadores
        }
        yield resumen