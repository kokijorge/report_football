# -*- coding: utf-8 -*-
import scrapy
import urllib.parse
from bs4 import BeautifulSoup

from afinn import Afinn

partido_inicial = 179510
CARACTERES_A_ESPACIAR=['\n\n\n\n\n\n\n']
CARACTERES_A_BORRAR=['\n']

def to_write(uni_str):
    return uni_str

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'comentarios-2016'

    def jor_par_generator(self):        
        for jorn in range(1,2):
            partido_inicial_de_jornada = partido_inicial + ((jorn-1)*10)
            for part in range(partido_inicial_de_jornada, partido_inicial_de_jornada+10):            
                yield (jorn, part)

    def borrar_caracteres(self,texto):
        for caracter in CARACTERES_A_BORRAR:
            texto=texto.replace(caracter,"")
        return texto
    def espaciar_caracteres(self,texto):
        for caracter in CARACTERES_A_ESPACIAR:
            texto=texto.replace(caracter," ")
        return texto
    def retocar_caracteres(self,texto):
        inicial = texto.find('\n')
        if texto[inicial-1] == ' ':
            texto_final = self.borrar_caracteres(texto)
        else:
            texto_retocado = texto[inicial+1:]
            texto_final = self.borrar_caracteres(texto_retocado)
        return texto_final

    def start_requests(self):
        base_url = "https://resultados.as.com/resultados/futbol/primera/2016_2017/directo/regular_a_%d_%d/narracion/?omnaut=1"

        for jor, par in self.jor_par_generator():
            yield scrapy.Request(url=(base_url %(jor, par)), callback=self.parse, meta={'jornada': jor, 'partido': par})
    

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        mydivs = soup.find("div", {"id": "comments-live-en-auto"})
        mycom = mydivs.findAll("p", {"class": "cnt-comentario"})
        print ("count ----->>> ", mycom)
        resumen = {
        'comentarios': []
        }
        for quote in mycom:
            minuto = quote.find("span", {"class": "minuto-comentario"}).get_text().strip()
            quote.span.extract() # quita el primer span
            quote.span.extract() # quita el segundo span
            texto_1 = quote.get_text().strip()            
            texto_2 = self.espaciar_caracteres(texto_1)
            texto = self.retocar_caracteres(texto_2)
            comentario = {            
            'text': texto
            }
            resumen['comentarios'].append(comentario)
        
        yield resumen