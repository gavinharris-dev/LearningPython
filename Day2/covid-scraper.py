from email.mime import base
import string
from urllib import request
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests


url = "https://en.wikipedia.org/wiki/List_of_countries_by_average_wage"

# years = [
#     [2000, 2],
#     [2005, 3]
# ]

def get_salaries(row, headings):
    result = {}
    
    tds = row.find_all("td")
    
    
    for idx, heading in enumerate(headings):
        if idx == 0:
            continue
    
        
        result[heading["title"]] = int(tds[heading["position"]].getText().replace(",", "").replace("\n", ""))
            
    
    
    # for idx, td in enumerate(tds):
    #     if idx == 0:
    #         continue
    
    #     if (td != None):
    #         text = td.getText().replace(",", "").replace("\n", "")
            
    #         if(text.isnumeric):
    #             result.append(text)
    
    return result

def year_headers(table):
    
    ths = table.find_all("th")
    
    headings = []
    
    for idx, th in enumerate(ths):
        if th != None:
            headings.append({
                "title": th.getText().replace("\n", ""),
                "position": idx
            })
    
    return headings
    
def process(soup):
    salaries_table = soup.find("table", class_="wikitable")
    
    headings = year_headers(salaries_table)

    sal_rows = salaries_table.find_all("tr")
    countries_dict = {}
    
    
    for sal_row in sal_rows:
        
        # Get country name
        
        country_name = sal_row.find("a")
        
        if (country_name != None):
            country_name = country_name.getText().replace("\u202f*", "")
            countries_dict[country_name] = get_salaries(sal_row, headings)
        
    return countries_dict
    # print(sal_rows)
    

def scraper(url): 
    
    response = requests.get(url)

    return process(BeautifulSoup(response.content, "html.parser"));
    
    

    
data = scraper(url)

print(data["United Kingdom"]["2005"])