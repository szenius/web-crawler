import scrapy
import sys

class ContentSpider(scrapy.Spider):
    name = "content_spider"    
    start_urls = []
    with open("google_links.txt", 'r') as f:
        start_urls = f.read().splitlines()
    start_urls = list(set(start_urls))

    def parse(self, response):
        # Write response into file
        filename = "".join(["./data/", response.url.split("/")[-2], ".html"])
        with open(filename, 'wb') as f:
            f.write(response.body)

        # Go to any links found in this page
        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )