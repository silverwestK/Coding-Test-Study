from collections import defaultdict
import os
import sys

sys.setrecursionlimit(10 ** 7)

def dfs(graph, f, t):
    global targetCity, tempPosts, totalSum, maxSum, k

    INF = sys.maxsize
    D1, D2 = -INF, -INF

    for i in range(len(graph[t])):
        if graph[t][i][0] != f:
            D1 = max(D1, dfs(graph, t, graph[t][i][0]) + graph[t][i][1])
            if (D1 > D2):
                D1, D2 = D2, D1

            tempPosts[t] += tempPosts[graph[t][i][0]]
            if 0 < tempPosts[graph[t][i][0]] < k:
                totalSum += graph[t][i][1]

    if D1 > 0:
        maxSum = max(maxSum, D1 + D2)

    if D2 > 0 and targetCity[t]:
        maxSum = max(maxSum, D2)

    if targetCity[t]:
        D2 = max(D2, 0)

    return D2


def jeanisRoute(k, city, roads):
    global targetCity, tempPosts, totalSum, maxSum

    for c in city:
        targetCity[c], tempPosts[c] = True, 1

    graph = defaultdict(list)
    for u, v, d in roads:
        graph[u].append([v, d])
        graph[v].append([u, d])

    dfs(graph, 1, 1)

    return totalSum * 2 - maxSum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    city = list(map(int, input().rstrip().split()))

    roads = []

    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))

    targetCity, tempPosts = [False] * (n + 1), [0] * (n + 1)
    totalSum, maxSum = 0, 0

    result = jeanisRoute(k, city, roads)

    fptr.write(str(result) + '\n')

    fptr.close()