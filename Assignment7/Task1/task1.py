inp = open('input1.txt', 'r')
out = open('output1.txt', 'w')

n, k = map(int, inp.readline().split())


def find_parent(parents, node):
    par_node = parents[node]
    if par_node == node:
        return par_node
    else:
        return find_parent(parents, par_node)


def friend_circle(n, k):
    parents = [i for i in range(n+1)]
    friends = [1] * (n+1)

    for i in range(k):
        node1, node2 = map(int, inp.readline().split())
        parent1 = find_parent(parents, node1)
        parent2 = find_parent(parents, node2)
        if parent1 != parent2:
            parents[node2] = parent1
            parents[parent2] = parent1
            friends[parent1] += friends[parent2]

        out.write(str(friends[parent1]))
        out.write("\n")


friend_circle(n, k)

inp.close()
out.close()


'''
To solve this problem, I have used two functions. In find parent
function, it identnfy the parent of a node. In friend circle function
it use two arrays, one is for tracking the parents and other is for size
of the friend circle. in a loop, it check every query and find the parents
of the two nodes. if the parents are not same, it joint the friends of the
two node and update the total friend of the parent and give the output. thus,
this problem can be solved.
'''