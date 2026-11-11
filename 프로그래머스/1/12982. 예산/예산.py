def solution(d, budget):
    answer = 0
    d = sorted(d) #가장 작은 것부터 예산 빼기 
    for i in d: 
        if budget - i >= 0: #예산 - 가격해서 남으면 올리고
            budget -= i
            answer += 1
        else: # 아니면 바로 리턴해서 끝내기
            return answer
    return answer
    