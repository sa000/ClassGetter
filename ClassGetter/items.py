# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy.item import Item, Field

class ClassItem(scrapy.Item):
 #major=scrapy.Field()
 ##	urlLink=scrapy.Field()
 	course=scrapy.Field()

class ProfessorItem(scrapy.Item):
	ProfessorName=scrapy.Field()