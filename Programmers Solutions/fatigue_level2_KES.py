# 문제: 피로도

from itertools import permutations
def solution(k, dungeons):
    answer = -1
    for perm in permutations(dungeons, len(dungeons)):
        stamina = k
        explored = 0

        for minimum, consumed in perm:
            if minimum <= stamina:
                stamina -= consumed
                explored += 1
            if stamina <= 0:
                break

        answer = max(answer, explored)

    return answer