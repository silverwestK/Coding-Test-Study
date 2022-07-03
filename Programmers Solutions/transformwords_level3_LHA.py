from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    que = deque([(begin, 0)])
    while que:
        v, depth = que.popleft()

        if v == target:
            return depth

        for w in words:
            diff = 0
            for v_c, w_c in zip(v, w):
                if v_c != w_c:
                    diff += 1
            if diff == 1 and w == target:
                depth += 1
                return depth

            elif diff == 1:
                que.append((w, depth + 1))

    return depth