
from SalaryScraper import SalaryScraper

import numpy

url = "https://en.wikipedia.org/wiki/List_of_countries_by_average_wage"

scraper = SalaryScraper(url)

print(scraper.data["Australia"]["2000"])

