import math
import os
import random
import re
import sys

mins = sys.maxsize

sys.setrecursionlimit(int(1e6)+1)

def cutTheTree(data, edges):
    global mins

    node_connected = [set() for i in range(n)]
    visited = [False] * n

    for n1, n2 in edges:
        node_connected[n1-1].add(n2-1)
        node_connected[n2-1].add(n1-1)

    sum_value = sum(data)

    dfs(0,sum_value,node_connected,data,visited)

    return mins

def dfs(current_idx, sum_value, node_connected, data, visited):
    global mins
    if visited[current_idx]:
        return 0
    visited[current_idx] = True

    lower_end = data[current_idx]
    for idx in node_connected[current_idx]:
        lower_end += dfs(idx, sum_value, node_connected, data, visited)
    diff = abs(sum_value - 2*lower_end)

    if diff < mins:
        mins = diff
    return lower_end


if __name__ == '__main__':
    global d_list

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, edges)

    print(result)