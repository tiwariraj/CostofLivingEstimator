# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CostAmountItem(scrapy.Item):

		# define the fields for your item here like:
		MarketName = scrapy.Field() 
		InexpensiveMeal = scrapy.Field() 
		InexpensiveMeal_Min = scrapy.Field()
		InexpensiveMeal_Max = scrapy.Field()
		ThreeCourseMeal = scrapy.Field() 
		ThreeCourseMeal_Min = scrapy.Field() 
		ThreeCourseMeal_Max = scrapy.Field() 
		McDonaldsMeal = scrapy.Field() 
		McDonaldsMeal_Min = scrapy.Field() 
		McDonaldsMeal_Max = scrapy.Field()
		MonthlyPass = scrapy.Field() 
		MonthlyPass_Min = scrapy.Field() 
		MonthlyPass_Max = scrapy.Field()
		BasicUtilities = scrapy.Field()
		BasicUtilities_Min = scrapy.Field()
		BasicUtilities_Max = scrapy.Field()
		Internet = scrapy.Field()
		Internet_Min = scrapy.Field()
		Internet_Max = scrapy.Field()
		FitnessClub = scrapy.Field()
		FitnessClub_Min = scrapy.Field()
		FitnessClub_Max = scrapy.Field()
		Childcare = scrapy.Field()
		Childcare_Min = scrapy.Field()
		Childcare_Max = scrapy.Field()
		Jeans = scrapy.Field()
		Jeans_Min = scrapy.Field()
		Jeans_Max = scrapy.Field()
		SummerDress = scrapy.Field()
		SummerDress_Min = scrapy.Field()
		SummerDress_Max = scrapy.Field()
		RunningShoes = scrapy.Field()
		RunningShoes_Min = scrapy.Field()
		RunningShoes_Max = scrapy.Field()
		Boots = scrapy.Field()
		Boots_Min = scrapy.Field()
		Boots_Max = scrapy.Field()
		Rent1Br_CityCenter = scrapy.Field()
		Rent1Br_CityCenter_Min = scrapy.Field()
		Rent1Br_CityCenter_Max = scrapy.Field()
		Rent1Br_OutsideCenter = scrapy.Field()
		Rent1Br_OutsideCenter_Min = scrapy.Field()
		Rent1Br_OutsideCenter_Max = scrapy.Field()
		Rent3Br_CityCenter = scrapy.Field()
		Rent3Br_CityCenter_Min = scrapy.Field()
		Rent3Br_CityCenter_Max = scrapy.Field()
		Rent3Br_OutsideCenter = scrapy.Field()
		Rent3Br_OutsideCenter_Min = scrapy.Field()
		Rent3Br_OutsideCenter_Max = scrapy.Field()
		BuyApt_CityCenter = scrapy.Field()
		BuyApt_CityCenter_Min = scrapy.Field()
		BuyApt_CityCenter_Max = scrapy.Field()
		BuyApt_OutsideCenter = scrapy.Field()
		BuyApt_OutsideCenter_Min = scrapy.Field()
		BuyApt_OutsideCenter_Max = scrapy.Field()
		MonthlySalary = scrapy.Field()
		ResponseCount = scrapy.Field()