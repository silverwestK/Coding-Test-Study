from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:
        t = 0
        cur = prices.popleft()

        for p in prices:
            t += 1
            if cur > p:
                break
        answer.append(t)

    return answer