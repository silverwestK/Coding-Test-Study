#!/bin/python3
import os
import sys
from heapq import *


def shortestReach(n, edges, s):
    INF = int(1e9)
    que = []
    distance = [INF] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for x, y, w in edges:
        graph[x].append((y, w))
        graph[y].append((x, w))

    heappush(que, (0, s))
    distance[s] = 0

    while que:
        dis, node = heappop(que)

        if distance[node] < dis:
            continue
        for next in graph[node]:

            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heappush(que, (cost, next[0]))

    result = [d if d != INF else -1 for d in distance]
    result.pop(s)

    return result[1:]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):

        nm = input().split()

        n = int(nm[0])
        m = int(nm[1])

        edges = set()
        for _ in range(m):
            edges.add(tuple(map(int, sys.stdin.readline().rstrip().split())))

        s = int(input())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')
    fptr.close()
