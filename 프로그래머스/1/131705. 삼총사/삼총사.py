#완전 탐색 문제로 보임
from itertools import combinations #itertools의 조합 가져오기
def solution(number):
    answer = 0
    for i in combinations(number,3):# 전체 리스트에서 3개 뽑기
        if sum(i) == 0: #3개 뽑은 거의 합이 0이면 삼총사
            answer += 1
            
    return answer