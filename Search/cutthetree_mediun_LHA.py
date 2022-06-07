#!/bin/python3
import os
import copy
import sys
sys.setrecursionlimit(10**6) 

def dfs(data, graph, v, tree1, visited):
    visited[v] = True
    tree1 += data[v - 1]

    for i in graph[v]:
        if not visited[i]:
            visited, tree1 = dfs(data, graph, i, tree1, visited)

    return visited, tree1


def cutTheTree(data, edges):
    graph = [[]] + [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    diff = []
    for i in range(len(edges)):
        visited = [False] * (n + 1)
        cutted_graph = copy.deepcopy(graph)
        cutted_graph[edges[i][0]].remove(edges[i][1])
        cutted_graph[edges[i][1]].remove(edges[i][0])

        tree1, tree2 = 0, 0
        visited, tree1 = dfs(data, cutted_graph, 1, tree1, visited)
        not_vis = list(filter(lambda x: visited[x] == False, range(len(visited))))
        not_vis.remove(0)
        tree2 = sum(list(map(lambda x: data[x - 1], not_vis)))

        diff.append(abs(tree1 - tree2))

    return min(diff)


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
