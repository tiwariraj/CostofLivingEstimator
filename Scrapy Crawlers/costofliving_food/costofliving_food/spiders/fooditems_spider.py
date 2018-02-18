from scrapy import Spider, Request
from costofliving_food.items import FoodAmountItem
import csv

class FoodItemSpider(Spider):

	name = "fooditem_spider"
	allowed_urls = ["https://www.numbeo.com/food-prices"]
	f = open('market.csv')
	csv_f = csv.reader(f)
	market = []
	for row in csv_f:
		market.append(row[0])
		start_urls = ["https://www.numbeo.com/food-prices/in/" + str(link) for link in market]



	def parse(self, response):

			marketname = response.xpath('//span[@itemprop="name"]/text()').extract()[2]
			milk = response.xpath('//table[1]/tr[@class="tr_standard"]//text()').extract()[0]
			milk_price = response.xpath('//table[1]/tr[@class="tr_standard"]//text()').extract()[2].split('\xa0$')[0]
			bread = response.xpath('//table[1]/tr[@class="tr_highlighted"]//text()').extract()[0]
			bread_price = response.xpath('//table[1]/tr[@class="tr_highlighted"]//text()').extract()[2].split('\xa0$')[0]

			rice = response.xpath('//table[1]/tr[@class="tr_standard"]//text()').extract()[4]
			rice_price = response.xpath('//table[1]/tr[@class="tr_standard"]//text()').extract()[6].split('\xa0$')[0]
			eggs = response.xpath('//table[1]/tr[@class="tr_highlighted"]//text()').extract()[4]
			eggs_price = response.xpath('//table[1]/tr[@class="tr_highlighted"]//text()').extract()[6].split('\xa0$')[0]

			cheese = response.xpath('//table[1]/tr[@class="tr_standard"]//text()').extract()[8]
			cheese_price = response.xpath('//table[1]/tr[@class="tr_standard"]//text()').extract()[10].split('\xa0$')[0]
			chicken = response.xpath('//table[1]/tr[@class="tr_highlighted"]//text()').extract()[8]
			chicken_price = response.xpath('//table[1]/tr[@class="tr_highlighted"]//text()').extract()[10].split('\xa0$')[0]

			beef = response.xpath('//table[1]/tr[@class="tr_standard"]//text()').extract()[12]
			beef_price = response.xpath('//table[1]/tr[@class="tr_standard"]//text()').extract()[14].split('\xa0$')[0]
			apples = response.xpath('//table[1]/tr[@class="tr_highlighted"]//text()').extract()[12]
			apples_price = response.xpath('//table[1]/tr[@class="tr_highlighted"]//text()').extract()[14].split('\xa0$')[0]

			banana = response.xpath('//table[1]/tr[@class="tr_standard"]//text()').extract()[16]
			banana_price = response.xpath('//table[1]/tr[@class="tr_standard"]//text()').extract()[18].split('\xa0$')[0]
			oranges = response.xpath('//table[1]/tr[@class="tr_highlighted"]//text()').extract()[16]
			oranges_price = response.xpath('//table[1]/tr[@class="tr_highlighted"]//text()').extract()[18].split('\xa0$')[0]

			tomato = response.xpath('//table[1]/tr[@class="tr_standard"]//text()').extract()[20]
			tomato_price = response.xpath('//table[1]/tr[@class="tr_standard"]//text()').extract()[22].split('\xa0$')[0]
			potato = response.xpath('//table[1]/tr[@class="tr_highlighted"]//text()').extract()[20]
			potato_price = response.xpath('//table[1]/tr[@class="tr_highlighted"]//text()').extract()[22].split('\xa0$')[0]

			onion = response.xpath('//table[1]/tr[@class="tr_standard"]//text()').extract()[24]
			onion_price = response.xpath('//table[1]/tr[@class="tr_standard"]//text()').extract()[26].split('\xa0$')[0]
			lettuce = response.xpath('//table[1]/tr[@class="tr_highlighted"]//text()').extract()[24]
			lettuce_price = response.xpath('//table[1]/tr[@class="tr_highlighted"]//text()').extract()[26].split('\xa0$')[0]

			dailymin = response.xpath('//table[1]/tr/td/b/text()').extract_first()
			dailymin_price = response.xpath('//table[1]/tr/td[@style="text-align: right"]//text()').extract()[14].split('\xa0$')[0]
			monthlymin = response.xpath('//table[1]/tr/td/b/text()').extract()[1]
			monthlymin_price = response.xpath('//table[1]/tr/td[@style="text-align: right"]//text()').extract()[15].split('\xa0$')[0]

			milk_col= response.xpath('//table[3]/tr/td//text()').extract()[0]
			milk_avg_col= response.xpath('//table[3]/tr/td//text()').extract()[1].split('\xa0$')[0]
			milk_min_col= response.xpath('//table[3]/tr/td//text()').extract()[3].split('\n')[1]
			milk_max_col= response.xpath('//table[3]/tr/td//text()').extract()[5]

			bread_col= response.xpath('//table[3]/tr/td//text()').extract()[6]
			bread_avg_col= response.xpath('//table[3]/tr/td//text()').extract()[7].split('\xa0$')[0]
			bread_min_col= response.xpath('//table[3]/tr/td//text()').extract()[9].split('\n')[1]
			bread_max_col= response.xpath('//table[3]/tr/td//text()').extract()[11]

			rice_col= response.xpath('//table[3]/tr/td//text()').extract()[12]
			rice_avg_col= response.xpath('//table[3]/tr/td//text()').extract()[13].split('\xa0$')[0]
			rice_min_col= response.xpath('//table[3]/tr/td//text()').extract()[15].split('\n')[1]
			rice_max_col= response.xpath('//table[3]/tr/td//text()').extract()[17]

			col_eggs_col= response.xpath('//table[3]/tr/td//text()').extract()[18]
			col_eggs_avg_col= response.xpath('//table[3]/tr/td//text()').extract()[19].split('\xa0$')[0]
			col_eggs_min_col= response.xpath('//table[3]/tr/td//text()').extract()[21].split('\n')[1]
			col_eggs_max_col= response.xpath('//table[3]/tr/td//text()').extract()[23]

			cheese_col= response.xpath('//table[3]/tr/td//text()').extract()[24]
			cheese_avg_col= response.xpath('//table[3]/tr/td//text()').extract()[25].split('\xa0$')[0]
			cheese_min_col= response.xpath('//table[3]/tr/td//text()').extract()[27].split('\n')[1]
			cheese_max_col= response.xpath('//table[3]/tr/td//text()').extract()[29]

			chicken_col= response.xpath('//table[3]/tr/td//text()').extract()[30]
			chicken_avg_col= response.xpath('//table[3]/tr/td//text()').extract()[31].split('\xa0$')[0]
			chicken_min_col= response.xpath('//table[3]/tr/td//text()').extract()[33].split('\n')[1]
			chicken_max_col= response.xpath('//table[3]/tr/td//text()').extract()[35]

			beef_col= response.xpath('//table[3]/tr/td//text()').extract()[36]
			beef_avg_col= response.xpath('//table[3]/tr/td//text()').extract()[37].split('\xa0$')[0]
			beef_min_col= response.xpath('//table[3]/tr/td//text()').extract()[39].split('\n')[1]
			beef_max_col= response.xpath('//table[3]/tr/td//text()').extract()[41]

			apples_col= response.xpath('//table[3]/tr/td//text()').extract()[42]
			apples_avg_col= response.xpath('//table[3]/tr/td//text()').extract()[43].split('\xa0$')[0]
			apples_min_col= response.xpath('//table[3]/tr/td//text()').extract()[45].split('\n')[1]
			apples_max_col= response.xpath('//table[3]/tr/td//text()').extract()[47]

			banana_col= response.xpath('//table[3]/tr/td//text()').extract()[48]
			banana_avg_col= response.xpath('//table[3]/tr/td//text()').extract()[49].split('\xa0$')[0]
			banana_min_col= response.xpath('//table[3]/tr/td//text()').extract()[51].split('\n')[1]
			banana_max_col= response.xpath('//table[3]/tr/td//text()').extract()[53]

			oranges_col= response.xpath('//table[3]/tr/td//text()').extract()[54]
			oranges_avg_col= response.xpath('//table[3]/tr/td//text()').extract()[55].split('\xa0$')[0]
			oranges_min_col= response.xpath('//table[3]/tr/td//text()').extract()[57].split('\n')[1]
			oranges_max_col= response.xpath('//table[3]/tr/td//text()').extract()[59]

			tomato_col= response.xpath('//table[3]/tr/td//text()').extract()[60]
			tomato_avg_col= response.xpath('//table[3]/tr/td//text()').extract()[61].split('\xa0$')[0]
			tomato_min_col= response.xpath('//table[3]/tr/td//text()').extract()[63].split('\n')[1]
			tomato_max_col= response.xpath('//table[3]/tr/td//text()').extract()[65]

			potato_col= response.xpath('//table[3]/tr/td//text()').extract()[66]
			potato_avg_col= response.xpath('//table[3]/tr/td//text()').extract()[67].split('\xa0$')[0]
			potato_min_col= response.xpath('//table[3]/tr/td//text()').extract()[69].split('\n')[1]
			potato_max_col= response.xpath('//table[3]/tr/td//text()').extract()[71]

			onion_col= response.xpath('//table[3]/tr/td//text()').extract()[72]
			onion_avg_col= response.xpath('//table[3]/tr/td//text()').extract()[73].split('\xa0$')[0]
			onion_min_col= response.xpath('//table[3]/tr/td//text()').extract()[75].split('\n')[1]
			onion_max_col= response.xpath('//table[3]/tr/td//text()').extract()[77]

			lettuce_col= response.xpath('//table[3]/tr/td//text()').extract()[78]
			lettuce_avg_col= response.xpath('//table[3]/tr/td//text()').extract()[79].split('\xa0$')[0]
			lettuce_min_col= response.xpath('//table[3]/tr/td//text()').extract()[81].split('\n')[1]
			lettuce_max_col = response.xpath('//table[3]/tr/td//text()').extract()[83]

			item = FoodAmountItem()
			item['marketname'] = marketname 
			item['milk'] = milk
			item['milk_price'] = milk_price
			item['bread'] = bread
			item['bread_price'] = bread_price
			item['rice'] = rice
			item['rice_price'] = rice_price
			item['eggs'] = eggs
			item['eggs_price'] = eggs_price
			item['cheese'] = cheese
			item['cheese_price'] = cheese_price
			item['chicken'] = chicken
			item['chicken_price'] = chicken_price
			item['beef'] = beef
			item['beef_price'] = beef_price
			item['apples'] = apples
			item['apples_price'] = apples_price
			item['banana'] = banana
			item['banana_price'] = banana_price
			item['oranges'] = oranges
			item['oranges_price'] = oranges_price           
			item['tomato'] = tomato
			item['tomato_price'] = tomato_price
			item['potato'] = potato
			item['potato_price'] = potato_price  
			item['onion'] = onion
			item['onion_price'] = onion_price
			item['lettuce'] = lettuce
			item['lettuce_price'] = lettuce_price  
			item['dailymin'] = dailymin
			item['dailymin_price'] = dailymin_price
			item['monthlymin'] = monthlymin
			item['monthlymin_price'] = monthlymin_price

			item['milk_col'] = milk_col
			item['milk_avg_col'] = milk_avg_col
			item['milk_min_col'] = milk_min_col
			item['milk_max_col'] = milk_max_col

			item['bread_col'] = bread_col
			item['bread_avg_col'] = bread_avg_col
			item['bread_min_col'] = bread_min_col
			item['bread_max_col'] = bread_max_col

			item['rice_col'] = rice_col
			item['rice_avg_col'] = rice_avg_col
			item['rice_min_col'] = rice_min_col
			item['rice_max_col'] = rice_max_col

			item['col_eggs_col'] = col_eggs_col
			item['col_eggs_avg_col'] = col_eggs_avg_col
			item['col_eggs_min_col'] = col_eggs_min_col
			item['col_eggs_max_col'] = col_eggs_max_col

			item['cheese_col'] = cheese_col
			item['cheese_avg_col'] = cheese_avg_col
			item['cheese_min_col'] = cheese_min_col
			item['cheese_max_col'] = cheese_max_col

			item['chicken_col'] = chicken_col
			item['chicken_avg_col'] = chicken_avg_col
			item['chicken_min_col'] = chicken_min_col
			item['chicken_max_col'] = chicken_max_col

			item['beef_col'] = beef_col
			item['beef_avg_col'] = beef_avg_col
			item['beef_min_col'] = beef_min_col
			item['beef_max_col'] = beef_max_col

			item['apples_col'] = apples_col
			item['apples_avg_col'] = apples_avg_col
			item['apples_min_col'] = apples_min_col
			item['apples_max_col'] = apples_max_col

			item['banana_col'] = banana_col
			item['banana_avg_col'] = banana_avg_col
			item['banana_min_col'] = banana_min_col
			item['banana_max_col'] = banana_max_col

			item['oranges_col'] = oranges_col
			item['oranges_avg_col'] = oranges_avg_col
			item['oranges_min_col'] = oranges_min_col
			item['oranges_max_col'] = oranges_max_col

			item['tomato_col'] = tomato_col
			item['tomato_avg_col'] = tomato_avg_col
			item['tomato_min_col'] = tomato_min_col
			item['tomato_max_col'] = tomato_max_col

			item['potato_col'] = potato_col
			item['potato_avg_col'] = potato_avg_col
			item['potato_min_col'] = potato_min_col
			item['potato_max_col'] = potato_max_col

			item['onion_col'] = onion_col
			item['onion_avg_col'] = onion_avg_col
			item['onion_min_col'] = onion_min_col
			item['onion_max_col'] = onion_max_col

			item['lettuce_col'] = lettuce_col
			item['lettuce_avg_col'] = lettuce_avg_col
			item['lettuce_min_col'] = lettuce_min_col
			item['lettuce_max_col'] = lettuce_max_col

			yield item