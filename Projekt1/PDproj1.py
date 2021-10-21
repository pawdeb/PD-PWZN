# -*- coding: utf-8 -*-

# PWZN Projekt 1
# Paweł Dębowski

import argparse
from ascii_graph import Pyasciigraph
from collections import Counter

parser = argparse.ArgumentParser(description="Mój piękny i wspaniały projekt 1 na PWZN")
parser.add_argument('plik', help = 'nazwa pliku tekstowego')
parser.add_argument('-ile', help = 'ile najpopularniejszych wyrazów', type = int, default=10)
parser.add_argument('-dlug', '--dlugosc', help = 'minimalna długość słowa', type = int, default=0)
args = parser.parse_args()

tekst = []
with open(args.plik) as f:
    for line in f:
        for word in line.split():
           #print(word)
           tekst.append(word)   

tekst = [s.replace(".", "") for s in tekst]
tekst = [s.replace(",", "") for s in tekst]
tekst = [s.replace("?", "") for s in tekst]
tekst = [s.replace("!", "") for s in tekst]
tekst = [s.replace("*", "") for s in tekst]
tekst = [s.replace("/", "") for s in tekst]

tekst = [l.lower() for l in tekst]
tekst = list(filter(lambda i: len(i) >= args.dlugosc, tekst))

dane = list(Counter(tekst).items())
dane.sort(key= lambda e: e[1], reverse=True)
dane = dane[:args.ile]

graph = Pyasciigraph()
napisladny = 'Histogram ' + str(args.ile) + ' najpopularniejszych słów z ' + args.plik + ' o minimalnej długości ' + str(args.dlugosc)

for line in graph.graph(napisladny, dane):
    print(line)
