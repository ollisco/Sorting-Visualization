"""
Created on 2019-11-05

Project: skola
@author: ollejernstrom
"""
import random

def är_sorterad(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            sorterad = False
        sorterad = True

def bogosort(lista):
    if not är_sorterad(lista):
        random.shuffle(lista)
        return lista


lista = [4, 3, 2, 1]
bogosort(lista)
print(lista)