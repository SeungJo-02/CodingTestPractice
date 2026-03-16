from itertools import combinations 
def solution(numbers):
    result = [sum(k) for k in combinations(numbers,2)]
    return sorted(set(result))