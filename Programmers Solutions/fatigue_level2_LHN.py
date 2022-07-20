def solution(k, dungeons):
    from collections import deque
    q = deque()
    q.append([k,dungeons,0])
    max_count = 0
    while q:
        cur_hp, left_d, count = q.popleft()
        if max_count < count:
            max_count = count
        for i in range(len(left_d)):
            if cur_hp >= left_d[i][0]:
                q.append([cur_hp-left_d[i][1],left_d[0:i]+left_d[i+1:],count + 1])
    return max_count