import os

def bfs(n, i, j):
    checkVisit = [[0] * n for _ in range(n)]
    queue = [[0, 0]]
    dx, dy = [i, i, -i, -i, j, -j, j, -j], [j, -j, j, -j, i, i, -i, -i]
    while queue:
        px, py = queue.pop(0)
        for p in range(8):
            nx, ny = px + dx[p], py + dy[p]
            if 0 <= nx < n and 0 <= ny < n and checkVisit[nx][ny] == 0:
                queue.append([nx, ny])
                checkVisit[nx][ny] = checkVisit[px][py] + 1
    return -1 if checkVisit[n - 1][n - 1] == 0 else checkVisit[n - 1][n - 1]


def knightlOnAChessboard(n):
    result = [[0] * (n - 1) for _ in range(n - 1)]
    for i in range(1, n):
        for j in range(i, n):
            val = bfs(n, i, j)
            result[i - 1][j - 1], result[j - 1][i - 1] = val, val
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
