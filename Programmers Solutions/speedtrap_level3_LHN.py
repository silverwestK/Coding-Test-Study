
def solution(routes):
    routes.sort()
    print(routes)
    cam = routes[0][1]
    routes.pop(0)
    answer = 1

    for i in routes:
        if i[0] <= cam:
            cam = min(i[1],cam)
        else:
            cam = i[1]
            answer+=1
    return answer

"""
def solution(routes):
    import sys
    answer = 0
    routes.sort(key=lambda x : x[1], reverse= True)
    cam = sys.maxsize
    for j in routes:
        if j[1] < cam:
            answer += 1
            cam = j[0]
        else:
            if cam < j[1]:
                cam = j[0]
    return answer
"""