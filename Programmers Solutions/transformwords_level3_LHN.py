"""
아이디어 :
문자열을 비교하는 함수 생성
"""


def check_word(begin, check):
    count = 0
    for i in check:
        if count > 1:
            break
        if i not in begin:
            count = count + 1
        else:
            begin = begin.replace(i, '', 1)
    if count <= 1:
        return True
    else:
        return False


def solution(begin, target, words):
    from collections import deque
    if target not in words:
        return 0
    q = deque()
    answer = 1
    words.append(begin)
    visited = [False] * len(words)
    q.append([len(words) - 1, answer])
    while q:
        cur_point, answer = q.popleft()
        visited[cur_point] = True
        for i in range(len(words) - 1):
            if check_word(words[cur_point], words[i]) and visited[i] == False:
                if words[i] == target:
                    return answer
                q.append([i, answer + 1])
    return 0