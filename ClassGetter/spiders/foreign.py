# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from ClassGetter.items import ProfessorItem
import re
class foreignSpider(scrapy.Spider):
    name = "foreign"
    allowed_domains = ["emory.edu"]
    start_urls = (
        'http://mesas.emory.edu/home/people/south_asia_faculty.html',
        'http://mesas.emory.edu/home/people/associated_faculty.html'
    )

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        professors=hxs.xpath('//*[@id="main-content"]/div/ul/li/a/text()').extract()
        for professor in professors:
            item=ProfessorItem()
            item['ProfessorName']=professor
            print item['ProfessorName']
            yield item
        

