#!/bin/python3
import os
from collections import deque

def search(graph, n, s):
    que = deque([(s, 0)])
    visited = [False] * n
    visited[s - 1] = True
    dep_list = [0 for _ in range(n)]

    while que:
        start, depth = que.popleft()
        dep_list[start - 1] = depth

        for node in graph[start - 1]:
            if not visited[node - 1]:
                que.append([node, depth + 1])
                visited[node - 1] = True

    return dep_list


def bfs(n, m, edges, s):
    graph = [[] for _ in range(n)]
    for e in edges:
        graph[e[0] - 1].append(e[1])
        graph[e[1] - 1].append(e[0])

    answer = search(graph, n, s)
    answer.pop(s - 1)
    answer = [-1 if i == 0 else i * 6 for i in answer]

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

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

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
