'''
A quick little web scraping project that notifies if there are any new in the elder scrolls 6(Beautiful soup)
'''

import os
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# the page(s) we are gonna be scraping
site_url = 'https://www.youtube.com/results?search_query=the+elder+scrolls+6&sp=CAMSBAgDEAE%253D'

# get the page and read the html
uClient = uReq(site_url)
page_html = uClient.read()
uClient.close()

# parse the hmtl
page_soup = soup(page_html, "html.parser")
