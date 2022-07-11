def solution(priorities, location):
    answer = 0
    while True:
        maxVal = max(priorities)
        tempVal = priorities.pop(0)
        if tempVal < maxVal:
            priorities.append(tempVal)
        else:
            answer += 1
            if location == 0:
                return answer
        location = location-1 if location > 0 else len(priorities)-1