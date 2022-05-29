#!/bin/python3
from collections import deque

def bfs(n, i_start, j_start, i_end, j_end):
    move = {'UL': (-2, -1), 'UR': (-2, 1), 'R': (0, 2),
            'LR': (2, 1), 'LL': (2, -1), 'L': (0, -2)}
    visited = [[False] * n for _ in range(n)]
    que = deque()
    que.append([i_start, j_start, []])
    visited[i_start][j_start] = True

    while que:
        s_i, s_j, path = que.popleft()
        if s_i == i_end and s_j == j_end:
            return path
        for m in move:
            n_i = s_i + move[m][0]
            n_j = s_j + move[m][1]
            if 0 <= n_i < n and 0 <= n_j < n and not visited[n_i][n_j]:
                m_l = path + [m]
                que.append([n_i, n_j, m_l])
                visited[n_i][n_j] = True

    return -1


def printShortestPath(n, i_start, j_start, i_end, j_end):
    # Print the distance along with the sequence of moves.
    ans = bfs(n, i_start, j_start, i_end, j_end)

    if ans == -1:
        print('Impossible')
    else:
        print(len(ans))
        print(*ans)


if __name__ == '__main__':
    n = int(input().strip())

    first_multiple_input = input().rstrip().split()

    i_start = int(first_multiple_input[0])

    j_start = int(first_multiple_input[1])

    i_end = int(first_multiple_input[2])

    j_end = int(first_multiple_input[3])

    printShortestPath(n, i_start, j_start, i_end, j_end)
