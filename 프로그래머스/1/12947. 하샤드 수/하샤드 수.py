def solution(x):
    
    hap = sum(int(i) for i in str(x))
    
    return True if x % hap ==0 else False