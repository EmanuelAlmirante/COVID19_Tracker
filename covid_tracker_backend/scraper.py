import json
from datetime import date

import requests
from bs4 import BeautifulSoup


def webscraper(country):
    url = 'https://www.worldometers.info/coronavirus/'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.find_all('tr')

    for tr in rows:
        data_text = tr.text

        if country in data_text:
            parsed_information = data_text.split("\n")

            country = parsed_information[2]
            total_cases = parsed_information[3]
            new_cases = parsed_information[4]
            total_deaths = parsed_information[5]
            new_deaths = parsed_information[6]
            total_recovered = parsed_information[7]
            active_cases = parsed_information[9]
            day = date.today()

            data = {"country": country, "total_cases": total_cases, "new_cases": new_cases,
                    "total_deaths": total_deaths, "new_deaths": new_deaths, "total_recovered": total_recovered,
                    "active_cases": active_cases, "day": day.strftime("%d/%m/%Y")}

            json_data = json.dumps(data)
            return json_data

    return None
