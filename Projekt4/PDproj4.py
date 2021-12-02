# -*- coding: utf-8 -*-

# PWZN Projekt 4
# Paweł Dębowski

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

from collections import Counter

import json

# import argparse
# parser = argparse.ArgumentParser(description="Mój piękny i wspaniały projekt 4 na PWZN")
# parser.add_argument('nazwa', help = 'nazwa pliku wyjściowego JSON', type=str)
# args = parser.parse_args()
# nazwa = args.nazwa + '.json'

nazwa = 'output'
print('Tworzę plik ' + nazwa)

options = Options()
options.add_argument('--disable-notifications')

driver = webdriver.Chrome('C:/Users/test/Desktop/PWZN/4/chromedriver.exe', options = options)
driver.get('https://www.reddit.com/r/travel')

button = driver.find_element(By.XPATH, '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[3]/div[1]/section/div/section/section/form[2]/button')
button.click()
time.sleep(2)

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("poland")
elem.send_keys(Keys.RETURN)
time.sleep(2)

for i in range(5):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)
time.sleep(2)

tekst = driver.find_element_by_xpath("/html/body").text

time.sleep(2)
driver.close()

dane = tekst.split()
dane = list(filter(lambda i: len(i) >= 3, dane))
counts = Counter(dane)
print(counts)

result = [{'name':key, 'value':value} for key,value in counts.items()]
with open(nazwa,'w') as f:
    json.dump(result,f)
