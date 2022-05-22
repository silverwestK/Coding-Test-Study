#!/bin/python3
import os
from collections import deque

def bfs(a, b, n):
    move = [[a, b], [a, -b], [-a, b], [-a, -b],
            [b, a], [b, -a], [-b, a], [-b, -a]]
    que = deque([(0, 0, 0)])
    visited = [[False] * n for _ in range(n)]

    visited[0][0] = True

    while que:
        x, y, cnt = que.popleft()
        cnt += 1
        for x_m, y_m in move:
            x_dst = x + x_m
            y_dst = y + y_m
            if 0 <= x_dst < n and 0 <= y_dst < n and not visited[x_dst][y_dst]:
                if x_dst == n - 1 and y_dst == n - 1:
                    return cnt
                visited[x_dst][y_dst] = True
                que.append((x_dst, y_dst, cnt))

    return -1


def knightlOnAChessboard(n):
    # Write your code here

    result = [[0 for _ in range(n - 1)] for _ in range(n - 1)]

    for i in range(1, n):
        for j in range(1, n):
            result[i - 1][j - 1] = bfs(i, j, n)
            result[j - 1][i - 1] = result[i - 1][j - 1]

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
