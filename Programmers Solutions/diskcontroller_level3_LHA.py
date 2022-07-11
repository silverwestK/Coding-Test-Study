from heapq import *

def solution(jobs):
    answer = 0
    t = 0
    cnt = 0
    start = -1
    tasks = []

    while cnt < len(jobs):
        for j in jobs:
            if start < j[0] <= t:
                heappush(tasks, [j[1], j[0]])

        if len(tasks) > 0:
            curr = heappop(tasks)
            start = t
            t += curr[0]
            answer += (t - curr[1])
            cnt += 1
        else:
            t += 1

    return answer // len(jobs)