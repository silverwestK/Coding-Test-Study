from collections import defaultdict

def solution(clothes):
    ctDict = defaultdict(lambda: 1)
    for _, ctgy in clothes:
        ctDict[ctgy] += 1
    answer = 1
    for i in ctDict.values():
        answer *= i
    return answer-1