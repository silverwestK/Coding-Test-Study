#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    from collections import deque
    # Write your code here
    # make graph
    graph = [set() for i in range(n)]
    for n1, n2 in edges:
        graph[n1 - 1].add(n2)
        graph[n2 - 1].add(n1)
    # result list
    result = [-1] * n

    q = deque()
    q.append([s, 0])
    visited = [False] * n
    while q:
        cur, depth = q.popleft()
        if visited[cur - 1] == False:
            result[cur - 1] = 6 * depth
            visited[cur - 1] = True
            if len(graph[cur - 1]) != 0:
                for i in graph[cur - 1]:
                    if visited[i - 1] != True:
                        q.append([i, depth + 1])
    result.pop(s - 1)
    return result


if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        print(result)
        print('--------------------------------------------')
