# 문제: 섬 연결하기

from collections import defaultdict
from heapq import heapify, heappop, heappush

def solution(n, costs):
    visited = [0] * n
    graph = defaultdict(list)
    for v1, v2, cost in costs:
        graph[v1].append((cost, v2))
        graph[v2].append((cost, v1))

    heapify(graph[0])
    visited[0] = 1
    answer = 0

    while graph[0]:
        cost, v = heappop(graph[0])
        if visited[v] == 0:
            visited[v] = 1
            answer += cost
            for edge in graph[v]:
                if visited[edge[1]] == 0:
                    heappush(graph[0], edge)

    return answer