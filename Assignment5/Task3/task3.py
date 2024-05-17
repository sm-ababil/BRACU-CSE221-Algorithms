inp = open("input3.txt", "r")
out = open("output3.txt", "w")

n, m = map(int, inp.readline().split())
graph = {}
reverse_graph = {}
for i in range(n + 1):
    graph[i] = []
    reverse_graph[i] = []
for i in range(m):
    v1, v2 = map(int, inp.readline().split())
    graph[v1].append(v2)
    reverse_graph[v2].append(v1)


def scc(n, graph, reverse_graph):
    stack = []
    visited = set()

    def dfs(g, v, topsort=True, sccl=None):
        visited.add(v)
        if not topsort:
            sccl.append(v)

        for r in g[v]:
            if r not in visited:
                dfs(g, r, topsort, sccl)

        if topsort:
            stack.append(v)

    for i in range(1, n+1):
        if i not in visited:
            dfs(graph, i)

    visited.clear()
    scc_list = []
    for i in range(1, n+1):
        list1 = []
        node = stack.pop()
        if node not in visited:
            dfs(reverse_graph, node, False, list1)
        if list1:
            scc_list.append(list1)

    for l in scc_list:
        out.write(str(l).strip("[]").replace(", ", " "))
        out.write("\n")


scc(n, graph, reverse_graph)

inp.close()
out.close()
