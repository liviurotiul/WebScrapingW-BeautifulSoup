'''
A quick little web scraping project that notifies if there are any new in the elder scrolls 6(Beautiful soup)
'''

import os
import bs4
from bs4 import BeautifulSoup as soup
import requests


# the page(s) we are gonna be scraping (mak a list with relevant reddit r/ pages
reddit_site_urls = ['https://www.reddit.com/r/ElderScrolls/', 'https://www.reddit.com/r/skyrim/', 'https://www.reddit.com/r/skyblivion/']

# headers to mimic a browser visit
headers = {'User-Agent': 'Mozilla/5.0'}


for site_url in reddit_site_urls:
	# returns a requests.models.Response object
	page_html = requests.get(site_url, headers=headers)

	# parse the hmtl
	page_soup = soup(page_html.text, "html.parser")

	# reddit gets its titles in h3 tags so it's easy to find
	threads = page_soup.findAll('h3')
	for thread in threads:
		print("-", thread.text) # get the text out of the tag


