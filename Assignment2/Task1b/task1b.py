import numpy as np

inp = open('input1b.txt', 'r')
out = open('output1b.txt', 'w')

line = inp.readline().split()
l, s = int(line[0]), int(line[1])

arr = np.array(inp.readline().split())

a = 0
b = l-1
flag = True
for i in range(l):
    if a == b:
        break
    s2 = int(arr[a]) + int(arr[b])
    if s2 == s:
        out.write(f"{a+1} {b+1}")
        flag = False
        break
    else:
        if s2 < s:
            a += 1
        else:
            b -= 1

if flag:
    out.write("IMPOSSIBLE")

inp.close()
out.close()
