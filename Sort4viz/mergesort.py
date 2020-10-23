"""
Created on 2020-03-09

Project: sortingvisualization
@author: ollejernstrom
"""
import random


def merge_sort(lst):
    current_size = 0

    for i in range(len(lst)):
        lst[i] = [lst[i]]

    # Storleken av nya listan
    size = len(lst) // 2 + len(lst) % 2
    new = [0] * size

    while len(new) > 1:
        new = [0] * size
        # pointer för listan new
        p1 = 0
        # Mergear två listor och placerar i new
        for i in range(0, len(lst) - 1, 2):
            r = merge(lst[i], lst[i + 1])
            new[p1] = r
            p1 += 1

        # om det finns ett element kvar (liststorleken är udda)
        if p1 < size:
            new[-1] = lst[-1]

        lst = new.copy()
        size = len(lst) // 2 + len(lst) % 2
        yield lst

    # listan lst har nu bara en lista returnera den
    return lst


def merge(a, b):
    m = len(a)
    n = len(b)
    c = []
    i, j = 0, 0

    while i < m and j < n:
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    for i_index in range(i, m):
        c.append(a[i_index])

    for j_index in range(j, n):
        c.append(b[j_index])
    return c


if __name__ == '__main__':

    l = [random.randint(0, 122) for i in range(200)]
    l = merge_sort(l)

    for i in l:
        print(0, i)
        break

    for i in l:
        print(1, i)
        break

    for i in l:
        print(2, i)
        break
