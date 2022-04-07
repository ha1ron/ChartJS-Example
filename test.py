import time

import requests
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import sys

base_url = 'https://www.alta.ru'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.set_window_size(1200, 900)
driver.get("https://www.alta.ru/railway/country/20/")

time.sleep(15)

all_roads = ['https://www.alta.ru/railway/83/', 'https://www.alta.ru/railway/51/', 'https://www.alta.ru/railway/88/',
             'https://www.alta.ru/railway/61/', 'https://www.alta.ru/railway/63/', 'https://www.alta.ru/railway/58/',
             'https://www.alta.ru/railway/28/', 'https://www.alta.ru/railway/01/', 'https://www.alta.ru/railway/96/',
             'https://www.alta.ru/railway/17/', 'https://www.alta.ru/railway/94/', 'https://www.alta.ru/railway/76/',
             'https://www.alta.ru/railway/24/', 'https://www.alta.ru/railway/99/', 'https://www.alta.ru/railway/92/',
             'https://www.alta.ru/railway/85/', 'https://www.alta.ru/railway/80/', 'https://www.alta.ru/railway/91/',
             'https://www.alta.ru/railway/10/']

# all_roads = ['https://www.alta.ru/railway/83/', 'https://www.alta.ru/railway/51/', 'https://www.alta.ru/railway/88/']

result = []
for road in all_roads:
    driver.get(road)
    pageSource = driver.page_source
    soup = BeautifulSoup(pageSource, 'lxml')
    links = soup.find_all('a', class_='pRailway_item')

    print(links)

    href = []
    for link in links:
        href.append(link.get('href'))

    print(href)
    for iterator in href:
        url = base_url + iterator

        driver.get(url)

        soup = BeautifulSoup(driver.page_source, 'lxml')
        data = soup.find_all('div', class_='pRailway_column')

        esr = ''
        coord = ''
        name_st = ''
        for line in data:
            if 'Код ECP' in line.text:
                esr = line.text
            if 'Наименование' in line.text:
                name_st = line.text
            if 'Широта' in line.text:
                coord = line.text

        try:
            res_line = {'ECR': esr.split()[2], 'NAME': name_st.split()[1], 'LAT': coord.split()[1], 'LON': coord.split()[3]}
            result.append(res_line)
        except IndexError:
            print(url)

        # print(res_line)
        # sys.exit()

z = pd.DataFrame(result)
z.to_excel("file_name.xlsx")
print(result)
print(len(result))

