import numpy as np

inp = open('input2a.txt', 'r')
out = open('output2a.txt', 'w')

l1 = int(inp.readline())
arr1 = np.array(inp.readline().split())
l2 = int(inp.readline())
arr2 = np.array(inp.readline().split())

l = l1 + l2
arr = np.zeros(l, dtype=int)

for i in range(l):
    if i < l1:
        arr[i] = int(arr1[i])
    else:
        arr[i] = int(arr2[i-l1])


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        a = merge_sort(arr[:mid])
        b = merge_sort(arr[mid:])
        arr2 = np.zeros(len(arr), dtype=int)

        k = 0
        i = 0
        j = 0

        while k < len(arr):
            if i != len(a) and j != len(b):
                if a[i] < b[j]:
                    arr2[k] = a[i]
                    i+=1
                elif a[i] > b[j]:
                    arr2[k] = b[j]
                    j+=1
                else:
                    arr2[k] = a[i]
                    k+=1
                    arr2[k] = b[j]
                    i+=1
                    j+=1

            else:
                if i == len(a):
                    arr2[k] = b[j]
                    j+=1
                else:
                    arr2[k] = a[i]
                    i+=1
            k += 1

        return arr2


arr3 = merge_sort(arr)
for i in range(l):
    out.write(str(arr3[i])+" ")

inp.close()
out.close()
