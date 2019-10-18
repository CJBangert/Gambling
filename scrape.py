
import pandas as pd
import requests
from bs4 import BeautifulSoup


def scrape_live_data:

	base_url = "https://io.oddsshark.com/upcoming/us2/nba?_=1571350544283"

	headers = {

	    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
		'Accept' : 'application/json, text/javascript, */*; q=0.01',
		'Accept-Language': 'en-US,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate, br',
		'Referer': 'https://www.oddsshark.com/nba/game-logs'
	}

	res = requests.get(base_url, headers = headers)

	f = open("page.html","w+")

	soup = BeautifulSoup(res.content, 'html5lib')

	f.write("%s" % res.content)

	f.close()

# table = soup.find('div', attrs = {'id':'block-system-main'}) 

# #table = soup.find("div",{"id":"block-system-main"}).find("ul",{"class":"list"}).find_all("li")

# print("Table:")
# print(table) 

