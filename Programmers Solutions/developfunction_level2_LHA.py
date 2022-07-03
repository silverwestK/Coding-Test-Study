from math import ceil
def solution(progresses, speeds):
    answer = []

    days = [ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    release = 1

    while days:
        d = days.pop(0)
        if len(days) != 0:
            if d >= days[0]:
                days[0] = d
                release += 1
            else:
                answer.append(release)
                release = 1
        else:
            answer.append(release)

    return answer