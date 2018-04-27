# -*- coding: utf-8 -*-
import scrapy,logging
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from TencentXiangQing.items import TencentxiangqingItem,TencentxiangqingContent


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = []
    start_urls = ['https://hr.tencent.com/position.php']

    rules = (
        # 通过LinkExtractor发送链接，并通过Rule发送请求
        # 通过Rule发送返回响应，交给callback解析数据，并且继续跟进提取
        Rule(LinkExtractor(allow=r'position\.php\?&start=\d+'),callback='pares_item',follow=True),
        Rule(LinkExtractor(allow=r'position_detail.php\?id=\d+'),callback='pares_position',follow=False)
    )

    def pares_item(self,response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = TencentxiangqingItem()
            item['name'] = each.xpath("./td/a/text()").extract()[0]
            try:
                item['categroy'] = each.xpath("./td[2]/text()").extract()[0]
            except:
                item['categroy'] = ''
            try:
                item['people'] = each.xpath("./td[3]/text()").extract()[0]
            except:
                item['people'] = ''
            try:
                item['address'] = each.xpath("./td[4]/text()").extract()[0]
            except:
                item['address'] = ''
            try:
                item['datetime'] = each.xpath("./td[5]/text()").extract()[0]
            except:
                item['datetime'] = ''
            yield item

    def pares_position(self,response):
        """
        # 工作职责
        //table[@class='tablelist textl']/tr[3]/td/ul/li/text()
        # 工作要求
         //table[@class='tablelist textl']/tr[4]/td/ul/li/text()
        """
        node_list = response.xpath('//table[@class="tablelist textl"]')
        for node in node_list:
            item = TencentxiangqingContent()
            try:
                item['job_responsibility'] = ';'.join(node.xpath('./tr[3]/td/ul/li/text()').extract())
            except:
                item['job_responsibility'] = ''
            try:
                item['work_description'] = ';'.join(node.xpath('./tr[4]/td/ul/li/text()').extract())
            except:
                item['work_description'] = ''
            print('--------------------')
            yield item


