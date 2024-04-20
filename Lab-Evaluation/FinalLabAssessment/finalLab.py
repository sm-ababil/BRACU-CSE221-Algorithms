import math
inp = open("input.txt", "r")
out = open("output.txt", "w")

n, e = map(int, inp.readline().split())
graph = {}
for i in range(n):
    graph[i] = []
for j in range(n):
    v1, v2, w = map(float, inp.readline().split())
    graph[v1].append((v2, w))
    graph[v2].append((v1, w))


def find_paths(graph, source, destination, weight=0.0, path=[]):
    all_paths = []
    path = path + [(source, weight)]
    if source == destination:
        return [path]
    for node in graph[source]:
        if node not in path:
            paths = find_paths(graph, node[0], destination, node[1], path)
            for i in paths:
                all_paths.append(i)
    return all_paths


source, destination = map(float, inp.readline().split())
all_paths = find_paths(graph, source, destination)

if not all_paths:
    out.write(str(0.0))
else:
    max_prob = None
    for path in all_paths:
        prob = 1.0
        for node in range(1, len(path)):
            prob *= path[node][1]
        if not max_prob or prob > max_prob:
            max_prob = prob
    out.write(str(max_prob))

inp.close()
out.close()
