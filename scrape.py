
import pandas as pd
import requests
from bs4 import BeautifulSoup

base_url = "http://www.oddshark.com"

res = requests.get(base_url + "/nba/game-logs")

print(res.content)

soup = BeautifulSoup(res.content, "html.parser")

table = soup.find("div",{"id":"block-system-main"}).find("ul",{"class":"list"}).find_all("li")

print("Table:")
print(table) 

