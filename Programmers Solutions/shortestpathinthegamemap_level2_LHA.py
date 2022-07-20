from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])

    start = (0, 0)
    maps[0][0] = 0
    que = deque([(start, 1, maps)])

    moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    while que:
        pos, cnt, graph = que.popleft()
        if pos == (n - 1, m - 1):
            return cnt

        for x, y in moves:
            next_x = pos[0] + x
            next_y = pos[1] + y
            if 0 <= next_x < n and 0 <= next_y < m and maps[next_x][next_y] == 1:
                maps[next_x][next_y] = 0
                que.append(((next_x, next_y), cnt + 1, maps))

    return -1