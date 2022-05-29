import os

def bfs(n, pos, dtn):
    matrix = [[0]*n for _ in range(n)]
    dx = [-2, -2, 0, 2, 2, 0]
    dy = [-1, 1, 2, 1, -1, -2]
    moveName = ['UL', 'UR', 'R', 'LR', 'LL', 'L']
    queue = [(pos[0], pos[1], [])]
    while queue:
        tx, ty, path = queue.pop(0)
        if (tx, ty) == dtn:
            return (matrix[tx][ty], path)
        for i in range(6):
            nx, ny = tx + dx[i], ty + dy[i]
            if 0<=nx<n and 0<=ny<n and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[tx][ty] + 1
                queue.append((nx, ny, path+[moveName[i]]))
    return -1

def printShortestPath(n, i_start, j_start, i_end, j_end):
    result = bfs(n, pos=(i_start, j_start), dtn=(i_end, j_end))
    if result == -1:
        print("Impossible")
    else:
        print(result[0])
        print(*result[1], end=' ')

if __name__ == '__main__':
    n = int(input().strip())

    first_multiple_input = input().rstrip().split()

    i_start = int(first_multiple_input[0])

    j_start = int(first_multiple_input[1])

    i_end = int(first_multiple_input[2])

    j_end = int(first_multiple_input[3])

    printShortestPath(n, i_start, j_start, i_end, j_end)