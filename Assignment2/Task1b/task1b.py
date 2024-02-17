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


'''
Here two pointers have been used. In a for loop two element of the array is accessed 
by using the pointers. Then the sum of the two elements is compared to the given sum.
If the sum is equal to the given then it will write the index otherwise it will make
the flag true which will write impossible. In this solution only one loop has been used
that's why it's time complexity is O(n)
'''