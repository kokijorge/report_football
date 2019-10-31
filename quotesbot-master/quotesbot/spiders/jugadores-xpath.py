# -*- coding: utf-8 -*-
import os
import json
import scrapy

class JuagadoresSpider(scrapy.Spider):
    name = 'jugadores-xpath'
    
    def start_requests(self):

        
        FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),"equipos.json")
        equipos = None
        with open(FILE, encoding="utf8") as f:
            equipos = json.loads(f.read())

        for equipo in equipos[0:1]:
            yield scrapy.Request(url=equipo['url'], callback=self.parse, meta={'equipo': equipo})			

    def parse(self, response):

        num_jugadores = response.xpath('count(//*[@id="yw1"]/table/tbody/tr)').extract_first()
        print ("count ----->>> ", num_jugadores)

        for i in range (1, int(num_jugadores[:-2])+1): #equipo['plantilla']
            jugador={
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
            yield jugador

        """

        for index, row in  enumerate(response.css('#yw1>table>tbody>tr')[0:1]):
            #<tr class="odd"><td title="Torwart" class="zentriert rueckennummer bg_Torwart"><div class="rn_nummer">1</div></td><td title="" class="posrela"><table class="inline-table" title=""><tbody><tr><td rowspan="2" class=""><a href="#"><img src="https://tmssl.akamaized.net//images/portrait/small/74857-1476949803.jpg?lm=1476949839" title="Marc-André ter Stegen" alt="Marc-André ter Stegen" class="bilderrahmen-fixed"></a></td><td class="hauptlink"><div class="di nowrap"><span class="hide-for-small"><a class="spielprofil_tooltip tooltipstered" id="74857" href="/marc-andre-ter-stegen/profil/spieler/74857">Marc-André ter Stegen</a></span></div><div class="di nowrap"><span class="show-for-small"><a class="spielprofil_tooltip tooltipstered" id="74857" href="/marc-andre-ter-stegen/profil/spieler/74857">M. ter Stegen</a></span></div></td></tr><tr><td>Portero</td></tr></tbody></table></td><td class="zentriert">30/04/1992 (26)</td><td class="zentriert"><img src="https://tmssl.akamaized.net//images/flagge/verysmall/40.png?lm=1520612525" title="Alemania" alt="Alemania" class="flaggenrahmen"></td><td class="zentriert"><a class="vereinprofil_tooltip tooltipstered" id="131" href="/fc-barcelona/startseite/verein/131"><img src="https://tmssl.akamaized.net//images/wappen/verysmall/131.png?lm=1406739548" title="&nbsp;" alt="FC Barcelona" class=""></a></td><td class="zentriert">1,87 m</td><td class="zentriert">derecho</td><td class="zentriert">01/07/2014</td><td class="zentriert"><a class="vereinprofil_tooltip tooltipstered" id="18" href="/borussia-monchengladbach/startseite/verein/18/saison_id/2014"><img src="https://tmssl.akamaized.net//images/wappen/verysmall/18.png?lm=1483890536" title=": Ablöse 12,00 mill. €" alt="Borussia Mönchengladbach" class=""></a></td><td class="zentriert">30.06.2022</td><td class="rechts hauptlink">60,00 mill. €&nbsp;<span title="Vorheriger Marktwert: 60,00 mill. €" class="icons_sprite grey-block-ten">&nbsp;</span></td></tr>

            tds = row.css("#yw1>table>tbody>tr:nth-child(2)")
            #print (dir(tds[1]))
            jugador={
            'dorsal': tds[0].css("div.rn_nummer ::text").extract_first(),
            'nombre': tds[1].css("::text").extract_first(),
            'fecha_nacimiento': tds[5].css("::text").extract_first(),
            'nacionalidad': tds[6].css("img ::attr(title)").extract_first(),
            'club_actual': tds[0].css("div.rn_nummer ::text").extract_first(),
            'altura': tds[0].css("div.rn_nummer ::text").extract_first(),
            'pie': tds[0].css("div.rn_nummer ::text").extract_first(),
            'fichado': tds[0].css("div.rn_nummer ::text").extract_first(),
            'club_anterior': tds[0].css("div.rn_nummer ::text").extract_first(),
            'contrato_hasta': tds[0].css("div.rn_nummer ::text").extract_first(),
            'valor_mercado': tds[0].css("div.rn_nummer ::text").extract_first(),
            }

            print ("Len TDs", len(tds))
            #print(jugador)"""           