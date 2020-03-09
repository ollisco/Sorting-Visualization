"""
Created on 2019-11-17

Project: skola
@author: ollejernstrom
"""
from random import randrange

def gen_list(storlek):
    lista = []
    for u in range(storlek):
        r = randrange(1, 1000)
        lista.append(r)

    return lista


def insertion_sort(lista):
    for i in range(1, len(lista)):
        # nv = nuvarande
        nv = lista[i]
        for j in range(i-1, -1, -1):
            if lista[j] > nv:
                lista[j+1] = lista[j]
            else:
                j += 1
                break
            lista[j] = nv
            break
    return lista


def insertion(lista):
    for i in range(1, len(lista)):
        for j in range(i-1, -1, -1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                break
            else:
                break
    return lista


# VÄRLDERNS BÄSTA SORTERING
def ollesort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i-1
        while j >= 0 and key < l[j]:
            l[j+1] = l[j]
            j -= 1
            return l

        l[j+1] = key
    return l

q = 1
def qqq(l):
    global q
    for i in range(q, len(l)):
        key = l[i]
        j = i-1
        while j >= 0 and key <= l[j]:
            l[j+1] = l[j]
            j -= 1

        l[j+1] = key
        q += 1
        return l

    return l


