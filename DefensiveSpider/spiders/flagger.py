# -*- coding: utf-8 -*-
import scrapy


class FlaggerSpider(scrapy.Spider):
    name = 'flagger'
    allowed_domains = ['mbcet.ac.in']
    start_urls = ['https://mbcet.ac.in/']

    def parse(self, response):
    	next_page_urls = response.css('a::attr(href)').extract()
    	raw_result = response.css('*::text').extract()
    	for i in raw_result:
        	i = i.strip().lower()
        	keywords = ["openlabsai", "deep", "learning"]
        	if any(word in i for word in keywords):
        		foundKeywords = []
        		for word in keywords:
        			if word in i:
        				foundKeywords.append(word)
        		scraped_info = {
					'sentence' : i, 
					'keywordsFound': foundKeywords, 
					'url' : response.request.url
				}
        		yield scraped_info

    	for url in next_page_urls:
        	if url[0] != "#":
	            yield scrapy.Request(
	            response.urljoin(url),
	            callback=self.parse)