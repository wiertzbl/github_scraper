from pathlib import Path

import scrapy


import scrapy

class GithubSpider(scrapy.Spider):
    name = 'github'
    start_urls = ['https://github.com/explore']

    def parse(self, response):
        for repo in response.css('article.Box-row'):
            yield {
                'name': repo.css('h3 a::text').get(),
                'description': repo.css('p::text').get()
            }

        next_page = response.css('a.btn:nth-child(2)::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
