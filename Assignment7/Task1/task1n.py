def find_root(person, friend_circles):
    # Find the root of the friend circle
    if friend_circles[person] != person:
        friend_circles[person] = find_root(friend_circles[person], friend_circles)
    return friend_circles[person]


def union(person1, person2, friend_circles, circle_sizes):
    # Union two friend circles
    root1, root2 = find_root(person1, friend_circles), find_root(person2, friend_circles)
    if root1 != root2:
        friend_circles[root1] = root2
        circle_sizes[root2] += circle_sizes[root1]


inp = open("input1.txt", "r")
# out = open("output1.txt", "w")

N, K = map(int, inp.readline().split())
friend_circles = {i: i for i in range(1, N + 1)}
circle_sizes = {i: 1 for i in range(1, N + 1)}

for _ in range(K):
    person1, person2 = map(int, inp.readline().split())
    union(person1, person2, friend_circles, circle_sizes)
    print(max(circle_sizes.values()))

