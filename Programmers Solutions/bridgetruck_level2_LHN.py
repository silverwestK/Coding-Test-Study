"""
아이디어
다리를 구현해서 돌려본다
"""


def solution(bridge_length, weight, truck_weights):
    from collections import deque
    que = deque([0] * bridge_length)
    q = deque(truck_weights)
    count = 0
    sums = 0
    while que:
        count = count + 1
        trash = que.pop()
        if trash != 0 or que[0] != 0:
            sums = sum(que)
        if q:
            if sums + q[0] <= weight:

                que.appendleft(q.popleft())
            else:
                que.appendleft(0)

    return count