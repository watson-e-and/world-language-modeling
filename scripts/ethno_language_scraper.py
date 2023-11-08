import requests
from bs4 import BeautifulSoup
import re

# s = "views-row views-row-28 views-row-even"
# print(re.compile(r'views-row'))
URL = "https://www.ethnologue.com/25/language/spa/"
page = requests.get(URL)

fi = open("countries.txt", "w")

soup = BeautifulSoup(page.content, "html.parser")
# print(soup)
results = soup.find("div", class_="view view-language view-id-language view-display-id-attachment_1")
countries = results.find_all("div", class_=re.compile(r'views-row*'))
for country in countries:
    name = country.find("span", class_="fieldset-legend")
    name.text.strip()
    name = name.find("span")
    name.text.strip()
    population = country.find("div", class_="field-content")
    population.text.strip()
    s = f'{name.text.strip()} \t {population.text.strip()} \n'
    fi.write(s)
fi.close()
print(len(countries))


# views-row
# job_elements = results.find_all("div", class_="card-content")
# for job_element in job_elements:
#     print(job_element, end="\n"*2)
# print(results.prettify())

# for future uses, check this
# https://stackoverflow.com/questions/50202238/python-pip-requestsdependencywarning-urllib3-1-9-1-or-chardet-2-3-0-doe