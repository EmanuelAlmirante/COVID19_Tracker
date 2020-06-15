import requests
import urllib3.request
import time
from bs4 import BeautifulSoup


def webscraper(country):
    url = 'https://www.worldometers.info/coronavirus/'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    soup.findAll('tr')

