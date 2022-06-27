import os

def evenForest(t_nodes, t_edges, t_from, t_to):
    tree = [[] for _ in range(t_nodes + 1)]
    for f, t in zip(t_from, t_to):
        tree[t].append(f)

    cumulativeSums = [1] * (t_nodes + 1)
    for pa in range(t_nodes, 1, -1):
        if tree[pa] != []:
            for ch in tree[pa]:
                cumulativeSums[pa] += cumulativeSums[ch]

    edges = 0
    for sums in cumulativeSums:
        if sums % 2 == 0:
            edges += 1
    return edges


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
