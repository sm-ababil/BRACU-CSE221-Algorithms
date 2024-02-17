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


'''
The best-case scenario for bubble sort is when the inputted array has already been sorted.
I have used a flag (line11) and a 'for loop'(line12) to check whether the array is sorted or not. 
If the array has already been sorted (best-case scenario) the flag will remain False and the code will 
end at that for loop and the time complexity will be O(n) for using only one for loop. 
That's how I have achieved O(n) for best case scenario.
'''