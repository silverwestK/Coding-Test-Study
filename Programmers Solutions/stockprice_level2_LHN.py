def solution(prices):
    n = len(prices)
    answer = [0]*(n)
    for i in range(n):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer