import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    scoville = [x for x in scoville if x<K]
    if not len(scoville):
        return 0
    for i in scoville :
        heapq.heappush(heap, i)
        
    while heap[0]<K:
        answer += 1
        try:
            heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap)*2)
        except:
            return -1
    
    return answer