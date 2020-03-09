"""
Created on 2019-11-05

Project: skola
@author: ollejernstrom
"""


def bubble_sort(lista):
    # Kopierar listan ifall man vill använda gamla


    for i, tal in enumerate(lista):
        # Stoppar forloopen om det är sista värdet i listan
        if i == len(lista) - 1:
            break
        # Om det första talet är större än det andra byt plats
        if tal > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            swaped = True

    return lista
