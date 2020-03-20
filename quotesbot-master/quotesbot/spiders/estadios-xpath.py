# -*- coding: utf-8 -*-
import scrapy
import datetime

url= "https://www.livefutbol.com/estadios/esp-primera-division-2017-2018"
#https://www.livefutbol.com/estadios/esp-primera-division-2016-2017_2/
#https://www.livefutbol.com/estadios/esp-primera-division-2017-2018
sub = "2"
indice = url.index(sub)
ano= url[indice:indice+4]

class EstadioSpider(scrapy.Spider):
    name = 'estadios-xpath'

    def obtener_url_tiempo(self,ciudad):
        tiempo = {        
            "Sevilla" : "https://www.eltiempo.es/sevilla.html?v=por_hora",
            "Barcelona" : "https://www.eltiempo.es/barcelona.html?v=por_hora",
            "Gijón" : "https://www.eltiempo.es/gijon.html?v=por_hora",
            "Pamplona" : "https://www.eltiempo.es/pamplona.html?v=por_hora",
            "Las Palmas de Gran Canaria" : "https://www.eltiempo.es/las-palmas-de-gran-canaria.html?v=por_hora",
            "Villarreal" : "https://www.eltiempo.es/vila-real.html?v=por_hora",
            "Valencia" : "https://www.eltiempo.es/valencia.html?v=por_hora",
            "Eibar" : "https://www.eltiempo.es/eibar.html?v=por_hora",
            "Málaga" : "https://www.eltiempo.es/malaga.html?v=por_hora",
            "Vitoria-Gasteiz" : "https://www.eltiempo.es/vitoria-gasteiz.html?v=por_hora",
            "Vigo" : "https://www.eltiempo.es/vigo.html?v=por_hora",
            "Leganés" : "https://www.eltiempo.es/leganes.html?v=por_hora",
            "Granada" : "https://www.eltiempo.es/granada.html?v=por_hora",
            "Cornellà de Llobregat" : "https://www.eltiempo.es/cornella-de-llobregat.html?v=por_hora",
            "La Coruña" : "https://www.eltiempo.es/a-coruna.html?v=por_hora",
            "Bilbao" : "https://www.eltiempo.es/bilbao.html?v=por_hora",
            "Madrid" : "https://www.eltiempo.es/madrid.html?v=por_hora",
            "Getafe" : "https://www.eltiempo.es/getafe.html?v=por_hora",
            "Girona" : "https://www.eltiempo.es/girona.html?v=por_hora",
            "San Sebastián" : "https://www.eltiempo.es/san-sebastian.html?v=por_hora"            
        }
        return tiempo.get(ciudad,"Ciudad inválida")
    
    def start_requests(self):
        base_url = url
        yield scrapy.Request(url=(base_url))
        
    def parse(self, response):
        for i in range (2,22):
            ciudad = response.xpath('//*[@id="site"]/div[2]/div[1]/div/div[2]/div/table/tbody/tr['+str(i)+']/td[3]//text()').extract_first()
            resumen={
            'estadio': response.xpath('//*[@id="site"]/div[2]/div[1]/div/div[2]/div/table/tbody/tr['+str(i)+']/td[2]//text()').extract_first(),
            'ano': ano,
            'ciudad':response.xpath('//*[@id="site"]/div[2]/div[1]/div/div[2]/div/table/tbody/tr['+str(i)+']/td[3]//text()').extract_first(),
            'capacidad':response.xpath('//*[@id="site"]/div[2]/div[1]/div/div[2]/div/table/tbody/tr['+str(i)+']/td[6]//text()').extract_first(),
            'url':  self.obtener_url_tiempo(ciudad)
            }
            yield resumen        