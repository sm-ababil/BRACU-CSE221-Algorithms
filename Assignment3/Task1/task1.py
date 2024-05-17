import numpy as np

inp = open('input1.txt', 'r')
out = open('output1.txt', 'w')

n = int(inp.readline())
arr = np.array(list(map(int, inp.readline().split())))


def merge(left, right):
    arr2 = np.zeros(len(left)+len(right), dtype=int)
    l = 0
    i = 0
    j = 0

    while l < len(arr2):
        if i != len(left) and j != len(right):
            if left[i] < right[j]:
                arr2[l] = left[i]
                i += 1
            elif left[i] > right[j]:
                arr2[l] = right[j]
                j += 1
            else:
                arr2[l] = left[i]
                l += 1
                arr2[l] = right[j]
                i += 1
                j += 1
        else:
            if i == len(left):
                arr2[l] = right[j]
                j += 1
            else:
                arr2[l] = left[i]
                i += 1
        l += 1

    return arr2


def merge_sort(arr1):
    if len(arr1) <= 1:
        return arr1
    else:
        mid = len(arr1) // 2
        left = merge_sort(arr1[:mid])
        right = merge_sort(arr1[mid:])
        return merge(left, right)


ans = merge_sort(arr)
for i in ans:
    out.write(f"{i} ")

inp.close()
out.close()
