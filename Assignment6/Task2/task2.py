import math

inp = open('input2.txt', 'r')
out = open('output2.txt', 'w')

n, m = map(int, inp.readline().split())

graph = {}
for i in range(n + 1):
    graph[i] = []
for j in range(m):
    v1, v2, w = map(int, inp.readline().split())
    graph[v1].append((v2, w))


def djikstra(source):
    visited = set()
    distance = [math.inf for i in range(n + 1)]
    distance[source] = 0

    for i in range(1, n + 1):
        selected = None
        for j in range(1, n + 1):
            if j not in visited:
                if not selected or distance[j] < distance[selected]:
                    selected = j
        visited.add(selected)
        for pair in graph[selected]:
            if distance[pair[0]] > distance[selected] + pair[1]:
                distance[pair[0]] = distance[selected] + pair[1]

    return distance


source1, source2 = map(int, inp.readline().split())
distance1 = djikstra(source1)
distance2 = djikstra(source2)

minimum = None
node = None
time = None
for k in range(1, n + 1):
    if distance1[k] != math.inf and distance2[k] != math.inf:
        if not minimum or abs(distance1[k] - distance2[k]) < minimum:
            minimum = abs(distance1[k] - distance2[k])
            node = k
            time = max(distance1[k], distance2[k])

if not node:
    out.write("IMPOSSIBLE")
else:
    out.write(f"Time {time}\nNode {node}")

inp.close()
out.close()
