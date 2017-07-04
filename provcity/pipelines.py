# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2
from items import *



class ProvcityPipeline(object):
    def open_spider(self, spider):
        print '-' * 100
        self.db = psycopg2.connect(database="pgerdb", user="postgres", password="liuyou", host="192.168.99.100", port=5432)
        print '*' * 100
        self.cur = self.db.cursor()


    def close_spider(self,spider):
        self.db.cursor()

    def process_item(self, item, spider):
        if item.__class__ is ProvinceItem:
            self.process_province( item)
        if item.__class__ is CityItem:
            self.process_city( item)
        if item.__class__ is CountyItem:
            self.process_county(item)
        if item.__class__ is TownItem:
            self.process_town(item)
        if item.__class__ is VillageItem:
            self.process_village(item)
        return item

    def process_province(self, item):
        """
        :type item: ProvinceItem
        """
        self.cur.execute('insert into basic.p_province (province_id, "name")values (%s, %s);' , (item['province_id'], item['name']))
        self.db.commit();

    def process_city(self, item):
        print '0' * 100
        """
        :type item: CityItem
        """
        self.cur.execute('insert into basic.p_city (city_id,province_id, "name") values(%s, %s, %s)',
                             (item['city_id'], item['province_id'], item['name']))
        self.db.commit();


    def process_county(self, item):
        """
        :type item: CountyItem
        """
        self.cur.execute('insert into basic.p_county (county_id,province_id,city_id, "name")values (%s, %s, %s, %s)',
                             (item['county_id'], item['province_id'], item['city_id'], item['name']))
        self.db.commit();


    def process_town(self, item):
        """
        :type item: TownItem
        """
        self.cur.execute('insert into basic.p_town (town_id,province_id,city_id,county_id, "name")values (%s, %s, %s, %s, %s)',
                             (item['town_id'], item['province_id'], item['city_id'], item['county_id'], item['name']))
        self.db.commit();


    def process_village(self, item):
        """
        :type item: VillageItem
        """
        self.cur.execute(
            'insert into basic.p_village (village_id,province_id,city_id,county_id, town_id,"name") values(%s, %s, %s, %s, %s, %s)',
            (item['village_id'], item['province_id'], item['city_id'], item['county_id'], item['town_id'], item['name']))
        self.db.commit();

