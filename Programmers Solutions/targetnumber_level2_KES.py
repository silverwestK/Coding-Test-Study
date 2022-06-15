def solution(numbers, target):
    from collections import deque
    answer = 0
    queue = deque([(0,0)])
    while queue:
        total, index = queue.popleft()
        if index > len(numbers):
            break
        elif index == len(numbers) and target == total:
            answer +=1
        value = numbers[index-1]
        queue.append((total+value, index+1))
        queue.append((total-value, index+1))
    return answer