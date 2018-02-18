from scrapy import Spider, Request
from costofliving_gas.items import GasAmountItem
import csv

class GasAmountSpider(Spider):

	name = "gas_spider"
	allowed_urls = ["https://www.numbeo.com/gas-prices"]
	f = open('market.csv')
	csv_f = csv.reader(f)
	market = []
	for row in csv_f:
		market.append(row[0])
		start_urls = ["https://www.numbeo.com/gas-prices/in/" + str(link) for link in market]



	# def parse(self, response):
	
	def parse(self, response):
			gas = response.xpath('//table[@class="data_wide_table"]')

			MarketName = response.xpath('//span[@itemprop="name"]/text()').extract()[2]
			#Gasoline (1 gallon)
			GasPrice = gas.xpath('.//tr/td//text()').extract()[1].split('\xa0$')[0]
			GasPrice_Min =  gas.xpath('.//tr/td//text()').extract()[3].split('\n')[1]
			GasPrice_Max = gas.xpath('.//tr/td//text()').extract()[5]

			#Volkswagen Golf 1.4 90 KW Trendline (Or Equivalent New Car)
			VolkswagenGolf = gas.xpath('.//tr/td//text()').extract()[7].split('\xa0$')[0]
			VolkswagenGolf_Min = gas.xpath('.//tr/td//text()').extract()[9].split('\n')[1]
			VolkswagenGolf_Max = gas.xpath('.//tr/td//text()').extract()[11]

			ToyotaCorolla = gas.xpath('.//tr/td//text()').extract()[13].split('\xa0$')[0]
			ToyotaCorolla_Min = gas.xpath('.//tr/td//text()').extract()[15].split('\n')[1]
			ToyotaCorolla_Max = gas.xpath('.//tr/td//text()').extract()[17]




			item = GasAmountItem()
			item['MarketName'] = MarketName 
			
			item['GasPrice'] = GasPrice
			item['GasPrice_Min'] = GasPrice_Min
			item['GasPrice_Max'] = GasPrice_Max

			item['VolkswagenGolf'] = VolkswagenGolf
			item['VolkswagenGolf_Min'] = VolkswagenGolf_Min
			item['VolkswagenGolf_Max'] = VolkswagenGolf_Max
			
			item['ToyotaCorolla'] = ToyotaCorolla
			item['ToyotaCorolla_Min'] = ToyotaCorolla_Min
			item['ToyotaCorolla_Max'] = ToyotaCorolla_Max

			yield item