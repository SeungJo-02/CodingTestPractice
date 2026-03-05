def solution(arr):
    l = len(arr)
    target = 1
    
    while(target < l):
        target *= 2
        
    arr += [0]*(target - l)
    
    return arr