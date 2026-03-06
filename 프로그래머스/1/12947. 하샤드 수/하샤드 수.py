def solution(x):

    hap = sum(int(i) for i in str(x))
    
    if x % hap == 0:
        return True
    else:
        return False
    
