inp = open('input3.txt', 'r')
out = open('output3.txt', 'w')

v, e = map(int, inp.readline().split())
visited = [0 for i in range(v+1)]

graph = {}
for i in range(v+1):
    graph[i] = []
for i in range(e):
    v1, v2 = map(int, inp.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


def dfs(graph, s):
    visited[s] = 1
    out.write(f"{s} ")
    for node in graph[s]:
        if visited[node] == 0:
            dfs(graph, node)


s = 1
dfs(graph, s)

inp.close()
out.close()
