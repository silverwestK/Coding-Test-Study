#!/bin/python3
import os

def dfs(matrix, i, j, area):
    matrix[i][j] = 0
    moving = [[0, 1], [0, -1], [1, 0], [-1, 0],
              [1, 1], [1, -1], [-1, 1], [-1, -1]]

    for i_m, j_m in moving:
        n_i = i + i_m
        n_j = j + j_m
        if 0 <= n_i < n and 0 <= n_j < m and matrix[n_i][n_j] == 1:
            area = dfs(matrix, n_i, n_j, area + 1)

    return area


def connectedCell(matrix):
    answer = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                area = dfs(matrix, i, j, 1)
                answer = max(area, answer)

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
