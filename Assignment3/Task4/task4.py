import numpy as np

inp = open('input4.txt', 'r')
out = open('output4.txt', 'w')

n = int(inp.readline())
arr = np.array(list(map(int, inp.readline().split())))


def maximum(l, r, ml, mr):
    if ml > mr:
        m = ml
    else:
        m = mr

    arr2 = np.zeros(len(l) + len(r), dtype=int)

    mx = l[0]
    arr2[0] = l[0]
    for i in range(1, len(l)):
        if l[i] > mx:
            mx = l[i]
        arr2[i] = l[i]

    i = 0
    while i < len(r):
        if m < mx + r[i]**2:
            m = mx + r[i]**2
        arr2[len(l)+i] = r[i]
        i += 1

    return arr2, m


def dev_conqr(arr1, max1=0):
    if len(arr1) <= 1:
        return arr1, arr1[0]
    mid = len(arr1) // 2
    left, ml = dev_conqr(arr1[:mid], max1)
    right, mr = dev_conqr(arr1[mid:], max1)
    return maximum(left, right, ml, mr)


out.write(f"{dev_conqr(arr)[1]}")

inp.close()
out.close()
