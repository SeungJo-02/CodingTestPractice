import heapq
def solution(k, score):
    li = []
    result = []
    for j in score:
        heapq.heappush(li,j)
        if len(li) > k:
            heapq.heappop(li)
        result.append(min(li))
        
            
    return result