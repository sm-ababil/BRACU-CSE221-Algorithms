inp = open('input5.txt', 'r')
out = open('output5.txt', 'w')

v, e, d = map(int, inp.readline().split())
visited = [0 for i in range(v+1)]
level = [0 for i in range(v+1)]
parent = [0 for i in range(v+1)]

graph = {}
for i in range(v+1):
    graph[i] = []
for i in range(e):
    v1, v2 = map(int, inp.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


def bfs(graph, s):
    queue = [s]
    visited[s] = 1
    level[s] = 0
    parent[s] = s

    while queue:
        temp = queue.pop(0)
        for x in graph[temp]:
            if visited[x] == 0:
                visited[x] = 1
                level[x] = level[temp] + 1
                parent[x] = temp
                queue.append(x)
            if x == d:
                break


s = 1
bfs(graph, s)
out.write(f"Time: {level[d]}\n")
shortest = []
while True:
    shortest.append(d)
    if d == s:
        break
    d = parent[d]
shortest.reverse()
out.write(f"Shortest Path: {' '.join(map(str, shortest))}")

inp.close()
out.close()
