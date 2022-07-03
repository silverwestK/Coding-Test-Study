#!/bin/python3
import os
from collections import defaultdict

def crabGraphs(n, t, graph):
    graph_dic = defaultdict(list)

    for v1, v2 in graph:
        graph_dic[v1].append(v2)
        graph_dic[v2].append(v1)

    nodes = set()

    for v in sorted(graph_dic, key=lambda u: len(graph_dic[u]), reverse=True):
        if v not in nodes and len(graph_dic[v]) >= t:
            nodes.add(v)

    for v in sorted(graph_dic, key=lambda u: len(graph_dic[u]), reverse=True):
        feet = 0
        for u in graph_dic[v]:
            if u not in nodes and feet < t:
                nodes.add(u)
                feet += 1

    return len(nodes)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    c = int(input().strip())

    for c_itr in range(c):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        t = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        graph = []

        for _ in range(m):
            graph.append(list(map(int, input().rstrip().split())))

        result = crabGraphs(n, t, graph)

        fptr.write(str(result) + '\n')

    fptr.close()
