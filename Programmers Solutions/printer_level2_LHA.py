from collections import deque

def solution(priorities, location):
    answer = 0
    que = deque([(p, i) for i, p in enumerate(priorities)])

    while que:
        pri, idx = que.popleft()

        if que and max(que)[0] > pri:
            que.append((pri, idx))
        else:
            answer += 1
            if idx == location:
                break

    return answer