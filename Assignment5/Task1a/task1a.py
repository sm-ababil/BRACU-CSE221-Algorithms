inp = open("input1a.txt", "r")
out = open("output1a.txt", "w")

n, m = map(int, inp.readline().split())
graph = {}
prereq_count = [0]*(n+1)
for i in range(n+1):
    graph[i] = []
for i in range(m):
    v1, v2 = map(int, inp.readline().split())
    graph[v1].append(v2)
    prereq_count[v2] += 1


def course_sequence(graph, n, prereq):
    sequence = []
    
    def dfs(g, v, prereq):
        sequence.append(v)
        for courses in g[v]:
            prereq[courses] -= 1
            if prereq[courses] == 0 and courses not in sequence:
                dfs(g, courses, prereq)

    for v in range(1, n+1):
        if prereq[v] == 0 and v not in sequence:
            dfs(graph, v, prereq)

    if len(sequence) < n:
        out.write("IMPOSSIBLE")
    else:
        out.write(str(sequence).strip("[]").replace(", ", " "))


course_sequence(graph, n, prereq_count)

inp.close()
out.close()


'''
firstly, using a dictionary the graph is created and
in a array, total prerequisite of each course has been
counted. then in the main course sequence funtion a nested
dfs function has been implemented whhere it update the
prereq count and traverse the courses using recursion method and 
append the valid course sequence. if the sequence list length 
is less than the total courses then it is impossible, otherwise 
it prints the course sequence.
'''