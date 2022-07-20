def solution(bridge_length, weight, truck_weights):
    time = 0
    que = [0] * bridge_length

    while que:
        time += 1
        que.pop(0)
        if truck_weights:
            if sum(que) + truck_weights[0] <= weight:
                que.append(truck_weights.pop(0))
            else:
                que.append(0)

    return time