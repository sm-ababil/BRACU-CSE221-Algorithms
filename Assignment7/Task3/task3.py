inp = open('input3.txt', 'r')
out = open('output3.txt', 'w')

steps = int(inp.readline())
dict1 = {i: [] for i in range(steps+2)}


def fibonacci(n):
    if dict1[n]:
        return dict1[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        ways = fibonacci(n-1) + fibonacci(n-2)
        dict1[n] = ways
        return ways


out.write(str(fibonacci(steps+1)))

inp.close()
out.close()


'''
To solve this problem, I have used fibonacci function in which recursive
method has been used. Firstly, creating a dictionary in which the fibonacci
values will stored. in fibonacci function it firstly check if the total steps key
has any value, if not it will perform the base cases or it will do the fibonacci
function again recursivley. thus it will count the number of ways by using recurssion.
'''