import scrapy
from ..items import PoetryItem

class PoetrySpider(scrapy.Spider):
    name = "poetry"
    allowed_domains = ["gushiwen.org"]
    start_urls = [
        "https://www.gushiwen.org/shiwen/default_0A0A1.aspx"
    ]

    def parse(self, response):
        for poetry in response.css(".left .cont"):
            item = PoetryItem()
            item['title'] = poetry.css("b::text").extract()
            item['dynasty'] = poetry.css(".source a:nth-child(1)::text").extract()
            item['poet'] = poetry.css(".source a:nth-child(3)::text").extract()
            item['content'] = poetry.css(".contson").extract()
            yield item

        nextpageurl = 'https://www.gushiwen.org' + response.css("a.amore::attr(href)").extract()[0]
        if nextpageurl:
            print(nextpageurl)
            yield scrapy.Request(nextpageurl, callback=self.parse)

