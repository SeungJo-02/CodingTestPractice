def solution(x):
    hap = sum(map(int,str(x)))
    return x % hap==0 