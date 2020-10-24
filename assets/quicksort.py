def partition(arr, strart_index, end_index):
    i = (strart_index - 1)
    x = arr[end_index]

    for j in range(strart_index, end_index):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end_index] = arr[end_index], arr[i + 1]
    return i + 1


def quicksort(arr):
    l = 0
    h = len(arr) - 1
    size = h - l + 1
    stack = [0] * (size)

    top = -1
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    steps = [arr.copy()]

    while top >= 0:

        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1


        p = partition(arr, l, h)


        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
        steps.append(arr.copy())

        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h
        steps.append(arr.copy())

    return steps, arr





