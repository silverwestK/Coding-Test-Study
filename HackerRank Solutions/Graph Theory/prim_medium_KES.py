from collections import defaultdict
import heapq
import os

def prims(n, edges, start):
    visited = [0] * (n + 1)
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append([w, u, v])
        graph[v].append([w, v, u])

    heapq.heapify(graph[start])
    visited[start] = 1
    total_weight = 0

    while graph[start]:
        w, u, v = heapq.heappop(graph[start])
        if visited[v] == 0:
            visited[v] = 1
            total_weight += w
            for edge in graph[v]:
                if visited[edge[2]] == 0:
                    heapq.heappush(graph[start], edge)

    return total_weight

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
