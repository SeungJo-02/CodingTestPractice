def solution(food):
    answer = ''
    #index랑 값 뽑아두고 글자를 몫 개수만큼 더하기
    for i,v in enumerate(food):
        answer += str(i) * (v//2) 
    return answer + "0" + answer[::-1]