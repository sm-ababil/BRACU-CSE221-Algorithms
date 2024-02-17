import numpy as np

inp = open('input.txt', 'r')
out = open('output.txt', 'w')

len1 = int(inp.readline())
arr1 = inp.readline().split()
len2 = int(inp.readline())
arr2 = inp.readline().split()
len3 = int(inp.readline())
arr3 = inp.readline().split()

k = len1 + len2 + len3
arr = np.zeros(k, dtype=int)
# print(arr)

for i in range(k):
    if i < len1:
        arr[i] = int(arr1[i])
    elif len1 <= i < len1+len2:
        arr[i] = int(arr2[i-len1])
    else:
        arr[i] = int(arr3[i-len1-len2])


def merge_sorting(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        a = merge_sorting(arr[:mid])
        b = merge_sorting(arr[mid:])

        arr2 = np.zeros(len(arr), dtype=int)
        l = 0
        i = 0
        j = 0

        while l < len(arr):
            if i != len(a) and j != len(b):
                if a[i] < b[j]:
                    arr2[l] = a[i]
                    i += 1
                elif a[i] > b[j]:
                    arr2[l] = b[j]
                    j += 1
                else:
                    arr2[l] = a[i]
                    l += 1
                    arr2[l] = b[j]
                    i += 1
                    j += 1

            else:
                if i == len(a):
                    arr2[l] = b[j]
                    j += 1
                else:
                    arr2[l] = a[i]
                    i += 1

            l+=1

        return arr2


out.write(str(merge_sorting(arr)))

inp.close()
out.close()


