import numpy as np

inp = open('input3.txt', 'r')
out = open('output3.txt', 'w')

line = int(inp.readline())
ids = np.array(inp.readline().split())
marks = np.array(inp.readline().split())
std_data = np.zeros((line, 2), dtype=int)

for i in range(line):
    std_data[i][0], std_data[i][1] = int(ids[i]), int(marks[i])


def selection_sort(line, std_data):
    for i in range(line):
        max_idx = i
        for j in range(i+1, line):
            if std_data[j][1] > std_data[max_idx][1]:
                max_idx = j
            elif std_data[j][1] == std_data[max_idx][1] and std_data[j][0] < std_data[max_idx][0]:
                max_idx = j

        if max_idx != i:
            std_data[i], std_data[max_idx] = std_data[max_idx].copy(), std_data[i].copy()


selection_sort(line, std_data)

for i in range(line):
    out.write(f"ID: {std_data[i][0]} Mark: {std_data[i][1]}\n")
