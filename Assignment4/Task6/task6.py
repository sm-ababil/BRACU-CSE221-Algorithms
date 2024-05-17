inp = open("input6.txt", "r")
out = open("output6.txt", "w")
r, c = map(int, inp.readline().split())
graph = [inp.readline().strip() for i in range(r)]


def dfs(graph, visited, r, c):
    if r < 0 or r >= len(graph):
        return 0
    if c < 0 or c >= len(graph[0]):
        return 0
    if graph[r][c] == '#' or visited[r][c]:
        return 0

    visited[r][c] = True
    diamonds = 0
    if graph[r][c] == 'D':
        diamonds += 1

    diamonds += dfs(graph, visited, r + 1, c)
    diamonds += dfs(graph, visited, r - 1, c)
    diamonds += dfs(graph, visited, r, c + 1)
    diamonds += dfs(graph, visited, r, c - 1)

    return diamonds


def max_diamonds(graph):
    row = len(graph)
    col = len(graph[0])
    count = 0
    for r in range(row):
        for c in range(col):
            if graph[r][c] == 'D':
                visited = []
                for i in range(row):
                    visited.append([False] * col)
                count = max(count, dfs(graph, visited, r, c))

    return count


count = max_diamonds(graph)
out.write(str(count))

inp.close()
out.close()

