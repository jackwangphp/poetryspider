import scrapy
from bs4 import BeautifulSoup


class ShixiSpride(scrapy.Spider):
    name = 'shixi'

    def start_requests(self):
        urls = []
        for i in range(8):
            urls.append('https://www.shixiseng.com/interns/st-intern_c-110100_?k=PHP&p=%d' % (i+1))
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        for url in urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        datas = soup.find_all('li', 'font')
        # for title in datas:
        #     print(title.string)
