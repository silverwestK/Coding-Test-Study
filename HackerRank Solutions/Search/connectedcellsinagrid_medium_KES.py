import os

def dfs(matrix, tempCnt, matsize, pos):
    matrix[pos[0]][pos[1]] = 0
    dx = [0, 0, 1, 1, 1, -1, -1, -1]
    dy = [1, -1, 0, 1, -1, 0, 1, -1]
    for i in range(8):
        ni, nj = pos[0] + dx[i], pos[1] + dy[i]
        if 0 <= ni < matsize[0] and 0 <= nj < matsize[1] and matrix[ni][nj] == 1:
            matrix[ni][nj] = 0
            tempCnt = dfs(matrix, tempCnt + 1, matsize=matsize, pos=(ni, nj))
    return tempCnt

def connectedCell(n, m, matrix):
    maxCnt = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                tempCnt = dfs(matrix, 1, matsize=(n, m), pos=(i, j))
                maxCnt = max(tempCnt, maxCnt)
    return maxCnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(n, m, matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
