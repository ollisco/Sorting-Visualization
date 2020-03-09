"""
Created on 2019-11-17

Project: skola
@author: ollejernstrom
"""

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

    return lista

