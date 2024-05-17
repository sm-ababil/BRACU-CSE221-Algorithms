import numpy as np

inp = open('input2.txt', 'r')
out = open('output2.txt', 'w')

n = int(inp.readline())
arr = np.array(list(map(int, inp.readline().split())))


def maximum(l, r):
    max1 = np.zeros(1, dtype=int)

    if l[0] > r[0]:
        max1[0] = l[0]
    else:
        max1[0] = r[0]

    return max1


def div_conqr(arr1):
    if len(arr1) == 1:
        return arr1
    else:
        mid = len(arr1) // 2
        left = div_conqr(arr1[:mid])
        right = div_conqr(arr1[mid:])
        return maximum(left, right)


out.write(f"{div_conqr(arr)[0]}\n")

inp.close()
out.close()
