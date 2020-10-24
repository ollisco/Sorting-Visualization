
import random

def check_sort(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
        return True


def bogosort(lst):

    while not check_sort(lst):
        random.shuffle(lst)
        return lst, []


lista = [4, 3, 2, 1]
bogosort(lista)
print(lista)