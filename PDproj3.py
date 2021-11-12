# -*- coding: utf-8 -*-

# PWZN Projekt 3
# Paweł Dębowski

import argparse

from rich import console
from rich.console import Console
import rich.traceback

import requests

from bs4 import BeautifulSoup

import json

# python PDproj3.py wyjsciowy

console = Console()
console.clear()
rich.traceback.install()

parser = argparse.ArgumentParser(description="Mój piękny i wspaniały projekt 3 na PWZN")
parser.add_argument('nazwa', help = 'nazwa pliku wyjściowego JSON', type=str)
args = parser.parse_args()

nazwa = args.nazwa + '.json'
console.print('[red]Tworzę[/red] [green]plik[/green] ' + '[blue]' + nazwa + '[/blue]\n')
console.print('[yellow]10 NAJPOPULARNIEJSZYCH KSIĄŻEK DAVIDA MITCHELLA[/yellow]\n')

req = requests.get('https://www.goodreads.com/author/show/6538289.David_Mitchell')
#console.print(req.status_code)

soup = BeautifulSoup(req.text, 'html.parser')
ksiazki = soup.find_all('span', role='heading')
dane = soup.find_all('span', class_='minirating')

ksiazkiL = []
for span in ksiazki:
    ksiazka = span.text
    console.print(ksiazka)
    ksiazkiL.append(ksiazka)
    console.print()

daneL= []
for span in dane:
    dana = span.text
    console.print(dana)
    daneL.append(dana)
    console.print()

slownik = dict(zip(ksiazkiL,daneL))
console.print(slownik)

with open(nazwa,'w') as f:
    json.dump(slownik,f)