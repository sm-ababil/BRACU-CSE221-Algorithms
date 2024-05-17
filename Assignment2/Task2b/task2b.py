import numpy as np

inp = open('input2b.txt', 'r')
out = open('output2b.txt', 'w')

l1 = int(inp.readline())
arr1 = np.array(inp.readline().split())
l2 = int(inp.readline())
arr2 = np.array(inp.readline().split())

l = l1 + l2
arr = np.zeros(l, dtype=int)

k = 0
i = 0
j = 0

while k < l:
    if i != l1 and j != l2:
        if int(arr1[i]) < int(arr2[j]):
            arr[k] = int(arr1[i])
            i += 1
        elif int(arr1[i]) > int(arr2[j]):
            arr[k] = int(arr2[j])
            j += 1
        else:
            arr[k] = int(arr1[i])
            k += 1
            arr[k] = int(arr2[j])
            i += 1
            j += 1
    else:
        if i == l1:
            arr[k] = int(arr2[j])
            j+=1
        else:
            arr[k] = int(arr1[i])
            i+=1
    k+=1


for i in range(l):
    out.write(str(arr[i])+" ")

inp.close()
out.close()



