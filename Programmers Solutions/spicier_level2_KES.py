# 문제: 더 맵게
import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville) > 0:
        if scoville[0] >= K:
            return answer
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        spiciest, n_spiciest = heapq.heappop(scoville), heapq.heappop(scoville)
        heapq.heappush(scoville, spiciest+n_spiciest*2)
        answer += 1