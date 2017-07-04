# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from provcity.items import *

import urlparse



class StatsSpider(scrapy.Spider):
    name = 'stats'
    allowed_domains = ['stats.gov.cn']
    start_urls = ['http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/']

    # def parse(self,response):
    #     #return Request('http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/13/1301.html', callback=self.parse_county)
    #     #return Request('http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/13/01/130102.html', callback=self.parse_town)
    #     return Request('http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/13/01/02/130102001.html', callback=self.parse_village)
    #

    def parse(self, response):
        content  =response.css('.provincetable')

        items = []
        for x in content.xpath('*//a'):
            item = ProvinceItem()
            item['province_id'] =  x.xpath('@href').re('[\d]+')[0]
            item['name'] = x.xpath('text()').extract()[0]
            items.append(item)
            yield item

        for item in items:
            yield Request(self.start_urls[0]+item['province_id']+'.html', callback=self.parse_city)



    def parse_city(self, response):
        urls = []
        for x in response.css('.citytr').xpath('td[2]/a'):
            item = CityItem()
            item['province_id'], item['city_id'] = x.xpath('@href').re('[\d]+')
            item['name'] = x.xpath('text()').extract()[0]

            urls.append(urlparse.urljoin(response.url , x.xpath('@href').extract()[0]))
            yield item

        for url in urls:
            yield Request(url, callback=self.parse_county)


    def parse_county(self, response):
        urls = []
        for x in response.css('.countytr').xpath('td[2]/a'):
            item = CountyItem()
            item['county_id'] = x.xpath('@href').re('[\d]+')[-1]
            item['province_id'] = item['county_id'][:2]
            item['city_id'] = item['county_id'][:4]
            item['name'] = x.xpath('text()').extract()[0]

            urls.append(urlparse.urljoin(response.url, x.xpath('@href').extract()[0]))
            yield item

        for url in urls:
            yield Request(url, callback=self.parse_town)


    def parse_town(self, response):
        urls = []
        for x in response.css('.towntr').xpath('td[2]/a'):
            item = TownItem()
            item['town_id'] = x.xpath('@href').re('[\d]+')[-1]
            item['county_id'] = item['town_id'][:6]
            item['province_id'] = item['town_id'][:2]
            item['city_id'] = item['town_id'][:4]
            item['name'] = x.xpath('text()').extract()[0]

            urls.append(urlparse.urljoin(response.url ,  x.xpath('@href').extract()[0]))
            yield item

        for url in urls:
            yield Request(url, callback=self.parse_village)


    def parse_village(self, response):
        for x in response.css('.villagetr'):
            item = VillageItem()
            item['village_id'], a, item['name'] = x.xpath('td/text()').extract()
            item['town_id'] = item['village_id'][:9]
            item['county_id'] = item['village_id'][:6]
            item['province_id'] = item['village_id'][:2]
            item['city_id'] = item['village_id'][:4]
            yield item


