#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    N = t_nodes
    E = [[] for _ in range(N)]
    for v1, v2 in zip(t_from, t_to):
        E[v1 - 1].append(v2)
        E[v2 - 1].append(v1)

    score = [1] * N
    s_from = set(t_from)
    s_to = set(t_to)
    singles = list(s_from - s_to)
    cuts = 0

    while singles:
        nd = singles.pop()
        nd = nd - 1
        if not E[nd]:
            continue
        neighbour = E[nd][0] - 1

        if score[nd] % 2 == 0:
            cuts += 1
        else:
            score[neighbour] += score[nd]

        E[neighbour].pop(E[neighbour].index(nd + 1))
        if len(E[neighbour]) == 1:
            singles.append(neighbour + 1)

    return cuts


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
