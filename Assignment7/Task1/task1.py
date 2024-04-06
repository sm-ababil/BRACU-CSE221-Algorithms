inp = open("input1.txt", "r")
out = open("output1.txt", "w")

n, q = map(int, inp.readline().split())


def find_friend_circle_size(N, friendships):
    # Initialize a dictionary to store friend circles
    friend_circles = {i: i for i in range(1, N + 1)}
    sizes = []

    def find_root(person):
        # Find the root of the friend circle
        if friend_circles[person] != person:
            friend_circles[person] = find_root(friend_circles[person])
        return friend_circles[person]

    def union(person1, person2):
        # Union two friend circles
        root1, root2 = find_root(person1), find_root(person2)
        if root1 != root2:
            friend_circles[root2] = root1
        # sizes.append(len(friend_circles[root1]))

    # Process each friendship
    for person1, person2 in friendships:
        union(person1, person2)

    # Count the size of each friend circle
    circle_sizes = {}
    for person in range(1, N + 1):
        root = find_root(person)
        circle_sizes[root] = circle_sizes.get(root, 0) + 1
    # print(circle_sizes)
    # Return the maximum friend circle size
    print(friend_circles)
    return circle_sizes

# Example usage

friendships = [(2,4), (4,5), (3,6), (4,7), (3,1), (2,7), (6,2)]  # Given friendships
largest_circle_size = find_friend_circle_size(n, friendships)
print(largest_circle_size)
print(f"Largest friend circle size: {largest_circle_size}")
