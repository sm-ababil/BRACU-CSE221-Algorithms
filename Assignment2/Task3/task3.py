import numpy as np

inp = open('input3.txt', 'r')
out = open('output3.txt', 'w')

line = int(inp.readline())
arr = np.zeros((line, 2), dtype=int)
arr2 = np.zeros((line, 2), dtype=int)
temp = 0
count = 0

for i in range(line):
    sch = inp.readline().split()
    arr[i][0], arr[i][1] = int(sch[0]), int(sch[1])


def bubble_sort(line, arr):
    for i in range(line):
        for j in range(line - i - 1):
            if arr[j][1] > arr[j+1][1]:
                arr[j], arr[j+1] = arr[j+1].copy(), arr[j].copy()


bubble_sort(line, arr)

for i in range(line):
    start = arr[i][0]
    end = arr[i][1]
    if start >= temp:
        arr2[i][0], arr2[i][1] = start, end
        temp = end
        count += 1

out.write(str(count) + '\n')
for i in range(line):
    if arr2[i][0] == 0 and arr2[i][0] == 0:
        continue
    out.write(f"{arr2[i][0]} {arr2[i][1]}\n")

inp.close()
out.close()


'''
To solve this, I make the pairs of the times in a 2d array.
Then, using nested loop in bubble sort function, the pairs of the array
has been sorted in ascending order by their end time. And then in another
for loop the possible pairs have been found by their start time with other
pairs' end time. Here, the time complexity is O(n^2) because of using bubble
sort which use nested loop.
'''
