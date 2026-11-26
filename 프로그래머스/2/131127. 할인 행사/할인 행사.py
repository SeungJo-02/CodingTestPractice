#collections의 Counter
#리스트 혹은 문자열에서 각각 그 원소들이 몇 개가 나오는 지 dic으로 바꿔줌
from collections import Counter 

def solution(want, number, discount):
    choice_day = 0
    dic = dict(zip(want,number))
    
    for s in range(len(discount) -9):
        if dic == Counter(discount[s:s+10]):
            choice_day += 1 

    return choice_day