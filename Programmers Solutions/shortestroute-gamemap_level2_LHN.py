"""
문제 : 시작(0,0)에서 끝 (nxm) 까지의 최소 거리
조건 :
n과 m은 같을 수도 다를 수도 있다
게임 칸 중에서 0은 가지 못하는 부분 1은 갈 수 있는 부분
끝까지 가지 못하는 경우 : -1 리턴
"""
def solution(maps):
    from collections import deque
    q = deque()
    q.append([[0,0],1])
    n = len(maps)
    m = len(maps[0])
    move = [[-1,0],[0,-1],[1,0],[0,1]]
    if maps[n-2][m-1] == 0 and maps[n-1][m-2] == 0:
        return -1
    maps[0][0] = 0
    while q:
        cur, count = q.popleft()
        if cur[0] == n-1 and cur[1] == m-1:
            return count
        for i in move:
            x = cur[0] + i[0]
            y = cur[1] + i[1]
            if x >= 0 and y >= 0 and x < n and y < m and maps[x][y] == 1:
                maps[x][y] = 0
                q.append([[x,y],count + 1])
    return -1