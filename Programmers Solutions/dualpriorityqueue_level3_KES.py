# 문제: 이중우선순위큐

from heapq import heappush, heappop, heapify
def solution(operations):
    heap = []
    for op in operations:
        cmd, val = op.split(" ")

        if cmd == "I":
            heappush(heap, int(val))
        elif heap and cmd == "D" and val == '-1':
            heappop(heap)
        elif heap and cmd == "D" and val == '1':
            heap.remove(max(heap))
            heapify(heap)

    if not heap:
        return [0, 0]

    return [max(heap), heap[0]]