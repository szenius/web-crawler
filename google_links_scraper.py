import scrapy
import sys

class LinkSpider(scrapy.Spider):
    name = "google_links_spider"
    start_urls = ["https://www.google.com/search?q=diabetes&num=100", "https://www.google.com/search?q=diabetes+q%26&num=100"]

    def parse(self, response):
        # Get all links
        hxs = scrapy.Selector(response)
        all_links = hxs.xpath('*//a/@href').extract()
        links = []
        for link in all_links:
            if str(link).startswith('/url?q=') and "webcache.googleusercontent.com" not in str(link) and "diabetes" in link:
                links.append(link.replace("/url?q=", "", 1).split("&sa=")[0])   

        links = list(set(links))     

        # Write links to file
        with open('google_links.txt', 'a+') as f:
            for link in links:
                f.write("{}\n".format(link))