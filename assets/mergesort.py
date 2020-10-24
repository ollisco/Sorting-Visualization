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
    full_steps = [lst.copy()]
    color_steps = []
    # Storleken av nya listan
    size = len(lst) // 2 + len(lst) % 2
    new = [0] * size

    while len(new) > 1:
        new = [0] * size

        p1 = 0

        merges = [0] * size
        for i in range(0, len(lst) - 1, 2):
            

            r = merge(lst[i], lst[i + 1])

            # get the step
            step = full_steps[-1].copy()
            input_index = int(i/2)
            step[input_index:input_index+2] = [r]
            full_steps.append(step)






            # Add merged list to new
            new[p1] = r
            p1 += 1

        # om det finns ett element kvar (liststorleken är udda)
        if p1 < size:
            new[-1] = lst[-1]

        lst = new.copy()
        size = len(lst) // 2 + len(lst) % 2


    # listan lst har nu bara en lista returnera den
    return full_steps, color_steps  # Neested Cuz the vizualizer is in a nested for loop


def merge(a, b):
    m = len(a)
    n = len(b)
    c = [0]*(m+n)
    i, j, k = 0, 0, 0

    while i < m and j < n:
        if a[i] < b[j]:
            c[k]= a[i]
            i += 1
            k += 1
        else:
            c[k]= b[j]
            j += 1
            k += 1

    for i_index in range(i, m):
        c[k]= a[i_index]
        k += 1
    for j_index in range(j, n):
        c[k] = b[j_index]
        k += 1

    return c


if __name__ == '__main__':

    l = [random.randint(0, 122) for i in range(20)]
   #l = [1,2,3,4,5,6]
    l, s = merge_sort(l)
    print()
    for i in s:
        print(i)




