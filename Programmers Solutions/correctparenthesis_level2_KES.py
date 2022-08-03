# 문제: 올바른 괄호

def solution(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if stack and stack[-1] == "(":
                stack.pop(-1)
            else:
                return False

    return False if stack else True