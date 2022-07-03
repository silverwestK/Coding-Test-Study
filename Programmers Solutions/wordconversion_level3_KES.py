# 문제: 단어 변환

from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque([(0, begin)])
    while queue:
        depth, tempWord = queue.popleft()
        if tempWord == target:
            return depth

        for w in words:
            diffChar = 0
            for i in range(len(w)):
                if tempWord[i] != w[i]:
                    diffChar += 1
            if diffChar == 1:
                queue.append((depth + 1, w))
    return 0