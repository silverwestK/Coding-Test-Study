# 문제: 게임 맵 최단거리

from collections import deque
def solution(maps):
    n, m = len(maps[0]), len(maps)
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = deque([(0, 0)])
    while queue:
        tx, ty = queue.popleft()
        for i in range(4):
            nx, ny = tx + dx[i], ty + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[ny][nx] == 1:
                queue.append((nx, ny))
                maps[ny][nx] = maps[ty][tx] + 1

    return -1 if maps[m - 1][n - 1] == 1 else maps[m - 1][n - 1]