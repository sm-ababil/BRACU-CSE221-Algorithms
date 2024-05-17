inp = open('input2.txt', 'r')
out = open('output2.txt', 'w')

n, k = map(int, inp.readline().split())


def find_parent(parents, node):
    par_node = parents[node]
    if par_node == node:
        return node
    else:
        return find_parent(parents, par_node)


def mini_spanning_cost(n, k):
    edges = []
    graph = []
    mini_cost = 0
    parents = [i for i in range(n+1)]

    for i in range(k):
        n1, n2, w = map(int, inp.readline().split())
        edges.append([n1, n2, w])
    sorted_edges = sorted(edges, key=lambda x: x[2])

    for i in range(k):
        node1 = sorted_edges[i][0]
        node2 = sorted_edges[i][1]
        cost = sorted_edges[i][2]

        parent1 = find_parent(parents, node1)
        parent2 = find_parent(parents, node2)

        if parent1 != parent2:
            parents[node2] = parent1
            parents[parent2] = parent1
            graph.append(sorted_edges[i])
            mini_cost += cost

    out.write(str(mini_cost))


mini_spanning_cost(n, k)

inp.close()
out.close()
