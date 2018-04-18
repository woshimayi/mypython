class Baidu(CrawlSpider):
	name = 'baidu'
	start_url=['http://www.baidu.com']
	url = 'http://www.baidu.com'

	def parse(self, response):
		selector = Selector(response)