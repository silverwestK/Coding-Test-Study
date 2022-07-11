#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickestWayUp' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY ladders
#  2. 2D_INTEGER_ARRAY snakes
#

def quickestWayUp(ladders, snakes):
    # Write your code here
    from collections import deque
    board = [i for i in range(1,101)]
    for i in ladders + snakes:
        board[i[0]-1] = i[1]
    q = deque()
    q.append([0,0])
    visited = [False]*106
    while q:
        cur, roll = q.popleft()
        visited[cur] = True
        if board[cur] >= 100:
            return roll
        for i in range(0,6):
            nexts = board[cur]+i
            if visited[nexts] == False:
                q.append([nexts, roll + 1])
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input().strip())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()
