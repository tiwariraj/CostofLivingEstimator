# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GasAmountItem(scrapy.Item):
		# define the fields for your item here like:
		MarketName = scrapy.Field() 
		GasPrice = scrapy.Field() 
		GasPrice_Min = scrapy.Field()
		GasPrice_Max = scrapy.Field()
		VolkswagenGolf = scrapy.Field() 
		VolkswagenGolf_Min = scrapy.Field() 
		VolkswagenGolf_Max = scrapy.Field() 
		ToyotaCorolla = scrapy.Field() 
		ToyotaCorolla_Min = scrapy.Field() 
		ToyotaCorolla_Max = scrapy.Field()
