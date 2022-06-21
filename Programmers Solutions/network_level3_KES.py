def dfs(computers, i, visited):
    visited[i] = True
    for j in range(len(computers)):
        if computers[i][j] == 1 and visited[j] == 0:
            dfs(computers, j, visited)

def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if visited[i] != True:
            dfs(computers, i, visited)
            answer += 1
    return answer