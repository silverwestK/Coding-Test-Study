"""
문제제:
노드드의  수, 엣지 리스트가 주어질 때 그래프가 총 몇개 있는지 반환
엣지 리스트는 노드의 개수만큼의 요소를 가지고 있고 각 요소도 노드의 개수만큼의 요소를 가지고 있다.
[[1,1,0],[1,1,0],[0,0,1]]
[1,1,0] -> node 0은 node 0과 연결, node 1과 연결되어 있다
아이디어 :
bfs 사용
"""


def solution(n, computers):
    from collections import deque
    visited = [False] * n
    answer = 0
    while all(visited) == False:
        q = deque()
        q.append(visited.index(False))
        while q:
            cur = q.popleft()
            visited[cur] = True
            for j in range(n):
                if visited[j] == False:
                    if computers[cur][j] == 1:
                        q.append(j)
        answer = answer + 1

    return answer