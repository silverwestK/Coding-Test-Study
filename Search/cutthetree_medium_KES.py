import os

def bfs(tree):
    parent_nodes, visited_nodes = {1}, []
    while parent_nodes:
        pn = parent_nodes.pop()
        # Save visited nodes in descending order along depth level
        visited_nodes.insert(0, pn)
        parent_nodes.update(set(tree[pn]))
        # Prevent node revisiting
        for cn in tree[pn]:
            tree[cn].remove(pn)
    return visited_nodes


def cutTheTree(data, edges):
    tree = {}
    for n1, n2 in edges:
        tree[n1] = tree.get(n1, []) + [n2]
        tree[n2] = tree.get(n2, []) + [n1]
    # bfs for calculating tree's depth
    visited_nodes = bfs(tree)
    for node in visited_nodes:
        data[node - 1] += sum(data[cn - 1] for cn in tree[node])
    return min(abs(data[0] - 2 * data[n]) for n in range(1, len(data)))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, edges)

    fptr.write(str(result) + '\n')

    fptr.close()