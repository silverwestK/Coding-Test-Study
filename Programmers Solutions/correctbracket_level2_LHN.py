def solution(s):
    stack = []

    for i in s:
        if i == '(':
            stack.append(1)
        elif i == ')':
            try:
                stack.pop()
            except:
                return False
    if len(stack) != 0:
        return False
    return True