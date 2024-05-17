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
