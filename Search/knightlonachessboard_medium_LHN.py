#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'knightlOnAChessboard' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

def knightlOnAChessboard(n):
    from collections import deque

    res = [[0] * (n - 1) for _ in range(n - 1)]
    for i in range(1, n):
        for j in range(1, n):
            if j < i:
                res[i - 1][j - 1] = res[j - 1][i - 1]
                continue
            moves = {(-i, -j), (-i, j), (i, -j), (i, j), (-j, -i), (-j, i), (j, -i), (j, i)}
            visited = [[False] * n for _ in range(n)]
            queue = deque([(0, 0, 0)])
            while queue:
                x, y, step = queue[0]
                queue.popleft()
                if not (0 <= x < n and 0 <= y < n) or visited[x][y]:
                    continue
                visited[x][y] = True
                if x == n - 1 and y == n - 1:
                    res[i - 1][j - 1] = step
                    break
                for dx, dy in moves:
                    queue.append((x + dx, y + dy, step + 1))
            else:
                res[i - 1][j - 1] = -1
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
