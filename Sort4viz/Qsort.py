"""
Created on 2019-11-11

Project: skola
@author: ollejernstrom
"""
from random import randrange
def gen_list(storlek):
    lista = []
    for u in range(storlek):
        r = randrange(1, 10000)
        lista.append(r)

    return lista

def qsort(lista):
    mindre = []
    lika = []
    större = []

    if len(lista) > 1:
        pivot = lista[0]
        for i in lista:
            if i < pivot:
                mindre.append(i)
            elif i == pivot:
                lika.append(i)
            elif i > pivot:
                större.append(i)
        return qsort(mindre) + lika + qsort(större)
    else:
        return lista


