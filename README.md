# Web Crawler 
This is a web crawler designed to fetch Google links via a Google search, then fetch the content from these links.

## Installation
This project was developed with `Python 3.6.8`. Please make sure an equivalent version is installed. 

Also install the necessary dependencies by running
```
pip install -r requirements.txt
```

## Developer's Guide

### Getting Google Results as Links
To get the Google links, run the following.
```
scrapy runspider google_links_scraper.py
```
* `start_urls` in `google_links_scraper.py` should be changed accordingly for your desired Google Searches.
    * For example, `https://www.google.com/search?q=diabetes&num=100` queries for the keyword "diabetes" and requests a maximum of 100 results. 
* The resulting links will be saved in an output file called `google_links.txt`.

### Scraping Content from Links
To scrape the content from the links in `google_links.txt`, run the following.
```
scrapy runspider content_scraper.py
```
* The scraped content from each webpage will be saved in an individual HTML file in `./data/`. Make sure the `./data/` directory exists in the root directory before running this script.

## Archive
The `./archive/` directory stores zip folders of previously scraped data. The file naming convention is `data-YYDDMM.zip`.