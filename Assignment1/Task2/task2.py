import numpy as np

inp = open('input2.txt','r')
out = open('output2.txt', 'w')

line = int(inp.readline())
arr = np.array(inp.readline().split())


def bubble_sort(line, arr):
    flag = False
    for i in range(line-1):
        if arr[i] > arr[i+1]:
            flag = True
            break
    if flag:
        for i in range(line - 1):
            for j in range(line - i - 1):
                if int(arr[j]) > int(arr[j+1]):
                    temp = int(arr[j])
                    arr[j] = int(arr[j+1])
                    arr[j+1] = temp


bubble_sort(line, arr)

for i in range(line):
    out.write(f"{arr[i]} ")

inp.close()
out.close()