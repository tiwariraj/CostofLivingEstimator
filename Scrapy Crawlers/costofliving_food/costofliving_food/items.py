# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FoodAmountItem(scrapy.Item):
	# define the fields for your item here like:
	marketname = scrapy.Field()
	milk = scrapy.Field()
	milk_price = scrapy.Field()
	bread = scrapy.Field()
	bread_price = scrapy.Field()
	rice = scrapy.Field()
	rice_price = scrapy.Field()
	eggs = scrapy.Field()
	eggs_price = scrapy.Field()
	cheese = scrapy.Field()
	cheese_price = scrapy.Field()
	chicken = scrapy.Field()
	chicken_price = scrapy.Field()
	beef = scrapy.Field()
	beef_price = scrapy.Field()
	apples = scrapy.Field()
	apples_price = scrapy.Field()
	banana = scrapy.Field()
	banana_price = scrapy.Field()
	oranges = scrapy.Field()
	oranges_price = scrapy.Field()
	tomato = scrapy.Field()
	tomato_price = scrapy.Field()
	potato = scrapy.Field()
	potato_price = scrapy.Field()
	onion = scrapy.Field()
	onion_price = scrapy.Field()
	lettuce = scrapy.Field()
	lettuce_price = scrapy.Field()
	dailymin = scrapy.Field()
	dailymin_price = scrapy.Field()
	monthlymin = scrapy.Field()
	monthlymin_price = scrapy.Field()

	milk_col = scrapy.Field()
	milk_avg_col = scrapy.Field()
	milk_min_col = scrapy.Field()
	milk_max_col = scrapy.Field()

	bread_col = scrapy.Field()
	bread_avg_col = scrapy.Field()
	bread_min_col = scrapy.Field()
	bread_max_col = scrapy.Field()

	rice_col = scrapy.Field()
	rice_avg_col = scrapy.Field()
	rice_min_col = scrapy.Field()
	rice_max_col = scrapy.Field()

	col_eggs_col = scrapy.Field()
	col_eggs_avg_col = scrapy.Field()
	col_eggs_min_col = scrapy.Field()
	col_eggs_max_col = scrapy.Field()

	cheese_col = scrapy.Field()
	cheese_avg_col = scrapy.Field()
	cheese_min_col = scrapy.Field()
	cheese_max_col = scrapy.Field()

	chicken_col = scrapy.Field()
	chicken_avg_col = scrapy.Field()
	chicken_min_col = scrapy.Field()
	chicken_max_col = scrapy.Field()

	beef_col = scrapy.Field()
	beef_avg_col = scrapy.Field()
	beef_min_col = scrapy.Field()
	beef_max_col = scrapy.Field()

	apples_col = scrapy.Field()
	apples_avg_col = scrapy.Field()
	apples_min_col = scrapy.Field()
	apples_max_col = scrapy.Field()

	banana_col = scrapy.Field()
	banana_avg_col = scrapy.Field()
	banana_min_col = scrapy.Field()
	banana_max_col = scrapy.Field()

	oranges_col = scrapy.Field()
	oranges_avg_col = scrapy.Field()
	oranges_min_col = scrapy.Field()
	oranges_max_col = scrapy.Field()

	tomato_col = scrapy.Field()
	tomato_avg_col = scrapy.Field()
	tomato_min_col = scrapy.Field()
	tomato_max_col = scrapy.Field()

	potato_col = scrapy.Field()
	potato_avg_col = scrapy.Field()
	potato_min_col = scrapy.Field()
	potato_max_col = scrapy.Field()

	onion_col = scrapy.Field()
	onion_avg_col = scrapy.Field()
	onion_min_col = scrapy.Field()
	onion_max_col = scrapy.Field()

	lettuce_col = scrapy.Field()
	lettuce_avg_col = scrapy.Field()
	lettuce_min_col = scrapy.Field()
	lettuce_max_col = scrapy.Field()