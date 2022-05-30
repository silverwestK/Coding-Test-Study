#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'printShortestPath' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER i_start
#  3. INTEGER j_start
#  4. INTEGER i_end
#  5. INTEGER j_end
#

# Complete the printShortestPath function below.
def printShortestPath(n, i_start, j_start, i_end, j_end):
    from collections import deque

    moves = {(-2, -1): "UL", (-2, 1): "UR", (0, 2): "R", (2, 1): "LR", (2, -1): "LL", (0, -2): "L"}
    start = (i_start, j_start)
    end = (i_end, j_end)

    visited = [[False for i in range(n)] for i in range(n)]
    q = deque()
    q.append([start, "", 0])
    visited[i_start][j_start] = True

    found = False
    while q:
        curr, m_list, step = q.popleft()
        if curr == end:
            print(step)
            print(m_list)
            found = True
            break
        for key in moves.keys():
            x = curr[0] + key[0]
            y = curr[1] + key[1]
            if check(n, x, y, visited):
                ll = m_list + moves[key] + " "
                q.append([(x, y), ll, step + 1])
                visited[x][y] = True

    if not found:
        print("Impossible")


def check(n, x, y, visited):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if visited[x][y]:
        return False
    return True


if __name__ == '__main__':
    n = int(input().strip())

    first_multiple_input = input().rstrip().split()

    i_start = int(first_multiple_input[0])

    j_start = int(first_multiple_input[1])

    i_end = int(first_multiple_input[2])

    j_end = int(first_multiple_input[3])

    printShortestPath(n, i_start, j_start, i_end, j_end)
