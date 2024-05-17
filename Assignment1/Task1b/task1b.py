inp=open('input1b.txt','r')
out = open('output1b.txt','w')
line = int(inp.readline())

for i in range(0,line):
    a = inp.readline().split()
    b = int(a[1])
    c = int(a[3])

    if a[2] == "+":
        out.write(f'The result of {b} + {c} is {b+c}\n')
    elif a[2] == "-":
        out.write(f'The result of {b} - {c} is {b-c}\n')
    elif a[2] == "*":
        out.write(f'The result of {b} * {c} is {b*c}\n')
    else:
        out.write(f'The result of {b} / {c} is {b/c}\n')


inp.close()
out.close()