"""
"""


def solution(priorities, location):
    from collections import deque
    stack = deque()
    for i, value in enumerate(priorities):
        stack.append([i, value])
    answer = 0
    priorities.sort(reverse=True)
    while stack:
        index, value = stack.popleft()
        if value == priorities[0]:
            del priorities[0]
            answer = answer + 1
            if index == location:
                return answer
        else:
            stack.append([index, value])

    return answer