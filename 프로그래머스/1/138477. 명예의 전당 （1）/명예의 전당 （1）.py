import heapq
def solution(k, score):
    result = []
    honor = []
    for i in score:
        heapq.heappush(honor,i)
        if len(honor) > k:
            heapq.heappop(honor)
        result.append(honor[0])
    return result