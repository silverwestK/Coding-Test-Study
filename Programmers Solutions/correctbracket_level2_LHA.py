from collections import deque

def solution(s):
    if s[0] == ')' or s[-1] == '(':
        return False

    que = deque(s)
    n = 0
    while que:
        x = que.popleft()
        if x == '(':
            n -= 1
        elif x == ')':
            if n == 0:
                return False
            n += 1

    return True if n == 0 else False

