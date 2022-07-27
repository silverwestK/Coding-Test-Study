from collections import deque, defaultdict

def bfs(graph, start, end, n):
    visited = [False] * (n + 1)
    que = deque([start])
    visited[start] = True
    cnt = 0

    while que:
        s = que.popleft()
        for next_s in graph[s]:
            if next_s == end:
                continue
            if not visited[next_s]:
                visited[next_s] = True
                cnt += 1
                que.append(next_s)

    return cnt

def solution(n, wires):
    answer = 1000
    graph = defaultdict(list)

    for f, t in wires:
        graph[f].append(t)
        graph[t].append(f)

    for n1, n2 in wires:

        t1 = bfs(graph, n1, n2, n)
        t2 = bfs(graph, n2, n1, n)

        diff = abs(t1 - t2)
        if diff < answer:
            answer = diff

    return answer
