# Problem: Breadth First Search: Shortest Reach
from collections import deque
import os

def bfs(n, m, edges, s):
    graph = [set() for _ in range(n)]
    for u, v in edges:
        graph[u - 1].add(v - 1)
        graph[v - 1].add(u - 1)

    end_nodes = [i for i in range(n)]
    end_nodes.remove(s - 1)
    queue, result = deque([(s - 1, 0)]), [-1] * n
    while queue:
        temp, depth = queue.popleft()
        if temp in end_nodes:
            result[temp] = depth * 6
            end_nodes.remove(temp)
        for n in list(graph[temp]):
            queue.append((n, depth + 1))
            graph[temp].remove(n)
            graph[n].remove(temp)
    result.pop(s - 1)
    return result


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
