# -*- coding: utf-8 -*-
import scrapy
import datetime

class TiempoMeteoSpider(scrapy.Spider):
    name = 'urlTiempo-xpath'
    
    def start_requests(self):
        base_url = "https://www.google.com/search?sxsrf=ACYBGNSrruOqzWJTD2BVkkv7HXKJ9lvaCg%3A1573989265565&ei=kSvRXcySItecjLsPseyL-Aw&q=www.eltiempo.es%2FCornell%C3%A1+de+Llobregat.html&oq=www.eltiempo.es%2FCornell%C3%A1+de+Llobregat.html&gs_l=psy-ab.3..35i39.19739.25359..25610...0.0..0.121.868.8j1......0....2j1..gws-wiz.NRw0SnSlbLE&ved=0ahUKEwiMn7f4jvHlAhVXDmMBHTH2As8Q4dUDCAs&uact=5"
        yield scrapy.Request(url=(base_url))
        
    def parse(self, response):       	
       	resumen ={        	
        	'url': response.xpath('//*[@id="rso"]/div[1]//div[@class="r"]/a/@href').extract_first()
        }        
        yield resumen