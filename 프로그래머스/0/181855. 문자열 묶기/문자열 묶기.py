def solution(strArr):
    answer = 0
    
    dix = {}
    
    for i in strArr:
        length = len(i)
        
        dix[length] = dix.get(length,0) + 1
    
    return max(dix.values())