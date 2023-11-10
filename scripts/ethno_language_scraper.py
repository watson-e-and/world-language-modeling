import requests
from bs4 import BeautifulSoup
import re

# s = "views-row views-row-28 views-row-even"
# print(re.compile(r'views-row'))


editions = ["16","17", "18", "19", "20", "21", "22", "23", "25"]

#English : eng
#Chinese Mandarin: cmn
#Hindi: hin
#Spanish: spa
#French: fra
#Bengali: ben
#Portugese: por
#Russian: rus
#Urdu: urd
#Indonesian: ind
#German Standard: deu
#Japanese: jpn
#Nigerian Pidgin: pcm
#Arabic Egyptian: arz
language_codes = ["eng", "cmn", "hin", "spa", "fra", "ben", "por", "rus", "urd", "ind", "deu","jpn", "pcm", "arz"]
code = "arz"
for edition in editions:
    fi = open(f'./data/{edition}{code}.txt', "w")
    URL = f'https://www.ethnologue.com/{edition}/language/{code}/'
    try:
        
        page = requests.get(URL)
        
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
    except:
        print(f'{edition}:{code}')

# fi = open("./data/17eng.txt", "w")

# soup = BeautifulSoup(page.content, "html.parser")
# # print(soup)
# results = soup.find("div", class_="view view-language view-id-language view-display-id-attachment_1")
# countries = results.find_all("div", class_=re.compile(r'views-row*'))
# for country in countries:
#     name = country.find("span", class_="fieldset-legend")
#     name.text.strip()
#     name = name.find("span")
#     name.text.strip()
#     population = country.find("div", class_="field-content")
#     population.text.strip()
#     s = f'{name.text.strip()} \t {population.text.strip()} \n'
#     fi.write(s)
# fi.close()
# print(len(countries))


# views-row
# job_elements = results.find_all("div", class_="card-content")
# for job_element in job_elements:
#     print(job_element, end="\n"*2)
# print(results.prettify())

# for future uses, check this
# https://stackoverflow.com/questions/50202238/python-pip-requestsdependencywarning-urllib3-1-9-1-or-chardet-2-3-0-doe