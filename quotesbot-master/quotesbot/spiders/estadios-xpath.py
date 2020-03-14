# -*- coding: utf-8 -*-
import scrapy
import datetime

class EstadioSpider(scrapy.Spider):
    name = 'estadios-xpath'
    
    def start_requests(self):
        base_url = "https://www.livefutbol.com/estadios/esp-primera-division-2017-2018"
        #https://www.livefutbol.com/estadios/esp-primera-division-2016-2017_2/
        #https://www.livefutbol.com/estadios/esp-primera-division-2017-2018
        yield scrapy.Request(url=(base_url))
        
    def parse(self, response):
        for i in range (2,22):
            resumen={
            'estadio': response.xpath('//*[@id="site"]/div[2]/div[1]/div/div[2]/div/table/tbody/tr['+str(i)+']/td[2]//text()').extract_first(),
            'ciudad':response.xpath('//*[@id="site"]/div[2]/div[1]/div/div[2]/div/table/tbody/tr['+str(i)+']/td[3]//text()').extract_first(),
            'capacidad':response.xpath('//*[@id="site"]/div[2]/div[1]/div/div[2]/div/table/tbody/tr['+str(i)+']/td[6]//text()').extract_first()
            }
            yield resumen