import numpy as np

inp = open('input1.txt', 'r')
outp = open('output1.txt', 'w')

l = int(inp.readline())
arr = np.array(map(int, inp.readline().split()))


def mergesort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        left = mergesort(arr[:mid])
        right = mergesort(arr[mid:])

        l = 0
        i = 0
        j = 0

        arr2 = np.zeros(len(arr), dtype=int)

        while l < len(arr):
            if
            if left[i] < right[j]:
                arr2[l] = left[i]
                i+=1
            elif left[i] > right[j]:
                arr2[l] = right[j]
                j+=1
            else:



