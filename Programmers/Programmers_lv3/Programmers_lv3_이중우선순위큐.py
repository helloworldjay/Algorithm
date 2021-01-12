def solution(operations:list) -> list:
    import heapq
    heap = []
    for operation in operations:
        if operation[0] == "I":
            heapq.heappush(heap, int(operation[2:]))
        elif heap:
            if operation[2] == "1":
                heap.pop(heap.index(heapq.nlargest(1, heap)[0]))
            else:
                heapq.heappop(heap)
    return [heap.pop(heap.index(heapq.nlargest(1,heap)[0])), heapq.heappop(heap)] if heap else [0,0]
print(solution(["I 7","I 5","I -5","D -1"]))