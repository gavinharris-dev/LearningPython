from email.mime import base
import string
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from selenium import webdriver

# def country_data_cleanup(data):
    

def takeCountryName(elem):
    return elem["name"];


def countries_data_cleanup(countries_data_outer_html):
    countries_data_list = []
    
    for countries_data_inner_html in countries_data_outer_html:
        country_data_dict = {
            "name": "",
            "total-cases": "",
            "new-cases": "",
            "total-deaths": "",
            "new-deaths": ""
        }
        
        country_name = countries_data_inner_html.find("a", class_="mt_a")
        
        if country_name != None:
            country_data_dict["name"] = country_name.getText()
        else:
            continue
        
        country_data_dict["total-cases"] = int(countries_data_inner_html.find("td", class_="sorting_1").getText().replace(",", ""))
        
        clean_numbers = True
        base_index = 3
        tds = countries_data_inner_html.find_all("td")
        
        for x in range(4):
            lData = tds[x + base_index].getText().replace(",", "")
            if lData == "" or lData in string.ascii_uppercase:
                clean_numbers = False
        
        if clean_numbers == True:
            country_data_dict["new-cases"] = int(tds[3].getText().replace(",", ""))
            country_data_dict["total-deaths"] = int(tds[4].getText().replace(",", ""))
            country_data_dict["new-deaths"] = int(tds[5].getText().replace(",", ""))
        else:
            continue
        
        countries_data_list.append(country_data_dict)
    
    return countries_data_list

def interactive_grapher(data_list):
    graph_count = input("How many countries should we graph? ")
    
    countries_to_graph = []
    
    for i in range(int(graph_count)):
        countries_to_graph.append(input("What country would you like to graph? "))
        
    compared_stat = input("What stat should we graph? ")
    
    

def worldometer_scraper():
    url = "https://www.worldometers.info/coronavirus/"
    
    driver = webdriver.Firefox()
    driver.get(url)
    
    html = driver.page_source
    
    soup  = BeautifulSoup(html, "html.parser")
    
    countries_data_outer_html_even = soup.find_all("tr", class_="even")
    countries_data_outer_html_odd  = soup.find_all("tr", class_="odd")
    
    countries_data_outer_html_odd  = soup.find_all("tr", class_=f"{'odd' or 'even'}")

    
    return countries_data_cleanup(countries_data_outer_html_even) + countries_data_cleanup(countries_data_outer_html_odd)

def remove_dups(countries):
    remove_idxs = []
    
    for i, country in enumerate(countries):
        print(i, country)

data = worldometer_scraper()

remove_dups(data)