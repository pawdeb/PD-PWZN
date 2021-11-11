# -*- coding: utf-8 -*-

# PWZN Projekt 2
# Paweł Dębowski

import argparse
import numpy as np
from numpy import random

from rich.console import Console
import rich.traceback
from rich.progress import track

from PIL import Image,ImageDraw
from matplotlib import cm

import datetime
import os

# python PDproj2.py 50 50 5 5 8 25

class Symulacja:
    def __init__(self):
        self._list = []
    
    def add_to_list(self,klatka):
        self._list.append(klatka)

    def __iter__(self):
        for e in self._list:
            yield e

parser = argparse.ArgumentParser(description="Mój piękny i wspaniały projekt 2 na PWZN")
parser.add_argument('a', help = 'pionowy wymiar siatki', type=int)
parser.add_argument('b', help = 'poziomy wymiar siatki', type=int)
parser.add_argument('j', help = 'wartość J', type=int)
parser.add_argument('beta', help = 'parametr beta', type=int)
parser.add_argument('h', help = 'wartość pola H', type=int) #nieuzywane
parser.add_argument('ile', help = 'liczba kroków symulacji', type=int)
parser.add_argument('-nazwa', '--nazwaklatki', help = 'prefiks nazwy pliku pojedynczej klatki',type=str, default='step')
args = parser.parse_args()

inicjalizacja = 'Siatka ' + str(args.a) + ' x ' + str(args.b) + ' przy J = ' + str(args.j) + ', parametrze beta = ' + str(args.beta) + ' i polu H = ' + str(args.h) + ' wykona się dla ' + str(args.ile) + ' kroków symulacji'
print(inicjalizacja)

a = args.a
b = args.b
model = np.random.randint(2, size=(a,b))
model[model == 0] = -1
print(model)

sym = Symulacja()
kod = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
lok = os.path.dirname(os.path.realpath(__file__))
path = lok + '/' + kod
os.mkdir(path)

def Wizualizator(model):
    image = Image.new('RGB', (a*25,b*25), (0,0,0))
    draw = ImageDraw.Draw(image)
    for i in range(a):
        for k in range(b):
            if model[i][k] == 1:
                draw.rectangle((i*25,k*25,(i+1)*25,(k+1)*25),(255,255,255))
    return image

klatka = Wizualizator(model)
sym.add_to_list(klatka)

# MONTE CARLO
j = args.j
beta = args.beta
ile = args.ile
for i in track(range(ile)):
   for k in range(a*b):
       r1 = np.random.randint(a)
       r2 = np.random.randint(b)
       org = model[r1][r2]
       # warunki brzegowe
       if r1 == a-1: 
           sas1=0
       else: 
           sas1 = model[r1+1][r2]
       if r1 == 0: 
           sas2=0
       else:
           sas2 = model[r1-1][r2]
       if r2 == b-1:
           sas3=0
       else:
           sas3 = model[r1][r2+1]
       if r2 == 0:
           sas4=0
       else:
           sas4 = model[r1][r2-1]
       E0 = np.sum([(-j*org*sas1), (-j*org*sas2), (-j*org*sas3), (-j*org*sas4)])
       flip = org*(-1)
       E1 = np.sum([(-j*flip*sas1), (-j*flip*sas2), (-j*flip*sas3), (-j*flip*sas4)])
       dE = E1-E0
       if dE < 0:
           model[r1][r2] = flip
       else:
           p = np.exp(-beta*dE)
           r3 = np.random.uniform()
           if r3 < p:
               model[r1][r2] = flip
   klatka = Wizualizator(model)
   sym.add_to_list(klatka)
print(model)

numerek = 0
for element in sym:
    nazwa=path + '/' + str(args.nazwaklatki) + str(numerek) + '.png'
    element.save(nazwa)
    numerek+=1
