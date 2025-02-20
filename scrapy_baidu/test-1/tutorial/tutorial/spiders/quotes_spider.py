import scrapy
import protego

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.tosctape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        print("page = ", page)
        filename = f'quotes-{page}.html'
        print("filename = ", filename)
        with open(filename, 'wb') as f:
            f.write(response.body)
        # self.log(f'Saved file {filename}')