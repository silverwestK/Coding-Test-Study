#!/bin/python3
import os
from collections import defaultdict
from heapq import *


def prims(n, edges, start):
    total_w = 0
    keys = []
    graph = defaultdict(dict)

    for n1, n2, w in edges:
        graph[n1][n2] = w
        graph[n2][n1] = w

    mst = [False] * n
    heappush(keys, (0, start))
    heapify(keys)

    while keys:
        current_key, current_node = heappop(keys)
        if mst[current_node - 1] == False:
            mst[current_node - 1] = True
            total_w += current_key
            for adjacent, w in graph[current_node].items():
                heappush(keys, (w, adjacent))
    return total_w


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input().strip())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()
