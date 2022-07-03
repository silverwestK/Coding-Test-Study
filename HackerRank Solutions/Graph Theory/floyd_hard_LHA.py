#!/bin/python3
import sys

def floyd_warshall(n, graph):
    INF = sys.maxsize
    dist = [[INF] * n for _ in range(n)]

    for f, t, w in graph:
        dist[f - 1][t - 1] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    dist[i][j] = 0
                    continue
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


if __name__ == '__main__':
    road_nodes, road_edges = map(int, input().rstrip().split())

    road_from = [0] * road_edges
    road_to = [0] * road_edges
    road_weight = [0] * road_edges
    graph = zip(road_from, road_to, road_weight)

    for i in range(road_edges):
        road_from[i], road_to[i], road_weight[i] = map(int, input().rstrip().split())
    graph = zip(road_from, road_to, road_weight)

    distance = floyd_warshall(road_nodes, graph)

    q = int(input().strip())
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        x = int(first_multiple_input[0])

        y = int(first_multiple_input[1])

        print(distance[x - 1][y - 1] if distance[x - 1][y - 1] != sys.maxsize else -1)






