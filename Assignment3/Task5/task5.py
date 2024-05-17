import numpy as np

inp = open("input5.txt", 'r')
out = open("output5.txt", 'w')

n = int(inp.readline().strip())
arr = np.array(list(map(int, (inp.readline().split()))))


def partition(arr2, l, r):
    pvt = arr2[r]
    j = l - 1
    for i in range(l, r):
        if arr2[i] <= pvt:
            j += 1
            arr2[i], arr2[j] = arr2[j], arr2[i]
    arr2[j+1], arr2[r] = arr2[r], arr2[j+1]
    return j+1


def quick_sort(arr1, l, r):
    if l < r:
        q = partition(arr1, l, r)
        quick_sort(arr1, l, q-1)
        quick_sort(arr1, q+1, r)


quick_sort(arr, 0, n-1)
for i in range(n):
    out.write(f"{arr[i]} ")

inp.close()
out.close()
