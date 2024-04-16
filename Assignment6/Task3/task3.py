import math
inp = open('input3.txt', 'r')
out = open('output3.txt', 'w')

n, m = map(int, inp.readline().split())

graph = {}
for i in range(n+1):
    graph[i] = []
for j in range(m):
    v1, v2, w = map(int, inp.readline().split())
    graph[v1].append((v2, w))


def find_paths(graph, source, destination, weight=0, path=[]):
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


all_paths = find_paths(graph, 1, n)

if not all_paths:
    out.write("IMPOSSIBLE")
else:
    mini_danger = None
    for path in all_paths:
        path_danger = None
        for i in range(1, len(path)):
            path_danger = max(path[i-1][1], path[i][1])
        if not mini_danger or path_danger < mini_danger:
            mini_danger = path_danger
    out.write(str(mini_danger))

inp.close()
out.close()


'''
to find the solution it use dfs traverse in find path function
by using recurssion. in this function it update all the possible paths
from source to destination with their edge weight which is danger
level. then after finding the paths in a nested for loop it compare the
danger levels in each path and finds the maximum for that path, then it compare
the minimum danger level among all the paths that is the safest path possible which
will be printed. if there is no path between source and destination it prints IMPOSSIBLE.
'''