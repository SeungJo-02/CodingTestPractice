from itertools import combinations
def solution(numbers):
    answer = sorted(set([sum(i) for i in combinations(numbers,2)]))
    return answer