from itertools import combinations
def solution(nums):
    answer = 0
    
    for combi in combinations(nums,3):
        sum_num = sum(combi)
        
        is_prime = True
        
        for k in range(2, int(sum_num**0.5) + 1 ):
            if sum_num % k == 0:
                is_prime = False
                break
                
        if is_prime:
            answer += 1
    
    return answer