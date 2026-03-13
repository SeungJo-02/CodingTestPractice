from itertools import combinations
def solution(number):
    answer = 0
    li = list(combinations(number,3))
    for i in li:
        if sum(i) == 0:
            answer +=1
    return answer