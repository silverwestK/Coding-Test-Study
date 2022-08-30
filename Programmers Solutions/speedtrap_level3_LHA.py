def solution(routes):
    routes.sort(key=lambda x: x[1])
    _, OUT = routes.pop(0)
    answer = 1

    for r in routes:
        if r[0] > OUT:
            answer += 1
            OUT = r[1]

    return answer