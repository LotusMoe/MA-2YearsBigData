import scrapy
from scrapy.selector import Selector
import json
import re

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        for num in range(0, 999999999):
            yield scrapy.Request(url='https://www.example.com/ma/ma?callback=ma&id={0:0>9}'.format(num),
                                 callback=self.parse)

    def parse(self, response):
        sel = Selector(response)
        status = sel.re_first('status":(.*?),')
        print(status)

        if (int(status) == 0):

            maid = response.url.split("=")[-1]
            filename = 'player-%s.json' % maid
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)
