# -*- coding: utf-8 -*-
import scrapy
import datetime

class EstadioSpider(scrapy.Spider):
    name = 'estadios-xpath'
    
    def start_requests(self):
        base_url = "https://www.livefutbol.com/estadios/esp-primera-division-2017-2018"
        yield scrapy.Request(url=(base_url))
        
    def parse(self, response):
        resumen={
            'estadio': response.xpath('//*[@id="site"]/div[2]/div[1]/div/div[2]/div/table/tbody/tr[2]/td[2]/a').extract_first(),
            'ciudad':response.xpath('//*[@id="site"]/div[2]/div[1]/div/div[2]/div/table/tbody/tr[2]/td[3]').extract_first(),
            'capacidad':response.xpath('//*[@id="site"]/div[2]/div[1]/div/div[2]/div/table/tbody/tr[2]/td[6]').extract_first()
            }
        yield resumen
                    '''for i in range (2,21):
            resumen={
            'estadio': response.xpath('//*[@id="site"]/div[2]/div[1]/div/div[2]/div/table/tbody/tr['+str(i)+']/td[2]/a').extract_first(),
            'ciudad':response.xpath('//*[@id="site"]/div[2]/div[1]/div/div[2]/div/table/tbody/tr['+str(i)+']/td[3]').extract_first(),
            'capacidad':response.xpath('//*[@id="site"]/div[2]/div[1]/div/div[2]/div/table/tbody/tr['+str(i)+']/td[6]').extract_first()
            }
            yield resumen'''     