# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from ClassGetter.items import ProfessorItem
import re
class profSpider(scrapy.Spider):
    name = "prof"
    allowed_domains = ["emory.edu"]
    start_urls = (
        'http://catalog.college.emory.edu/department-program/faculty.html',
    )

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        professors=hxs.xpath('//*[@id="alpha-group"]/div/div/div/span/div/strong/text()').extract()
        for professor in professors:
            item=ProfessorItem()
            item['ProfessorName']=professor
            print item['ProfessorName']
            yield item
        

