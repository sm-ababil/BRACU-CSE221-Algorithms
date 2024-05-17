import numpy as np

inp = open('input1a.txt', 'r')
out = open('output1a.txt', 'w')

line = inp.readline().split()
l, s = int(line[0]), int(line[1])

arr = np.array(inp.readline().split())

flag = False
for i in range(l):
    for j in range(i+1, l):
        if int(arr[i]) + int(arr[j]) == s:
            out.write(f"{i+1} {j+1}")
            flag = True
            break
    if flag:
        break

if not flag:
    out.write("IMPOSSIBLE")

inp.close()
out.close()


