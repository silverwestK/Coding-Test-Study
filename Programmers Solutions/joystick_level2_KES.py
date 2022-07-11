# 문제: 조이스틱

def solution(name):
    answer = 0
    minMove = len(name) - 1
    for idx, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        nextIdx = idx + 1
        while nextIdx < len(name) and name[nextIdx] == 'A':
            nextIdx += 1

        minMove = min([minMove, idx * 2 + len(name) - nextIdx, idx + 2 * (len(name) - nextIdx)])
    answer += minMove
    return answer