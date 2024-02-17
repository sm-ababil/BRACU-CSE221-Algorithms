import numpy as np

inp = open('input1b.txt', 'r')
out = open('output1b.txt', 'w')

ver, edge = map(int, inp.readline().split())

arr = np.zeros((ver+1, ver+1), dtype=int)

for i in range(edge):
    v1, v2, w = map(int, inp.readline().split())
    arr[v1][v2] = w

for i in range(ver+1):
    out.write(f"{i}: ")
    for j in range(ver+1):
        if arr[i][j] != 0:
            out.write(f"({j}, {arr[i][j]}) ")
    out.write("\n")

inp.close()
out.close()
