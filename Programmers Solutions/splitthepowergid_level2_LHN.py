#!/bin/python3

import math
import os
import random
import re
import sys



"""
문제 : n 개의 송전탑이 트리 형태로 연결되어 있을 때, 한개의 선을 끊어서 전력망 네크워크를 2개로 분할하려고 함. 이 때 두 네트워크 안의 송전탑 차이가 가장 적을 경우를
리턴
아이디어 : 송전탑 연결 중에 한개씩 제거하여 bfs 돌고 네트워크 안의 송전탑 개수 차이를 리턴하도록 한다.
"""

def bfs(wire_left,n):
    from collections import deque
    #make_graph
    visited = [0]*n
    graph = [[]for i in range(n)]
    for i,j in wire_left:
        graph[i-1].append(j-1)
        graph[j-1].append(i-1)
    #do bfs
    q = deque()
    q.append(0)
    while q:
        cur = q.popleft()
        visited[cur] = 1
        for i in graph[cur]:
            if visited[i] != 1:
                q.append(i)
    return abs(n - 2*sum(visited))
def solution(n, wires):
    import sys
    answer = sys.maxsize
    for i in range(len(wires)):
        count = bfs(wires[0:i]+wires[i+1:],n)
        if count < answer:
            answer = count
    return answer
