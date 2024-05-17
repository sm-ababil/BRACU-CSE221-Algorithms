import numpy as np

inp = open("input6.txt", 'r')
out = open("output6.txt", 'w')

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


def quick_sort(arr1, l, r, k):
    if l == r:
        return arr1[l]

    pvt = partition(arr1, l, r)
    if k == pvt:
        return arr1[pvt]
    elif k < pvt:
        return quick_sort(arr1, l, pvt - 1, k)
    else:
        return quick_sort(arr1, pvt + 1, r, k)


q = int(inp.readline())

for i in range(q):
    k = int(inp.readline())
    ks = quick_sort(arr, 0, n - 1, k - 1)
    out.write(str(ks) + '\n')

inp.close()
out.close()
