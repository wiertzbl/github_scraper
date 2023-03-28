from pathlib import Path
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
