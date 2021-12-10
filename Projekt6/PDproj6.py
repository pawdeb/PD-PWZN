# -*- coding: utf-8 -*-

# PWZN Projekt 6
# Paweł Dębowski

import time
from rich.progress import track

def decorator_factory(argument = 1):
    def decorator(function):
        def wrapper(*args, **kwargs):
            suma = 0
            for i in track(range(argument)):
                t1 = time.time()
                result = function(*args, **kwargs)
                t2 = time.time()
                suma = suma + (t2 - t1)
            print(f'Function {function.__name__!r} executed in {suma/argument:.4f}s for {argument} times average')
            return result
        return wrapper
    return decorator

ile = 10
@decorator_factory(ile)
def silnia(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

silnia(100000)
