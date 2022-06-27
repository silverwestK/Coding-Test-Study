def dfs(n, computers, start, visited):
    visited[start] = True
    for i, c in enumerate(computers[start]):
        if c == 1 and not visited[i]:
            dfs(n, computers, i, visited)

def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            dfs(n, computers, i, visited)
            answer += 1

    return answer