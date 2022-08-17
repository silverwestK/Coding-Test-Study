def solution(operations):
    import heapq
    heap = []
    for i in operations:
        i = list(i.split(" "))
        if i[0] == "I":
            heapq.heappush(heap,int(i[1]))
        elif i[0] == "D" and len(heap) > 0:
            if int(i[1]) == -1:
                heapq.heappop(heap)
            else:
                heap.sort(reverse=True)
                heap = heap[1:]
                heapq.heapify(heap)
    if len(heap) == 0:
        return [0,0]
    else:
        heap.sort()
        return [heap[-1],heap[0]]