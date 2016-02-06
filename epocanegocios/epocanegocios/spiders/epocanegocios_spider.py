import scrapy

from epocanegocios.items import EpocanegociosItem

class EpocanegociosSpider(scrapy.Spider):
	name = "epoca"
	allowed_domains = ["http://epocanegocios.globo.com"]
	start_urls = [
	"http://epocanegocios.globo.com/Brasil/index.html",
	]
	def parse(self, response):
		for sel in response.xpath('//ul/li'):
        		item = EpocanegociosItem()
        		item['titulo'] = sel.xpath('//a/h2/@title').extract()
        		item['link'] = sel.xpath('//article/a/@href').extract()
        		yield item