from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    que = deque(people)
    while que :
        w = limit - que.popleft()
        if que and que[-1] <= w :
            que.pop()
        answer += 1
    return answer