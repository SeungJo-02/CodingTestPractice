def solution(strArr):
    answer = {}
    
    for i in strArr:
        length = len(i)
        
        answer[length] = answer.get(length,0) +1
    
    return max(answer.values())