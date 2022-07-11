"""
요청시간으로 먼저 정렬
요청시간이 같으면 소요시간으로 정렬


"""
def solution(jobs):
    import heapq
    h = []
    n = len(jobs)
    check, start, now, answer = 0,-1,0,0
    while check < n:
        for i in jobs:
            if i[0] > start and i[0] <= now:
                heapq.heappush(h,[i[1],i[0]])
        if h:
            t_time, s_time = heapq.heappop(h)
            start = now
            now = now + t_time
            answer = answer + now - s_time
            check = check + 1
        else:
            now = now + 1
    return answer//n