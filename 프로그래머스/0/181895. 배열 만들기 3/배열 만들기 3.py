def solution(arr, intervals):
    answer = []
    for i in intervals:
        a, b = i[0], i[1]
        answer+=arr[a:b+1]
    
    
    return answer