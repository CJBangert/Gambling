
import pandas as pd
import requests
from bs4 import BeautifulSoup

BASE_LOGS_URL = "https://www.oddsshark.com/nba/game-logs"

def getLogHeaders(referer):

	return {

	    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
		'Accept' : 'application/json, text/javascript, */*; q=0.01',
		'Accept-Language': 'en-US,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate, br',
		'Referer': referer
	}

def scrape_live_data():

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

def scrape_log_url():
	#gets the url component for each team's game log

	headers = getLogHeaders('https://www.oddsshark.com/nba/game-logs')

	res = requests.get(BASE_LOGS_URL, headers = headers)

	soup = BeautifulSoup(res.content, 'html5lib')

	table = []

	table = soup.find("div",{"id":"block-system-main"}).find("div",{"class":"content"}).find_all("li")

	linkPartsTable = [] 

	for x in range(0, len(table)):

		linkPartsTable.append(table[x].a['href'])
		#print(linkPartsTable[x])
		
	return linkPartsTable



def scrape_game_log_data():

	linkParts = scrape_log_url()

	headers = getLogHeaders('https://www.oddsshark.com/nba/game-logs')

	#for x in linkParts:

	url = "https://www.oddsshark.com/" + linkParts[0]

	res = requests.get(url, headers)

	soup = BeautifulSoup(res.content,'lxml')

	table = soup.find_all('table')[0]

	df = pd.read_html(str(table))

	print(df)

	# f = open("page.html","w+")

	# f.write("%s" % res.content)

	# f.close()




scrape_game_log_data()


# table = soup.find('div', attrs = {'id':'block-system-main'}) 

# #table = soup.find("div",{"id":"block-system-main"}).find("ul",{"class":"list"}).find_all("li")

# print("Table:")
# print(table) 

