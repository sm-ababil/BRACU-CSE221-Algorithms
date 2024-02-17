inp = open('input1a.txt', 'r')
out = open('output1a.txt', 'w')
line = int(inp.readline())

for i in range(line):
    a = int(inp.readline())
    if a%2 == 0:
        out.write(f'{a} is an Even number\n')
    else:
        out.write(f'{a} is an Odd number\n')