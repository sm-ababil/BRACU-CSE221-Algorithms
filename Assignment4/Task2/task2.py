inp = open('input2.txt', 'r')
out = open('output2.txt', 'w')

v, e = map(int, inp.readline().split())
visited = [0 for i in range(v+1)]

graph = {}
for i in range(v+1):
    graph[i] = []
for i in range(e):
    v1, v2 = map(int, inp.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


def bfs(g, s):
    queue = [s]
    visited[s] = 1
    while queue:
        temp = queue.pop(0)
        out.write(f"{temp} ")
        for i in g[temp]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)


s = 1
bfs(graph, s)

inp.close()
out.close()
