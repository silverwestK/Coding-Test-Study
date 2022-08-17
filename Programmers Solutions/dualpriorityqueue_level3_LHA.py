def solution(operations):
    que = []

    for op in operations:
        if op.startswith('D'):
            if len(que) == 0:
                pass
            else:
                if '-' in op:
                    que.remove(min(que))
                else:
                    que.remove(max(que))
        else:
            que.append(int(op.split(' ')[-1]))

    if que:
        return [max(que), min(que)]
    else:
        return [0, 0]
