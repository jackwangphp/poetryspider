import scrapy
from bs4 import BeautifulSoup


class LolSpride(scrapy.Spider):
    name = 'lol'

    def start_requests(self):
        urls = ['https://www.jianshu.com/c/V2CqjW?utm_medium=index-collections&utm_source=desktop', ]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        for url in urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        titles = soup.find_all('a', 'title')
        for title in titles:
            print(title.string)
