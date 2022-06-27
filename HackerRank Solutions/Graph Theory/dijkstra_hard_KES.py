from collections import defaultdict
import os
import heapq

def shortestReach(n, edges, s):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append([v, w])
        graph[v].append([u, w])
    distances = [float('inf')] * (n + 1)
    distances[s] = 0
    queue = [[0, s]]
    heapq.heapify(queue)

    while queue:
        temp_dist, temp_node = heapq.heappop(queue)
        if temp_dist > distances[temp_node]:
            continue
        candidate = graph[temp_node]
        for next_node, next_dist in candidate:
            new_distance = temp_dist + next_dist
            if new_distance < distances[next_node]:
                distances[next_node] = new_distance
                heapq.heappush(queue, [new_distance, next_node])
    distances = distances[1:s] + distances[s + 1:]
    return [d if d != float('inf') else -1 for d in distances]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
