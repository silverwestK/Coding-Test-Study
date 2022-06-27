#!/bin/python3
import os
from collections import defaultdict

child_num = defaultdict(int)

def dfs(graph, start):
    global child_num

    if start not in graph.keys():
        return 1
    else:
        cnt = 1
        for node in graph[start]:
            child_num[node] = dfs(graph, node)
            cnt += child_num[node]
        return cnt

def evenForest(t_nodes, t_edges, t_from, t_to):
    global child_num
    graph = defaultdict(list)
    for f, t in zip(t_from, t_to):
        graph[t].append(f)
    child_num[1] = dfs(graph, 1)

    answer = 0
    for k, v in child_num.items():
        if k != 1 and v % 2 == 0:
            answer += 1
    return answer


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
