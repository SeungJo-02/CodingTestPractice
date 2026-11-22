#완전탐색 문제 
def solution(elements):
    n = len(elements) # 몇 번 반복
    extended = elements * 2 # 원형 수열을 위해서 리스트를 2배로
    result = set()# 중복을 제거하기 위해서 
    
    for i in range(n):
        current_sum = 0
        #i에서 부터 n까지 계속 늘려가면서 그 합을 더하기 
        for length in range(n):
            current_sum += extended[i + length]
            result.add(current_sum)
    
    return len(result)