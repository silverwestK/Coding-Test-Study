#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#


def kruskals(g_nodes, g_from, g_to, g_weight):
    # Write your code here
    # make graph
    n_e = len(g_from)
    check_cycle_s = ''
    for i in range(g_nodes):
        check_cycle_s = check_cycle_s + '"'+str(i+1)+'",'
    check_cycle = check_cycle_s.split(',')
    graph = []
    mst = 0
    for i in range(n_e):
        graph.append([g_from[i],g_to[i],g_weight[i]])
    #sort graph with weight
    graph.sort(key=lambda x : x[2])
    #calculate MST
    count = 0
    for i in graph:
        if count < g_nodes:
            if check_cycle[i[0]-1] != check_cycle[i[1]-1]:
                mst = mst + i[2]
                if check_cycle[i[0]-1] <= check_cycle[i[1]-1]:
                    have_to_change = str(check_cycle[i[1]-1])
                    value = str(check_cycle[i[0]-1])
                else:
                    have_to_change = str(check_cycle[i[0]-1])
                    value = str(check_cycle[i[1]-1])
                check_cycle_s = check_cycle_s.replace(have_to_change,value)
                check_cycle = check_cycle_s.split(',')
                count = count + 1
        else:
            break
    return mst





if __name__ == '__main__':

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    print(res)
