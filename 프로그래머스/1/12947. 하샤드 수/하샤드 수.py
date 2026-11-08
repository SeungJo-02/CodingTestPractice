def solution(x):
    hap = sum(map(int,str(x)))
    return True if x%hap==0 else False