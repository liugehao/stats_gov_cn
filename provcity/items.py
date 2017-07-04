# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProvinceItem(scrapy.Item):
    province_id = scrapy.Field()
    name = scrapy.Field()

class CityItem(scrapy.Item):
    city_id=scrapy.Field()
    province_id = scrapy.Field()
    name = scrapy.Field()


class CountyItem(scrapy.Item):
    county_id=scrapy.Field()
    province_id = scrapy.Field()
    city_id=scrapy.Field()
    name = scrapy.Field()

class TownItem(scrapy.Item):
    town_id = scrapy.Field()
    province_id = scrapy.Field()
    city_id=scrapy.Field()
    county_id=scrapy.Field()
    name = scrapy.Field()

class VillageItem(scrapy.Item):
    village_id = scrapy.Field()
    province_id = scrapy.Field()
    city_id=scrapy.Field()
    county_id=scrapy.Field()
    town_id = scrapy.Field()
    name = scrapy.Field()