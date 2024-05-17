inp = open('input1b.txt', 'r')
out = open('output1b.txt', 'w')

ver, edge = map(int, inp.readline().split())

graph = {}
for i in range(ver+1):
    graph[i] = []
for i in range(edge):
    v1, v2, w = map(int, inp.readline().split())
    graph[v1].append((v2, w))

for v, e in graph.items():
    out.write(f"{v}: {str(e)[1:-1]}\n")

inp.close()
out.close()
