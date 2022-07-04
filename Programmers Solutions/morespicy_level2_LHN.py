"""
문제 : 주어진 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 음식을 섞어야 하는 최소 횟수를 반환하느ㅡㄴ 문제
섞는 방법 : 가장 맵지않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 읍식의 스코빌 지수 * 2)
조건 : 모든 음식의 스코빌 지수를 K이상으로 만들 수 없으면 -1 반환
아이디어 :
heap 함수가 리스트를 힙 구조로 변환하고 가장 작은 값을 반환하는 성질을 가지기 때문에
그것을 사용하여 가장 작은 값과 그 다음 작은 값을 계산
함수 동작 과정:
scoville 리스트를 heapfiy 하여 heap 으로 만들고 heap 의 맨 첫번째 요소가 k 보다 크면 섞은 수를 반환하도록 함
"""
def solution(scoville, K):
    import heapq
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < K:
        if len(scoville) == 1:
            return - 1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        c = a + 2*b
        answer = answer + 1
        heapq.heappush(scoville,c)

    return answer