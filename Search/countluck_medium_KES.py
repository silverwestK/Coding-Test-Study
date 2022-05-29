import os

def findMPosition(matrix):
    posDic = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'M':
                return [i, j]

def checkIntersection(pos):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    res = []

    for i in range(4):
        nx, ny = pos[0] + dx[i], pos[1] + dy[i]
        if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] != 'X':
            res.append([nx, ny])
    return res

def dfs(matrix, wave_cnt, pos):
    if matrix[pos[0]][pos[1]] == '*':
        return wave_cnt

    matrix[pos[0]][pos[1]] = 'X'
    moves = checkIntersection(pos)
    if len(moves) > 1:
        wave_cnt += 1
    for nx, ny in moves:
        result = dfs(matrix, wave_cnt, pos=[nx, ny])
        if result != -1:
            return result
    return -1

def countLuck(matrix, k):
    temp_pos = findMPosition(matrix)
    wave_cnt = dfs(matrix, 0, pos=temp_pos)
    return 'Oops!' if wave_cnt != k else 'Impressed'


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
            matrix.append(list(matrix_item))

        k = int(input().strip())

        result = countLuck(matrix, k)

        fptr.write(result + '\n')

    fptr.close()
