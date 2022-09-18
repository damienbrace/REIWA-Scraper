from urllib import response
import requests
from bs4 import BeautifulSoup


response = requests.get("https://reiwa.com.au")
html = response.text
soup = BeautifulSoup(html, 'html.parser')

noOfHouses = soup.find("div", {"class": "homeSearch-propertyCounts"})
noOfHouses = noOfHouses.text.split()[0].split(',')
noOfHouses = int(noOfHouses[0] + noOfHouses[1])
print(noOfHouses)

