#!/bin/python3

import math
import os
import random
import re
import sys


def make_graph(node, road_from, road_to, road_weight, ms):
    graph_in = [ms for i in range(node)]
    graph = [graph_in[:] for i in range(node)]

    for i in range(node):
        graph[i][i] = 0

    for f, t, w in zip(road_from, road_to, road_weight):
        graph[f - 1][t - 1] = w
    return graph


def floyd(node, road_from, road_to, road_weight, ms):
    graph = make_graph(node, road_from, road_to, road_weight, ms)
    # through node
    for i in range(node):
        t = graph[i]
        # start node
        for s in range(node):
            if graph[s][i] == ms:
                continue
            s = graph[s]
            # finish node
            for f in range(node):
                if t[f] == ms:
                    continue
                if s[f] > s[i] + t[f]:
                    s[f] = s[i] + t[f]

    return graph


if __name__ == '__main__':
    road_nodes, road_edges = map(int, input().rstrip().split())

    road_from = [0] * road_edges
    road_to = [0] * road_edges
    road_weight = [0] * road_edges

    for i in range(road_edges):
        road_from[i], road_to[i], road_weight[i] = map(int, input().rstrip().split())

    ms = sys.maxsize

    graph = floyd(road_nodes, road_from, road_to, road_weight, ms)

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        x = int(first_multiple_input[0])

        y = int(first_multiple_input[1])

        result = graph[x - 1][y - 1]
        if result == ms:
            print(-1)
        else:
            print(result)

