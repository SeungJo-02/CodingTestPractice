def solution(n, lost, reserve):
    reserve1 = set(reserve) - set(lost)
    lost1 = set(lost) - set(reserve)
    
    for i in sorted(reserve1):
        if i-1 in lost1:
            lost1.remove(i-1)
            
        elif i + 1 in lost1:
            lost1.remove(i + 1)
            
    return n-len(lost1)