# 문제: 다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
    answer = 1
    trk_cnt = len(truck_weights)
    passed_trk = []
    passing_trk, passing_sec = [truck_weights.pop(0)], [1]
    while len(passed_trk) < trk_cnt:
        passing_sec = [sec + 1 for sec in passing_sec]
        for sec, trk in zip(passing_sec, passing_trk):
            if sec > bridge_length:
                passing_sec.pop(0)
                passed_trk.append(passing_trk.pop(0))

        if len(truck_weights) > 0 and (sum(passing_trk) + truck_weights[0]) <= weight:
            passing_trk.append(truck_weights.pop(0))
            passing_sec.append(1)

        answer += 1

    return answer