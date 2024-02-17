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
    for j in range(person):
        if start >= arr2[j]:
            arr2[j] = end
            count += 1
            break

out.write(str(count) + '\n')

inp.close()
out.close()


'''
Firstly, pairs of the times included in 2d array, then using nested loop in
bubble sort function, the pairs of the array has been sorted in ascending 
order by their end time. After that, in another nested for loop the possible pairs
have been counted for each of the person by their start time with other
pairs' end time. The time complexity is O(n^2) because of using nested loops. 
Thus, this solution uses a greedy algorithm to solve the problem.
'''