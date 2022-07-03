# 문제: 기능개발
from math import ceil
def solution(progresses, speeds):
    req_days = [ceil((100 - p) / s) for p, s in zip(progresses, speeds)]

    answer = []
    i, j = 0, 1
    while j < len(req_days):
        if req_days[i] >= req_days[j]:
            j += 1
        else:
            answer.append(j - i)
            i, j = j, j + 1
    answer.append(j - i)
    return answer