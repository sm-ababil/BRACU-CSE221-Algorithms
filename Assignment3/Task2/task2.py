import numpy as np

inp = open('input2.txt', 'r')
out = open('output2.txt', 'w')

l1 = int(inp.readline())
arr1 = np.array(inp.readline().split())
l2 = int(inp.readline())
arr2 = np.array(inp.readline().split())

arr3 = np.zeros(l1+l2, dtype=int)

#O(n)
for i in range(l1+l2):
    if i<l1:
        arr3[i] = int(arr1[i])
    else:
        arr3[i] = int(arr2[i-l1])

arr4 = sorted(arr3)

for i in range(l1+l2):
    out.write(f"{arr4[i]} ")
