from scrapy import Spider, Request
from costofliving.items import CostAmountItem
import csv

class CostAmountSpider(Spider):

	name = "costofliving_spider"
	allowed_urls = ["https://www.numbeo.com/cost-of-living"]
	f = open('market.csv')
	csv_f = csv.reader(f)
	market = []
	for row in csv_f:
		market.append(row[0])
		start_urls = ["https://www.numbeo.com/cost-of-living/in/" + str(link) for link in market]
	
	def parse(self, response):
			primary = response.xpath('//table[@class="data_wide_table"]')

			MarketName = response.xpath('//span[@itemprop="name"]/text()').extract()[2]
			
			#Restaurant
			InexpensiveMeal = primary.xpath('.//tr//td//text()').extract()[1].split('\xa0$')[0]
			InexpensiveMeal_Min =  primary.xpath('.//tr/td//text()').extract()[3].split('\n')[1]
			InexpensiveMeal_Max = primary.xpath('.//tr/td//text()').extract()[5]

			#Meal For 2 People - Mid-Range Restaurant - Three Course
			ThreeCourseMeal = primary.xpath('.//tr/td//text()').extract()[7].split('\xa0$')[0]
			ThreeCourseMeal_Min = primary.xpath('.//tr/td//text()').extract()[9].split('\n')[1]
			ThreeCourseMeal_Max = primary.xpath('.//tr/td//text()').extract()[11]

			McDonaldsMeal = primary.xpath('.//tr/td//text()').extract()[13].split('\xa0$')[0]
			McDonaldsMeal_Min = primary.xpath('.//tr/td//text()').extract()[15].split('\n')[1]
			McDonaldsMeal_Max = primary.xpath('.//tr/td//text()').extract()[17]

			#Transportation Monthly Pass
			transportation = response.xpath('//tr[32]')
			MonthlyPass = transportation.xpath('.//td//text()').extract()[1].split('\xa0$')[0]
			MonthlyPass_Min = transportation.xpath('.//td//text()').extract()[3].split('\n')[1]
			MonthlyPass_Max = transportation.xpath('.//td//text()').extract()[5]

			#Utilities
			utilities = response.xpath('//tr[40]')
			BasicUtilities = utilities.xpath('.//td//text()').extract()[1].split('\xa0$')[0]
			BasicUtilities_Min = utilities.xpath('.//td//text()').extract()[3].split('\n')[1]
			BasicUtilities_Max = utilities.xpath('.//td//text()').extract()[5]

			#Internet
			internet = response.xpath('//tr[42]')
			Internet = internet.xpath('.//td//text()').extract()[1].split('\xa0$')[0]
			Internet_Min = internet.xpath('.//td//text()').extract()[3].split('\n')[1]
			Internet_Max = internet.xpath('.//td//text()').extract()[5]
			
			#Fitness Club
			fitness = response.xpath('//tr[44]')
			FitnessClub = fitness.xpath('.//td//text()').extract()[1].split('\xa0$')[0]
			FitnessClub_Min = fitness.xpath('.//td//text()').extract()[3].split('\n')[1]
			FitnessClub_Max = fitness.xpath('.//td//text()').extract()[5]

			#Childcare
			childcare = response.xpath('//tr[48]')
			Childcare = childcare.xpath('.//td//text()').extract()[1].split('\xa0$')[0]
			Childcare_Min = childcare.xpath('.//td//text()').extract()[3].split('\n')[1]
			Childcare_Max = childcare.xpath('.//td//text()').extract()[5]

			#ClothingShoes
			jeans = response.xpath('//tr[51]')
			Jeans = jeans.xpath('.//td//text()').extract()[1].split('\xa0$')[0]
			Jeans_Min = jeans.xpath('.//td//text()').extract()[3].split('\n')[1]
			Jeans_Max = jeans.xpath('.//td//text()').extract()[5]

			dress = response.xpath('//tr[52]')
			SummerDress = dress.xpath('.//td//text()').extract()[1].split('\xa0$')[0]
			SummerDress_Min = dress.xpath('.//td//text()').extract()[3].split('\n')[1]
			SummerDress_Max = dress.xpath('.//td//text()').extract()[5]
			
			shoes = response.xpath('//tr[53]')
			RunningShoes = shoes.xpath('.//td//text()').extract()[1].split('\xa0$')[0]
			RunningShoes_Min = shoes.xpath('.//td//text()').extract()[3].split('\n')[1]
			RunningShoes_Max = shoes.xpath('.//td//text()').extract()[5]
			
			boots = response.xpath('//tr[54]')
			Boots = boots.xpath('.//td//text()').extract()[1].split('\xa0$')[0]
			Boots_Min = boots.xpath('.//td//text()').extract()[3].split('\n')[1]
			Boots_Max = boots.xpath('.//td//text()').extract()[5]

			#RentPerMonth
			rent1br_citycenter = response.xpath('//tr[56]')
			Rent1Br_CityCenter = rent1br_citycenter.xpath('.//td//text()').extract()[1].split('\xa0$')[0]
			Rent1Br_CityCenter_Min = rent1br_citycenter.xpath('.//td//text()').extract()[3].split('\n')[1]
			Rent1Br_CityCenter_Max = rent1br_citycenter.xpath('.//td//text()').extract()[5]

			rent1br_outsidecenter = response.xpath('//tr[57]')
			Rent1Br_OutsideCenter = rent1br_outsidecenter.xpath('.//td//text()').extract()[1].split('\xa0$')[0]
			Rent1Br_OutsideCenter_Min = rent1br_outsidecenter.xpath('.//td//text()').extract()[3].split('\n')[1]
			Rent1Br_OutsideCenter_Max = rent1br_outsidecenter.xpath('.//td//text()').extract()[5]

			rent3br_citycenter = response.xpath('//tr[58]')
			Rent3Br_CityCenter = rent3br_citycenter.xpath('.//td//text()').extract()[1].split('\xa0$')[0]
			Rent3Br_CityCenter_Min = rent3br_citycenter.xpath('.//td//text()').extract()[3].split('\n')[1]
			Rent3Br_CityCenter_Max = rent3br_citycenter.xpath('.//td//text()').extract()[5]

			rent3br_outsidecenter = response.xpath('//tr[59]')
			Rent3Br_OutsideCenter = rent3br_outsidecenter.xpath('.//td//text()').extract()[1].split('\xa0$')[0]
			Rent3Br_OutsideCenter_Min = rent3br_outsidecenter.xpath('.//td//text()').extract()[3].split('\n')[1]
			Rent3Br_OutsideCenter_Max = rent3br_outsidecenter.xpath('.//td//text()').extract()[5]


			#BuyAptMonth
			buy_center = response.xpath('//tr[61]')
			BuyApt_CityCenter = buy_center.xpath('.//td//text()').extract()[1].split('\xa0$')[0]
			BuyApt_CityCenter_Min = buy_center.xpath('.//td//text()').extract()[3].split('\n')[1]
			BuyApt_CityCenter_Max = buy_center.xpath('.//td//text()').extract()[5]

			buy_outsidecenter = response.xpath('//tr[62]')
			BuyApt_OutsideCenter = buy_outsidecenter.xpath('.//td//text()').extract()[1].split('\xa0$')[0]
			BuyApt_OutsideCenter_Min = buy_outsidecenter.xpath('.//td//text()').extract()[3].split('\n')[1]
			BuyApt_OutsideCenter_Max = buy_outsidecenter.xpath('.//td//text()').extract()[5]

			#SalaryPostTax
			salary = response.xpath('//tr[64]')
			MonthlySalary = salary.xpath('.//td//text()').extract()[1].split('\xa0$')[0]

			#Responses
			ResponseCount = response.xpath('//div[@style="display: inline"]/text()').extract_first().strip()


			item = CostAmountItem()
			
			item['MarketName'] = MarketName
			item['InexpensiveMeal'] = InexpensiveMeal
			item['InexpensiveMeal_Min'] = InexpensiveMeal_Min
			item['InexpensiveMeal_Max'] = InexpensiveMeal_Max
			
			item['ThreeCourseMeal'] = ThreeCourseMeal
			item['ThreeCourseMeal_Min'] = ThreeCourseMeal_Min
			item['ThreeCourseMeal_Max'] = ThreeCourseMeal_Max
			
			item['McDonaldsMeal'] = McDonaldsMeal
			item['McDonaldsMeal_Min'] = McDonaldsMeal_Min
			item['McDonaldsMeal_Max'] = McDonaldsMeal_Max
			
			item['MonthlyPass'] = MonthlyPass
			item['MonthlyPass_Min'] = MonthlyPass_Min
			item['MonthlyPass_Max'] = MonthlyPass_Max
			
			item['BasicUtilities'] = BasicUtilities
			item['BasicUtilities_Min'] = BasicUtilities_Min
			item['BasicUtilities_Max'] = BasicUtilities_Max
			
			item['Internet'] = Internet
			item['Internet_Min'] = Internet_Min
			item['Internet_Max'] = Internet_Max
			
			item['FitnessClub'] = FitnessClub
			item['FitnessClub_Min'] = FitnessClub_Min
			item['FitnessClub_Max'] = FitnessClub_Max
			
			item['Childcare'] = Childcare
			item['Childcare_Min'] = Childcare_Min
			item['Childcare_Max'] = Childcare_Max
			
			item['Jeans'] = Jeans
			item['Jeans_Min'] = Jeans_Min
			item['Jeans_Max'] = Jeans_Max
			
			item['SummerDress'] = SummerDress
			item['SummerDress_Min'] = SummerDress_Min
			item['SummerDress_Max'] = SummerDress_Max
			
			item['RunningShoes'] = RunningShoes
			item['RunningShoes_Min'] = RunningShoes_Min
			item['RunningShoes_Max'] = RunningShoes_Max
			item['Boots'] = Boots
			item['Boots_Min'] = Boots_Min
			item['Boots_Max'] = Boots_Max
			item['Rent1Br_CityCenter'] = Rent1Br_CityCenter
			item['Rent1Br_CityCenter_Min'] = Rent1Br_CityCenter_Min
			item['Rent1Br_CityCenter_Max'] = Rent1Br_CityCenter_Max
			item['Rent1Br_OutsideCenter'] = Rent1Br_OutsideCenter
			item['Rent1Br_OutsideCenter_Min'] = Rent1Br_OutsideCenter_Min
			item['Rent1Br_OutsideCenter_Max'] = Rent1Br_OutsideCenter_Max
			item['Rent3Br_CityCenter'] = Rent3Br_CityCenter
			item['Rent3Br_CityCenter_Min'] = Rent3Br_CityCenter_Min
			item['Rent3Br_CityCenter_Max'] = Rent3Br_CityCenter_Max
			item['Rent3Br_OutsideCenter'] = Rent3Br_OutsideCenter
			item['Rent3Br_OutsideCenter_Min'] = Rent3Br_OutsideCenter_Min
			item['Rent3Br_OutsideCenter_Max'] = Rent3Br_OutsideCenter_Max
			item['BuyApt_CityCenter'] = BuyApt_CityCenter
			item['BuyApt_CityCenter_Min'] = BuyApt_CityCenter_Min
			item['BuyApt_CityCenter_Max'] = BuyApt_CityCenter_Max
			item['BuyApt_OutsideCenter'] = BuyApt_OutsideCenter
			item['BuyApt_OutsideCenter_Min'] = BuyApt_OutsideCenter_Min
			item['BuyApt_OutsideCenter_Max'] = BuyApt_OutsideCenter_Max
			item['MonthlySalary'] = MonthlySalary
			item['ResponseCount'] = ResponseCount

			yield item