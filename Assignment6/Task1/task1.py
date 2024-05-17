import math
inp = open('input1.txt', 'r')
out = open('output1.txt', 'w')

n, m = map(int, inp.readline().split())

graph = {}
for i in range(n+1):
    graph[i] = []
for j in range(m):
    v1, v2, w = map(int, inp.readline().split())
    graph[v1].append((v2, w))


def djikstra(source):
    visited = set()
    distance = [math.inf for i in range(n+1)]
    distance[source] = 0

    for i in range(1, n+1):
        selected = None
        for j in range(1, n+1):
            if j not in visited:
                if not selected or distance[j] < distance[selected]:
                    selected = j
        visited.add(selected)
        for pair in graph[selected]:
            if distance[pair[0]] > distance[selected] + pair[1]:
                distance[pair[0]] = distance[selected] + pair[1]

    return distance


source = int(inp.readline())
distance = djikstra(source)
for k in range(1, n + 1):
    if distance[k] == math.inf:
        out.write("-1 ")
    else:
        out.write(f"{distance[k]} ")

inp.close()
out.close()
