#!/bin/python3
import os
from collections import deque


def is_ok(n_i, n_j, n, m, matrix, visited):
    if 0 <= n_i < n and 0 <= n_j < m:
        if (matrix[n_i][n_j] == '*' or matrix[n_i][n_j] == '.') and not visited[n_i][n_j]:
            return True
    else:
        return False


def bfs(mat, k, start, portk):
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # left, right, up, down
    que = deque([[start, 0]])
    visited = [[False] * m for _ in range(n)]
    visited[start[0]][start[1]] = True

    while que:
        stt, c = que.popleft()

        adj = [[stt[0] - 1, stt[1]], [stt[0] + 1, stt[1]],
               [stt[0], stt[1] - 1], [stt[0], stt[1] + 1]]
        cross = [p for p in adj if 0 <= p[0] < n and 0 <= p[1] < m
                 and (mat[p[0]][p[1]] == '.' or mat[p[0]][p[1]] == '*')
                 and not visited[p[0]][p[1]]]
        if len(cross) > 1:
            c += 1
        for m_i, m_j in move:
            n_i = stt[0] + m_i
            n_j = stt[1] + m_j

            if is_ok(n_i, n_j, n, m, mat, visited):
                visited[n_i][n_j] = True
                que.append([[n_i, n_j], c])
                if portk == [n_i, n_j]:
                    if c == k:
                        return 'Impressed'
                    else:
                        return 'Oops!'


def countLuck(matrix, k):
    # Write your code here

    points = [[i, j, matrix[i][j]] for i in range(n) for j in range(m)
              if matrix[i][j] == 'M' or matrix[i][j] == '*']

    for p in points:
        if p[2] == 'M':
            start = p[:2]
        else:
            portk = p[:2]

    result = bfs(matrix, k, start, portk)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input().strip())

        result = countLuck(matrix, k)

        fptr.write(result + '\n')

    fptr.close()
