# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from ClassGetter.items import ClassItem
import re
class OverallSpider(scrapy.Spider):
    name = "overall"
    allowed_domains = ["emory.edu"]
    start_urls = (
        'http://catalog.college.emory.edu/department-program/departments/index.html',
    )

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        majors=hxs.xpath('//*[@id="department-listing"]/ul/li/a').extract()
        for major in majors:
            #item=ClassItem()
            #item['major']=re.compile('>(.*?)<').search(major).group(1)
            #item['urlLink']=re.search('\w*\.html', major).group(0)
            urlLink=re.search('\w*\.html', major).group(0)
            classLinkforMajor='http://catalog.college.emory.edu/department-program/departments/'+urlLink
            yield scrapy.Request(classLinkforMajor, callback=self.parse_subpage)


    def parse_subpage(self, response):
        hxs=HtmlXPathSelector(response)
        courses=hxs.xpath('//*[@id="courses"]/dl/dd/div/text()').extract()
        for course in courses:
            print course
            item=ClassItem()
            item['course']=course
            yield item


