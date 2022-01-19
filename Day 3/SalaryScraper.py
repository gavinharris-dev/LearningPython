
from email.mime import base
import string
from urllib import request
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests

class SalaryScraper:

    data = {}

    def __init__(self, url):
        self.data = self.__scrape(url)

    def __get_salaries(self, row, headings):
        result = {}
        
        tds = row.find_all("td")
        
        
        for idx, heading in enumerate(headings):
            if idx == 0:
                continue
            
            result[heading["title"]] = int(tds[heading["position"]].getText().replace(",", "").replace("\n", ""))
                
        return result

    def __year_headers(self, table):
        
        ths = table.find_all("th")
        
        headings = []
        
        for idx, th in enumerate(ths):
            if th != None:
                headings.append({
                    "title": th.getText().replace("\n", ""),
                    "position": idx
                })
        
        return headings
        
    def __process(self, soup):
        salaries_table = soup.find("table", class_="wikitable")
        
        headings = self.__year_headers(salaries_table)

        sal_rows = salaries_table.find_all("tr")
        countries_dict = {}
        
        
        for sal_row in sal_rows:
            
            # Get country name
            
            country_name = sal_row.find("a")
            
            if (country_name != None):
                country_name = country_name.getText().replace("\u202f*", "")
                countries_dict[country_name] = self.__get_salaries(sal_row, headings)
            
        return countries_dict
        # print(sal_rows)
        

    def __scrape(self, url): 
        
        response = requests.get(url)

        return self.__process(BeautifulSoup(response.content, "html.parser"));
