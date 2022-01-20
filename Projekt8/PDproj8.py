# -*- coding: utf-8 -*-

# PWZN Projekt 8
# Paweł Dębowski

import requests
from bs4 import BeautifulSoup
import os
import time
import threading

# odpalanie z terminala - python PDproj8.py  

# funkcja pobierania
def pobieranie(adres, kod):
    obrazek = link + '/' + adres
    print(obrazek)
    with open(file_path + '/' + kod + adres, 'wb') as handler:
        handler.write(requests.get(obrazek).content)

# stałe
file_path = os.path.dirname(os.path.abspath(__file__))
link = 'http://www.if.pw.edu.pl/~mrow/dyd/wdprir' 
url = requests.get(link)
soup = BeautifulSoup(url.text,"html.parser")
adresy = []

# adresy do obrazków
for a in soup.find_all('a', href=True):
    if a["href"][a["href"].rfind(".")+1:] in ['png']:
        adresy.append(a["href"])
print(adresy)

# (1) pobieranie klasycznie
t = time.time()
for img in adresy:
    pobieranie(img,'1')
print('Zadanie klasycznie zajęło ' + str(time.time()-t))

# (2) ppobieranie wielowątkowe
t = time.time()
threads = []
for img in adresy:
    threads.append(threading.Thread(target=pobieranie, args=(img, '2')))
for p in threads:
    p.start()
for p in threads:
    p.join()
print('Zadanie wielowątkowo zajęło ' + str(time.time()-t))

# średnio wychodzi trzy/cztery razy szybciej
