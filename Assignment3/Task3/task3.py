import numpy as np

inp = open("input3.txt", "r")
out = open("output3.txt", "w")

n = int(inp.readline())
arr = np.array(list(map(int, inp.readline().split())))


def count(l, r, cl, cr):
    arr2 = np.zeros(len(l)+len(r), dtype=int)
    c, k, i, j = 0, 0, 0, 0
    while k < len(arr2):
        if i != len(l) and j != len(r):
            if l[i] < r[j]:
                arr2[k] = l[i]
                i += 1

            elif l[i] > r[j]:
                arr2[k] = (r[j])
                c += len(l) - i
                j += 1

            else:
                arr2[k] = l[i]
                k += 1
                arr2[k] = r[j]
                i += 1
                j += 1
        else:
            if i == len(l):
                arr2[k] = r[j]
                j += 1
            else:
                arr2[k] = l[i]
                i += 1
        k += 1

    return arr2, cl + c + cr


def dev_conqr(arr1, c=0):
    if len(arr1) <= 1:
        return arr1, c
    mid = len(arr1) // 2
    left, cl = dev_conqr(arr1[:mid], c)
    right, cr = dev_conqr(arr1[mid:], c)
    return count(left, right, cl, cr)


out.write(f"{dev_conqr(arr)[0]}")

inp.close()
out.close()
