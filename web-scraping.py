'''
Example of how to scrape a website using BeautifulSoup.

ATTENTION: no sanitization is done. The website could theoretically 
be compromised at any given moment.

Instructions (Linux):
1) Create a virtual environment: `python3 -m venv somename`
2) Activate the virtual environment: `source somename/bin/activate`
3) Install required libraries: `pip install requests beautifulsoup4` 
4) Execute the script: `python3 web-scraping.py`

'''

import requests
from bs4 import BeautifulSoup

# URL for scraping. This website is designed to allow legal scraping.
url = "https://quotes.toscrape.com/"

# Fetch the information from the URL
webpage = requests.get(url)

# Use BeautifulSoup to parse the information fetched
soup = BeautifulSoup(webpage.content, "html.parser")

# Get all the quotes. Inspecting each quote, we can see 
# only the quotes are surrounded by <span class="text"></span>
for quote in soup.find_all(attrs={'class': 'text'}):
	print(quote.text)