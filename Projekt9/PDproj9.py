# -*- coding: utf-8 -*-

# PWZN Projekt 9
# Paweł Dębowski w oparciu o artykuł
# https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp

import numpy as np
import aiohttp
import asyncio
import time
import requests

poke = 151
adres = 'https://pokeapi.co/api/v2/pokemon/'

# klasycznie
t1 = time.time()
for number in range(1, poke):
    url = adres + str(number)
    resp = requests.get(url)
    pokemon = resp.json()
    print(pokemon['name'])
t2 = time.time()

# asynchronicznie
t3 = time.time()
async def main():
    async with aiohttp.ClientSession() as session:
        for number in range(1, poke):
            url = adres + str(number)
            async with session.get(url) as resp:
                pokemon = await resp.json()
                print(pokemon['name'])
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
t4 = time.time()

# porównanie
print('Pokemony klasycznie ściągają się w ' + str(np.round(t2-t1,2)) + ' sekund')
print('Pokemony asynchronizcnie ściągają się w ' + str(np.round(t4-t3,2)) + ' sekund')
