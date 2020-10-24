"""
Created on 2019-11-05

Project: skola
@author: ollejernstrom
"""


def bubble_sort(lst):
    # Kopierar lstn ifall man vill använda gamla
    steps = [lst.copy()]
    swaped = True
    while swaped:
        swaped = False
        for i, tal in enumerate(lst):
            # Stoppar forloopen om det är sista värdet i lstn
            if i == len(lst) - 1:
                break
            # Om det första talet är större än det andra byt plats
            if tal > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]

                swaped = True
        steps.append(lst.copy())
    return steps, lst

if __name__ == '__main__':
    l = [3, 1, 4, 2, 7]
    steps, l = bubble_sort(l)
    print(steps)
    for i in steps:
        print(i)