import numpy as np

inp = open('input4.txt', 'r')
out = open('output4.txt', 'w')

l1 = inp.readline().split()
line, person = int(l1[0]), int(l1[1])
arr = np.zeros((line, 2), dtype=int)
arr2 = np.zeros(person, dtype=int)
count = 0

for i in range(line):
    l2 = inp.readline().split()
    arr[i][0], arr[i][1] = int(l2[0]), int(l2[1])


def bubble_sort(line, arr):
    for i in range(line):
        for j in range(line - i - 1):
            if arr[j][1] > arr[j+1][1]:
                arr[j], arr[j+1] = arr[j+1].copy(), arr[j].copy()


bubble_sort(line, arr)

for i in range(line):
    start = arr[i][0]
    end = arr[i][1]
    min_d = arr2[0] - start
    for j in range(person):
        d = arr2[j] - start
        if start >= arr2[j] and d < min_d:
            min_d = d
            arr2[j] = end
            count += 1
            break
        elif d < min_d:
            min_d = d

out.write(str(count) + '\n')

inp.close()
out.close()
