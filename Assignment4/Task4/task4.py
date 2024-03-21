inp = open('input4.txt', 'r')
out = open('output4.txt', 'w')

v, e = map(int, inp.readline().split())
visited = [0 for i in range(v+1)]

graph = {}
for i in range(v+1):
    graph[i] = []
for i in range(e):
    v1, v2 = map(int, inp.readline().split())
    graph[v1].append(v2)


def cycle(graph, s):
    visited[s] = 1
    for i in graph[s]:
        if visited[i] == 0:
            cyclic = cycle(graph, i)
            if cyclic:
                return True
        elif visited[i] == 1:
            return True
    visited[s] = 2
    return False


def iscyclic(graph):
    for i in range(1, v+1):
        if visited[i] == 0:
            if cycle(graph, i):
                return "YES"
    return "NO"


out.write(iscyclic(graph))

inp.close()
out.close()

'''
in cycle function it using dfs traverse it traverse through
the veretices using recursive method. if it finds any visited
vertices which is marked by 1 it make the graph cyclic. thus it make 
all the vertices as source and check the cyclic or not for each vertices as source.
thus it identify cyclic graph or not.
'''