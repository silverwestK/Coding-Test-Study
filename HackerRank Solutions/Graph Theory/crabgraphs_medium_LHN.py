#!/bin/python3

import math
import os
import random
import re
import sys
"""
문제 :
무방향 그래프가 주어졌을 때 노드 1개를 head 로 가지고 그와 연결된 노드들을 잇는 엣지를 feet으로 하는 구조를 crab 이라고 할 때 
인풋으로 노드 수, crab 이 가질 수 있는 최대 feet 수, 엣지 수가 주어지고 만들어질 수 있는 crab 에 포함되어 있는 노드들의 최대값을
구하는 문제이다
조건 :
각 crab은 서로 연결 될 수 없고 떨어져 있어야 한다(두개의 crab은 중복된 노드를 가질 수 없음)
아이디어 : head가 될 수 있는 노드들을 먼저 골라서 crab에 포함 처리를 한다 -> 어차피 head 노드를 모두 살리는 것이 더 많은 노드를 포함하기 때문
동작 과정 :
그래프 만들기 -> 헤드 노드 찾기 -> 노드들 돌면서 crab 에 포함될 노드 추가

"""

#
# Complete the 'crabGraphs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER t
#  3. 2D_INTEGER_ARRAY graph
#

def crabGraphs(n, t, graph):
    crab_graph={x:[] for x in range(1,n+1)}
    for u,v in graph:
        crab_graph[u].append(v)
        crab_graph[v].append(u)
    print(crab_graph)
    nodes=set()
    #헤드 가 될 수 있는 노드들을 찾아서 넣어주는 과정
    for u in sorted(crab_graph, key=lambda s:len(crab_graph[s]),reverse=True):
        if u not in nodes and len(crab_graph[u])>=t:
            nodes.add(u)
        else:
            break
    print(nodes)
    for u in sorted(crab_graph, key=lambda s:len(crab_graph[s]),reverse=True):
        #발의 개수가 최대 개수를 넘는지 확인하기 위한 변수
        feetofu=0
        for v in crab_graph[u]:
            if v not in nodes and feetofu<t:
                nodes.add(v)
                feetofu+=1
    return len(nodes)

if __name__ == '__main__':

    c = int(input().strip())

    for c_itr in range(c):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        t = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        graph = []

        for _ in range(m):
            graph.append(list(map(int, input().rstrip().split())))

        result = crabGraphs(n, t, graph)
        print(result)