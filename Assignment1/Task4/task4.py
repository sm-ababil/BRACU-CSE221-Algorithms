import numpy as np

inp = open('input4.txt','r')
out = open('output4.txt','w')

line = int(inp.readline())
data = []
for i in range(line):
    data.append(inp.readline().split())
train_data = np.array(data)


def selection_sort(line, train_data):
    for i in range(line):
        min_idx = i
        for j in range(i+1, line):
            if train_data[j][0].lower() < train_data[min_idx][0].lower():
                min_idx = j
            elif train_data[j][0].lower() == train_data[min_idx][0].lower():
                a = int(train_data[j][-1][:2])
                b = int(train_data[min_idx][-1][:2])
                c = int(train_data[j][-1][3:])
                d = int(train_data[min_idx][-1][3:])
                if a > b:
                    min_idx = j
                elif a == b and c > d:
                    min_idx = j
        if min_idx != i:
            train_data[i], train_data[min_idx] = train_data[min_idx].copy(), train_data[i].copy()


selection_sort(line, train_data)

for i in range(line):
    out.write(" ".join(train_data[i]))
    out.write("\n")

inp.close()
out.close()